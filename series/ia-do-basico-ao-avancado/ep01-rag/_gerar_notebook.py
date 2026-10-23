"""Gera ep01-rag/rag_duas_fases.ipynb (Episódio 1 da série)."""
import nbformat as nbf, sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "GHDaru/linkedinmaterial"
PATH = "series/ia-do-basico-ao-avancado/ep01-rag/rag_duas_fases.ipynb"
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))

md(f"""
# Episódio 1 · RAG em duas fases

<a href="https://colab.research.google.com/github/{REPO}/blob/main/{PATH}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir no Colab"/></a>

![RAG em duas fases](https://raw.githubusercontent.com/{REPO}/main/series/ia-do-basico-ao-avancado/ep01-rag/rag-duas-fases.gif)

Este notebook implementa, passo a passo, o mesmo fluxo do GIF acima. Cada etapa é uma célula curta para você rodar e ver o que ela faz.

| Fase | Etapa | O que acontece |
|---|---|---|
| **1 · Indexação** (offline) | Documentos | Os arquivos da empresa entram no pipeline |
| | Chunking | Cada documento é quebrado em pedaços menores |
| | Embedding | Cada chunk vira um vetor |
| | Vector DB | Os vetores são gravados num índice |
| **2 · Recuperação e geração** (tempo real) | Pergunta | O usuário pergunta em linguagem natural |
| | Embedding | A pergunta passa pelo **mesmo** modelo de embedding |
| | Busca top-k | O índice devolve os k chunks mais próximos |
| | Prompt | Os chunks recuperados entram no prompt |
| | Resposta | O LLM responde com base no contexto e cita as fontes |

**Como rodar:** `Ambiente de execução → Executar tudo`. A GPU é opcional. Para gerar a resposta com o Claude, cadastre a chave `ANTHROPIC_API_KEY` em *Secrets* (ícone de chave na barra lateral do Colab). Sem chave, o notebook usa um modelo aberto pequeno (Qwen 2.5) e, se nem isso for possível, mostra o prompt pronto para você colar em qualquer chat.
""")

md("## 0 · Instalação")
code("""
%pip install -q sentence-transformers anthropic scikit-learn pandas matplotlib
""")
code("""
import os, re, textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_colwidth", 120)
""")

md("""
---
# Fase 1 · Indexação

Roda **uma vez** (ou sempre que os documentos mudam). Em produção é um job em lote: lê as fontes, quebra, gera vetores e grava no banco.

## 1.1 · Documentos

Três fontes fictícias de uma distribuidora, com formatos diferentes de propósito: um contrato (texto corrido), um SLA (markdown) e uma planilha de pedidos (CSV).
""")
code('''
documentos = {
    "contrato.pdf": """
Cláusula 5. O pedido mínimo é de 20 caixas por SKU, consolidadas por centro de distribuição.
Cláusula 6. O pagamento será efetuado em 30 dias corridos a partir da emissão da nota fiscal.
Cláusula 7. A entrega ocorrerá em até 3 dias úteis após o faturamento do pedido, para capitais e regiões metropolitanas do Sul.
Cláusula 8. Em caso de atraso na entrega, incide multa de 2% sobre o valor do pedido, limitada a 10%.
Cláusula 9. Devoluções por avaria devem ser registradas em até 48 horas após o recebimento.
""",
    "sla_logistica.md": """
# SLA de logística
## Separação
A separação no CD acontece em até 4 horas após a liberação do pedido pelo financeiro.
## Expedição
Pedidos B2B saem do CD em até 24 horas após o faturamento. Pedidos de e-commerce saem no mesmo dia se faturados até 14 h.
## Transporte
A coleta pela transportadora é diária, às 16 h. Rotas para o interior têm prazo adicional de 2 dias úteis.
""",
    "pedidos.csv": """pedido,cliente,cidade,status,data_faturamento
4519,Mercado Bom,Joinville,entregue,2026-10-13
4520,Super Vale,Blumenau,em transporte,2026-10-19
4521,Lojas Sul,Curitiba,faturado,2026-10-21
4522,Atacado Norte,Chapecó,aguardando pagamento,
4523,Casa Real,Florianópolis,em separação,
""",
}
for nome, texto in documentos.items():
    print(f"{nome:18} {len(texto):5} caracteres")
''')

md("""
## 1.2 · Chunking

Um chunk é o pedaço de texto que será recuperado inteiro. Se ele for grande demais, a busca traz muito texto irrelevante junto. Se for pequeno demais, a informação se perde entre pedaços.

Duas decisões aparecem aqui:
- **Tamanho e sobreposição.** O texto é agrupado frase a frase até um limite de caracteres, e a última frase de um chunk se repete no começo do seguinte (*overlap*), para que nenhuma ideia fique cortada no meio. Em produção é comum usar ~500 tokens com overlap de 50.
- **O formato manda.** Em CSV, cada linha vira um chunk e leva o nome das colunas junto, senão "4521, Lojas Sul, faturado" perde o significado.
""")
code('''
def frases(texto):
    linhas = [l.strip("# ").strip() for l in texto.strip().splitlines() if l.strip()]
    out = []
    for l in linhas:
        out += [f.strip() for f in re.split(r"(?<=[^\\d\\s][.!?])\\s+", l) if f.strip()]
    return out

def chunk_texto(texto, tamanho=180, sobreposicao=1):
    fs, chunks, atual = frases(texto), [], []
    for f in fs:
        if atual and len(" ".join(atual + [f])) > tamanho:
            chunks.append(" ".join(atual))
            atual = atual[-sobreposicao:] if sobreposicao else []
        atual.append(f)
    if atual:
        chunks.append(" ".join(atual))
    return chunks

def chunk_csv(texto):
    linhas = texto.strip().splitlines()
    cab = linhas[0].split(",")
    return ["; ".join(f"{c}: {v or '—'}" for c, v in zip(cab, l.split(","))) for l in linhas[1:]]

def fazer_chunks(documentos, tamanho=180, sobreposicao=1):
    registros = []
    for fonte, texto in documentos.items():
        partes = chunk_csv(texto) if fonte.endswith(".csv") else chunk_texto(texto, tamanho, sobreposicao)
        for i, p in enumerate(partes, 1):
            registros.append({"id": f"{fonte}#{i}", "fonte": fonte, "texto": p})
    return pd.DataFrame(registros)

chunks = fazer_chunks(documentos)
print(len(chunks), "chunks")
chunks
''')

md("""
## 1.3 · Embedding

Um modelo de embedding transforma texto em um vetor de números. Textos com significado parecido viram vetores próximos, mesmo sem palavras em comum.

Aqui usamos `paraphrase-multilingual-MiniLM-L12-v2`, um modelo aberto, pequeno (384 dimensões) e bom em português. Se o download falhar (sem internet, por exemplo), o notebook cai para TF-IDF, que compara palavras em vez de significado. O fluxo é o mesmo, mas a qualidade da busca cai, e isso já é uma lição do episódio.
""")
code('''
MODELO_EMBEDDING = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
STOPWORDS_PT = ("a o e de da do das dos em no na nos nas um uma para por com que se ao aos as os "
                "qual quais é ser sera sao foi tem ate apos sobre mais mesmo").split()

class Embedder:
    """Mesma interface para os dois backends: encode(lista_de_textos) -> matriz normalizada."""
    def __init__(self, nome=MODELO_EMBEDDING):
        try:
            from sentence_transformers import SentenceTransformer
            self.modelo = SentenceTransformer(nome)
            self.backend = nome
        except Exception as e:
            from sklearn.feature_extraction.text import TfidfVectorizer
            print(f"Modelo neural indisponível ({type(e).__name__}). Usando TF-IDF como reserva.")
            self.modelo, self.backend = None, "tfidf"
            self.tfidf = TfidfVectorizer(strip_accents="unicode", lowercase=True, stop_words=STOPWORDS_PT)

    def fit(self, textos):
        if self.modelo is None:
            self.tfidf.fit(textos)
        return self

    def encode(self, textos):
        if self.modelo is not None:
            v = self.modelo.encode(list(textos), normalize_embeddings=True)
        else:
            v = self.tfidf.transform(textos).toarray()
            v = v / np.clip(np.linalg.norm(v, axis=1, keepdims=True), 1e-9, None)
        return np.asarray(v, dtype=np.float32)

embedder = Embedder().fit(chunks.texto)
vetores = embedder.encode(chunks.texto)
print("backend:", embedder.backend)
print("matriz de vetores:", vetores.shape, "→ um vetor por chunk")
print("primeiro vetor:", np.round(vetores[0, :6], 3), "...")
''')

md("""
## 1.4 · Banco vetorial

O banco vetorial guarda os vetores e os metadados (texto, fonte) e responde a uma pergunta: *quais vetores estão mais perto deste?*

Para ficar transparente, o índice abaixo tem 15 linhas de NumPy. Com vetores normalizados, a similaridade de cosseno é só um produto escalar. Em produção você trocaria por FAISS, pgvector, Qdrant ou similar, que fazem a mesma conta com índices aproximados para milhões de vetores.
""")
code('''
class IndiceVetorial:
    def __init__(self):
        self.vetores, self.meta = None, []

    def adicionar(self, vetores, metadados):
        self.vetores = vetores if self.vetores is None else np.vstack([self.vetores, vetores])
        self.meta += metadados

    def buscar(self, vetor_consulta, k=3):
        scores = self.vetores @ vetor_consulta          # cosseno, pois tudo está normalizado
        idx = np.argsort(-scores)[:k]
        return [{**self.meta[i], "score": float(scores[i])} for i in idx]

    def __len__(self):
        return 0 if self.vetores is None else len(self.vetores)

indice = IndiceVetorial()
indice.adicionar(vetores, chunks.to_dict("records"))
print(f"Índice com {len(indice)} vetores. Fase 1 concluída.")
''')

md("""
---
# Fase 2 · Recuperação e geração

Roda **a cada pergunta**, em tempo real.

## 2.1 · Pergunta
""")
code('''
pergunta = "Qual o prazo de entrega do pedido 4521?"
''')

md("""
## 2.2 · Embedding da pergunta

A pergunta passa pelo **mesmo** modelo usado na indexação. Se você trocar o modelo, precisa reindexar tudo: vetores de modelos diferentes não são comparáveis.
""")
code('''
vq = embedder.encode([pergunta])[0]
print("vetor da pergunta:", vq.shape, np.round(vq[:6], 3), "...")
''')

md("""
## 2.3 · Busca top-k

O índice devolve os `k` chunks mais próximos da pergunta, com o score de similaridade de cada um.
""")
code('''
K = 3
recuperados = indice.buscar(vq, k=K)
pd.DataFrame(recuperados)[["score", "id", "texto"]].round(3)
''')

md("""
### Como isso parece no espaço vetorial

Os vetores têm centenas de dimensões. Para enxergar, projetamos tudo em 2D com PCA. A projeção distorce distâncias, então use o gráfico só como intuição. O losango é a pergunta e os círculos destacados são os top-k.
""")
code('''
from sklearn.decomposition import PCA

def plotar_espaco(pergunta, recuperados):
    vq = embedder.encode([pergunta])[0]
    pts = PCA(n_components=2, random_state=0).fit_transform(np.vstack([indice.vetores, vq]))
    cores = {"contrato.pdf": "#0A84FF", "sla_logistica.md": "#5E5CE6", "pedidos.csv": "#40C8E0"}
    top = {r["id"] for r in recuperados}
    fig, ax = plt.subplots(figsize=(7, 5.5))
    for (x, y), m in zip(pts[:-1], indice.meta):
        ax.scatter(x, y, s=140 if m["id"] in top else 50, color=cores.get(m["fonte"], "#8E9AB4"),
                   edgecolor="#111725" if m["id"] in top else "none", linewidth=1.5, zorder=3)
        ax.annotate(m["id"], (x, y), xytext=(6, 4), textcoords="offset points", fontsize=8, color="#596379")
    qx, qy = pts[-1]
    for (x, y), m in zip(pts[:-1], indice.meta):
        if m["id"] in top:
            ax.plot([qx, x], [qy, y], color="#0A84FF", lw=1.5, zorder=2)
    ax.scatter(qx, qy, marker="D", s=120, color="#111725", zorder=4)
    ax.annotate("pergunta", (qx, qy), xytext=(8, -12), textcoords="offset points", fontsize=10, weight="bold")
    for f, c in cores.items():
        ax.scatter([], [], color=c, label=f)
    ax.legend(frameon=False, fontsize=9, loc="best")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title(f"Espaço vetorial (PCA 2D) · backend: {embedder.backend.split('/')[-1]}", fontsize=11)
    plt.show()

plotar_espaco(pergunta, recuperados)
''')

md("""
## 2.4 · Prompt aumentado

O "A" de RAG é isto: o prompt passa a levar os trechos recuperados. A instrução de sistema pede que o modelo use **só** o contexto e cite a fonte de cada afirmação, e é o que reduz a alucinação.
""")
code('''
SISTEMA = ("Você é um assistente de operações. Responda em português usando SOMENTE o contexto fornecido. "
           "Cite a fonte de cada afirmação entre colchetes, por exemplo [contrato.pdf#3]. "
           "Se o contexto não tiver a resposta, diga que não encontrou a informação.")

def montar_prompt(pergunta, recuperados):
    contexto = "\\n".join(f"[{r['id']}] {r['texto']}" for r in recuperados)
    return f"Contexto:\\n{contexto}\\n\\nPergunta: {pergunta}"

prompt = montar_prompt(pergunta, recuperados)
print("SYSTEM:", SISTEMA, "\\n")
print(prompt)
''')

md("""
## 2.5 · Resposta do LLM

A função `gerar` tenta três caminhos, nesta ordem:
1. **Claude**, se houver `ANTHROPIC_API_KEY` nos Secrets do Colab ou no ambiente.
2. **Qwen 2.5 Instruct**, modelo aberto que roda no próprio Colab (1.5B com GPU, 0.5B sem GPU).
3. **Sem LLM**, quando nenhum dos dois funciona: devolve o prompt para você testar em qualquer chat.
""")
code('''
MODELO_CLAUDE = "claude-haiku-5-5"
_llm_local = None

def _chave_anthropic():
    try:
        from google.colab import userdata
        return userdata.get("ANTHROPIC_API_KEY")
    except Exception:
        return os.environ.get("ANTHROPIC_API_KEY")

def gerar(prompt, sistema=SISTEMA, max_tokens=300):
    global _llm_local
    chave = _chave_anthropic()
    if chave:
        import anthropic
        msg = anthropic.Anthropic(api_key=chave).messages.create(
            model=MODELO_CLAUDE, max_tokens=max_tokens, system=sistema,
            messages=[{"role": "user", "content": prompt}])
        return msg.content[0].text, MODELO_CLAUDE
    try:
        import torch
        from transformers import pipeline
        nome = "Qwen/Qwen2.5-1.5B-Instruct" if torch.cuda.is_available() else "Qwen/Qwen2.5-0.5B-Instruct"
        if _llm_local is None or _llm_local[0] != nome:
            _llm_local = (nome, pipeline("text-generation", model=nome, device_map="auto"))
        msgs = [{"role": "system", "content": sistema}, {"role": "user", "content": prompt}]
        out = _llm_local[1](msgs, max_new_tokens=max_tokens, do_sample=False)
        return out[0]["generated_text"][-1]["content"], nome
    except Exception as e:
        return f"(Sem LLM disponível: {type(e).__name__}. Cole o prompt acima em qualquer chat.)", "nenhum"

resposta, modelo_usado = gerar(prompt)
print(f"[{modelo_usado}]\\n")
print(textwrap.fill(resposta, 100))
''')

md("""
## 2.6 · Tudo junto: a função `rag()`

As duas fases inteiras cabem em poucas linhas. A indexação já foi feita; a cada pergunta rodam embedding, busca, prompt e geração.
""")
code('''
def rag(pergunta, k=3, mostrar=True):
    vq = embedder.encode([pergunta])[0]
    rec = indice.buscar(vq, k=k)
    resp, modelo = gerar(montar_prompt(pergunta, rec))
    if mostrar:
        print("Pergunta:", pergunta)
        for r in rec:
            print(f"  {r['score']:.2f}  {r['id']:20} {r['texto'][:70]}")
        print(f"Resposta [{modelo}]:", textwrap.fill(resp, 100, subsequent_indent="  "), "\\n")
    return resp, rec

_ = rag("Qual o prazo de entrega do pedido 4521?")
_ = rag("Quanto tempo tenho para devolver um produto avariado?")
''')

md("""
---
# Experimentos

## A · Pergunta sem resposta na base

O RAG convencional **sempre** devolve k chunks, mesmo quando nenhum é relevante. Compare os scores da pergunta abaixo com os das anteriores.
""")
code('''
_ = rag("Qual é a política de home office da empresa?")
''')
md("""
Mesmo quando os scores caem, os chunks continuam indo para o prompt. Duas defesas simples:
- uma instrução de sistema que manda dizer "não encontrei" (já está no `SISTEMA`);
- um **limiar mínimo de score**, que descarta chunks fracos antes do prompt.

O valor do limiar depende do modelo de embedding. Descobrir o valor certo é tarefa de avaliação, tema do Episódio 8 (Evals).
""")
code('''
# O limiar depende do backend: scores de TF-IDF são bem mais baixos que os de um modelo neural.
LIMIAR = 0.10 if embedder.backend == "tfidf" else 0.40

def rag_com_limiar(pergunta, k=3, limiar=LIMIAR):
    vq = embedder.encode([pergunta])[0]
    rec = [r for r in indice.buscar(vq, k=k) if r["score"] >= limiar]
    if not rec:
        return "Não encontrei essa informação nos documentos.", []
    return gerar(montar_prompt(pergunta, rec))[0], rec

for p in ["Qual o prazo de entrega do pedido 4521?", "Qual é a política de home office da empresa?"]:
    resp, rec = rag_com_limiar(p)
    print(p, "→", len(rec), "chunks acima do limiar\\n ", textwrap.fill(resp, 100, subsequent_indent="  "), "\\n")
''')

md("""
## B · Tamanho do chunk muda o que é recuperado

Reindexe com chunks maiores e veja a mesma pergunta trazer mais texto, e mais ruído, por chunk.
""")
code('''
for tamanho in (120, 400):
    ch = fazer_chunks(documentos, tamanho=tamanho)
    emb = Embedder().fit(ch.texto)
    idx = IndiceVetorial(); idx.adicionar(emb.encode(ch.texto), ch.to_dict("records"))
    top = idx.buscar(emb.encode(["Qual o prazo de entrega do pedido 4521?"])[0], k=1)[0]
    print(f"tamanho={tamanho:3} → {len(ch):2} chunks | top-1 ({top['score']:.2f}): {top['texto'][:110]}...")
''')

md("""
## C · Busca semântica, não por palavra

A pergunta abaixo não usa nenhuma palavra do trecho certo ("multa", "atraso"). Um modelo neural tem chance de achar a Cláusula 8 pelo significado. O TF-IDF, que só compara palavras, não tem como. Rode com os dois backends e compare. Aprofundamos isso no Episódio 3 (Embeddings).
""")
code('''
_ = rag("O que acontece se a mercadoria chegar depois do combinado?", k=2)
''')

md("""
---
# Onde o RAG convencional para

| Limite | Sintoma | Episódio |
|---|---|---|
| Recupera por proximidade, não por relação | "Quais clientes do Sul têm pedido atrasado?" exige cruzar contrato, SLA e pedidos | 9 · Grafo de conhecimento |
| Contexto longo se degrada | Com k grande, o modelo ignora trechos no meio do prompt | 4 · Contexto e prompt |
| Sem medição, não há melhoria | Como saber se o limiar, o k ou o chunk estão certos? | 8 · Evals |
| Uma busca, uma resposta | Perguntas que pedem várias etapas ou ferramentas | 5 · Ferramentas e MCP |

### Exercícios
1. Adicione um quarto documento (por exemplo, uma tabela de frete por região) e pergunte o prazo para um pedido do interior.
2. Troque `MODELO_EMBEDDING` por `intfloat/multilingual-e5-small`. Esse modelo pede os prefixos `query:` e `passage:`. O que muda nos scores?
3. Mude `K` para 1 e para 6. Quando a resposta piora?
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata = {"colab": {"provenance": [], "toc_visible": True},
               "kernelspec": {"name": "python3", "display_name": "Python 3"},
               "language_info": {"name": "python"}}
import pathlib
pathlib.Path(PATH).parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, PATH)
print("ok", PATH, len(cells), "células")
