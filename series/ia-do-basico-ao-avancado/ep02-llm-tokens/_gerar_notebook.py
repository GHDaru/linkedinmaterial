"""Gera series/ia-do-basico-ao-avancado/ep02-llm-tokens/llm_tokens.ipynb (Episódio 2)."""
import nbformat as nbf, pathlib, sys

REPO = sys.argv[1] if len(sys.argv) > 1 else "GHDaru/linkedinmaterial"
PATH = "series/ia-do-basico-ao-avancado/ep02-llm-tokens/llm_tokens.ipynb"
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))

md(f"""
# Episódio 2 · LLM e tokens

<a href="https://colab.research.google.com/github/{REPO}/blob/main/{PATH}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir no Colab"/></a>

![LLM e tokens](https://raw.githubusercontent.com/{REPO}/main/series/ia-do-basico-ao-avancado/ep02-llm-tokens/llm-tokens.gif)

Um LLM não consulta nada sozinho. Ele **completa texto, um token por vez**, sorteando o próximo entre os mais prováveis. Este notebook mostra isso por dentro, com um modelo aberto pequeno que roda no Colab **sem GPU e sem chave de API**:

| Seção | O que você vai ver |
|---|---|
| 1 · A pergunta | O modelo responde sobre um fornecedor que não conhece |
| 2 · Tokens | Como o texto é picado, e por que português costuma gastar mais |
| 3 · Próximo token | As probabilidades que o modelo dá para cada continuação |
| 4 · Passo a passo | A resposta sendo montada token por token |
| 5 · Temperatura | Mesma pergunta, respostas diferentes |
| 6 · Custo e janela | Quanto custam os tokens e quanto cabe no contexto |
| 7 · Ponte com o Ep. 1 | A mesma pergunta, agora com o dado certo no prompt |

**Como rodar:** `Ambiente de execução → Executar tudo`. O download do modelo (~1 GB) leva um ou dois minutos na primeira vez.
""")

md("## 0 · Instalação e modelo")
code("""
%pip install -q transformers tiktoken
""")
code('''
import os, math, textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from IPython.display import HTML, display

# Modelo aberto pequeno (0,5 bilhão de parâmetros), roda em CPU.
MODELO = os.environ.get("MODELO_EP2", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODELO)
modelo = AutoModelForCausalLM.from_pretrained(MODELO, torch_dtype=torch.float32)
modelo.eval()
print("modelo:", MODELO, "|", f"{sum(p.numel() for p in modelo.parameters())/1e6:.0f} milhões de parâmetros")
''')

md("""
---
## 1 · A pergunta, sem contexto

A mesma pergunta da animação. O modelo nunca viu o "fornecedor Alfa" nem o "item 7781": eles não existem. Repare no que ele faz.
""")
code('''
PERGUNTA = "Qual o lead time do fornecedor Alfa para o item 7781?"
SISTEMA = "Você é um assistente de supply chain. Responda em português, em uma frase."

def mensagens(pergunta, contexto=None):
    usuario = pergunta if contexto is None else f"Contexto:\\n{contexto}\\n\\nPergunta: {pergunta}"
    return [{"role": "system", "content": SISTEMA}, {"role": "user", "content": usuario}]

def ids_do_prompt(msgs, prefixo_resposta=""):
    texto = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True) + prefixo_resposta
    return tok(texto, return_tensors="pt", add_special_tokens=False).input_ids

@torch.no_grad()
def responder(pergunta, contexto=None, temperatura=0.0, max_novos=40, semente=0):
    ids = ids_do_prompt(mensagens(pergunta, contexto))
    torch.manual_seed(semente)
    extra = dict(do_sample=True, temperature=temperatura, top_p=1.0, top_k=0) if temperatura > 0 else dict(do_sample=False)
    out = modelo.generate(ids, max_new_tokens=max_novos, pad_token_id=tok.eos_token_id, **extra)
    return tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).strip()

print(PERGUNTA)
print("→", responder(PERGUNTA))
''')
md("""
Se ele respondeu com um prazo, esse número foi **inventado**: não existe nenhuma fonte para ele. Se ele disse que não sabe, ótimo, mas isso depende do modelo e da forma da pergunta. A seção 3 mostra que, por dentro, ele continua atribuindo probabilidade a vários prazos plausíveis.
""")

md("""
---
## 2 · Tokens: o texto picado em pedaços

O modelo não lê letras nem palavras. Ele lê **tokens**, pedaços de palavra com um número de identificação. Cada modelo tem seu próprio tokenizador. Abaixo, o tokenizador do modelo que estamos usando:
""")
code('''
CORES = ["#DCEBFF", "#E4E3FB", "#DDF5E4", "#FFEFD6"]

def mostrar_tokens(texto, tokenizador=None):
    tokenizador = tokenizador or tok
    # recorta cada token do texto original (evita "�" quando um acento cai entre dois tokens)
    enc = tokenizador(texto, add_special_tokens=False, return_offsets_mapping=True)
    ids = enc["input_ids"]
    pedacos = [texto[a:b] for a, b in enc["offset_mapping"]]
    spans = "".join(
        f'<span style="background:{CORES[k % 4]};padding:3px 2px;margin:1px;border-radius:4px;'
        f'font-family:monospace;white-space:pre">{p.replace(" ", "·")}</span>'
        for k, p in enumerate(pedacos))
    display(HTML(f"<div style='line-height:2.2'>{spans} <b>→ {len(ids)} tokens</b></div>"))
    return len(ids)

mostrar_tokens(PERGUNTA)
mostrar_tokens("What is the lead time of supplier Alfa for item 7781?")
''')
md("""
Repare no número **7781**: dependendo do tokenizador, ele vira um token por dígito ou pedaços como `778` + `1`. O modelo não "vê" o número 7781; vê pedaços. Por isso LLMs erram contas que uma planilha acerta.

### Português gasta mais tokens?

Na maioria dos tokenizadores, sim, porque eles foram treinados com mais texto em inglês. Mas a diferença varia muito de um tokenizador para outro. Vamos medir em vez de chutar:
""")
code('''
PARES = [
    ("Qual o lead time do fornecedor Alfa para o item 7781?",
     "What is the lead time of supplier Alfa for item 7781?"),
    ("O fornecedor entrega a mercadoria no centro de distribuição em quinze dias úteis após o faturamento.",
     "The supplier delivers the goods to the distribution center fifteen business days after invoicing."),
    ("A ruptura de estoque na loja reduz as vendas e piora o nível de serviço ao cliente.",
     "A stockout at the store reduces sales and worsens the customer service level."),
]

contadores = {f"{MODELO.split('/')[-1]}": lambda s: len(tok.encode(s, add_special_tokens=False))}
try:
    import tiktoken
    for nome in ("o200k_base", "cl100k_base"):
        enc = tiktoken.get_encoding(nome)
        contadores[nome] = lambda s, enc=enc: len(enc.encode(s))
except Exception as e:
    print(f"tiktoken indisponível ({type(e).__name__}); medindo só com o tokenizador do modelo.")

linhas = []
for pt, en in PARES:
    for nome, contar in contadores.items():
        a, b = contar(pt), contar(en)
        linhas.append({"frase": pt[:45] + "…", "tokenizador": nome, "pt": a, "en": b, "pt/en": round(a / b, 2)})
pd.DataFrame(linhas)
''')
md("""
`o200k_base` é o tokenizador dos modelos recentes da OpenAI e `cl100k_base` o da geração anterior. Tokenizadores novos reduziram bastante a diferença do português, mas ela não sumiu nas frases mais longas. Como **custo e limite de contexto são contados em tokens**, a mesma conversa em português pode custar mais que em inglês.
""")

md("""
---
## 3 · O próximo token

Por dentro, a cada passo o modelo produz uma **probabilidade para cada token do vocabulário**. Vamos começar a resposta por ele ("O lead time do fornecedor Alfa para o item 7781 é de") e ver o que ele considera para o próximo token.
""")
code('''
PREFIXO = "O lead time do fornecedor Alfa para o item 7781 é de"

@torch.no_grad()
def proximos_tokens(prefixo, k=8, pergunta=PERGUNTA, contexto=None):
    ids = ids_do_prompt(mensagens(pergunta, contexto), prefixo)
    probs = torch.softmax(modelo(ids).logits[0, -1], dim=-1)
    top = torch.topk(probs, k)
    return pd.DataFrame({"token": [repr(tok.decode([i])) for i in top.indices.tolist()],
                         "probabilidade": top.values.numpy().round(4)})

top = proximos_tokens(PREFIXO)
top
''')
md("""
Em vários modelos, os candidatos são um espaço ou um único dígito, porque números são picados em tokens. Para comparar **prazos inteiros** ("15 dias", "30 dias"...), somamos o log da probabilidade de cada token da continuação. É a chance que o modelo dá para aquela frase sair inteira:
""")
code('''
@torch.no_grad()
def prob_continuacao(prefixo, continuacao, pergunta=PERGUNTA, contexto=None):
    base = ids_do_prompt(mensagens(pergunta, contexto), prefixo)
    cont = tok(continuacao, add_special_tokens=False, return_tensors="pt").input_ids
    ids = torch.cat([base, cont], dim=1)
    logp = torch.log_softmax(modelo(ids).logits[0, :-1], dim=-1)
    alvo = ids[0, 1:]
    pos = torch.arange(base.shape[1] - 1, ids.shape[1] - 1)
    return float(logp[pos, alvo[pos]].sum().exp())

def comparar_prazos(contexto=None, titulo="Sem contexto"):
    prazos = [5, 7, 10, 12, 15, 20, 30, 45, 60, 90]
    p = np.array([prob_continuacao(PREFIXO, f" {d} dias", contexto=contexto) for d in prazos])
    p = p / p.sum()   # normaliza entre os candidatos
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.bar([f"{d} dias" for d in prazos], p, color="#0A84FF")
    ax.set_ylabel("probabilidade relativa"); ax.set_title(titulo)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    plt.xticks(rotation=0, fontsize=9); plt.tight_layout(); plt.show()
    return dict(zip(prazos, p.round(3)))

comparar_prazos(titulo="Que prazo o modelo 'acha' provável, sem nenhum dado?")
''')
md("""
O modelo espalha a probabilidade por vários prazos **plausíveis**. Nenhum deles vem de um sistema; todos vêm do padrão de textos que ele leu no treino. É isso que significa "alucinação": uma continuação provável, não um fato consultado.
""")

md("""
---
## 4 · A resposta sendo montada, token por token

Agora o modelo gera sozinho a partir do prefixo, sempre pegando o token mais provável (modo "guloso", temperatura zero). A tabela mostra cada escolha e a confiança dela.
""")
code('''
@torch.no_grad()
def passo_a_passo(prefixo=PREFIXO, passos=10):
    ids = ids_do_prompt(mensagens(PERGUNTA), prefixo)
    linhas, texto = [], prefixo
    for _ in range(passos):
        probs = torch.softmax(modelo(ids).logits[0, -1], dim=-1)
        top = torch.topk(probs, 3)
        escolhido = int(top.indices[0])
        if escolhido == tok.eos_token_id:
            break
        pedaco = tok.decode([escolhido])
        texto += pedaco
        linhas.append({"token escolhido": repr(pedaco), "prob.": round(float(top.values[0]), 3),
                       "2º lugar": repr(tok.decode([int(top.indices[1])])), "prob. 2º": round(float(top.values[1]), 3)})
        ids = torch.cat([ids, torch.tensor([[escolhido]])], dim=1)
    print(texto)
    return pd.DataFrame(linhas)

passo_a_passo()
''')

md("""
---
## 5 · Temperatura: a mesma pergunta, respostas diferentes

Na prática, os assistentes não pegam sempre o mais provável: eles **sorteiam** entre os mais prováveis. A **temperatura** controla o sorteio. Perto de zero, quase sempre sai o favorito; acima de 1, os azarões ganham chance.
""")
code('''
for temp in (0.1, 0.7, 1.3):
    print(f"\\n— temperatura {temp}")
    for semente in range(4):
        print("  ", textwrap.shorten(responder(PERGUNTA, temperatura=temp, semente=semente, max_novos=30), 110))
''')
md("""
Com temperatura baixa, as respostas se repetem. Com temperatura alta, o prazo "inventado" muda de uma rodada para outra. Mesmo modelo, mesma pergunta. Uma resposta que muda a cada vez que você pergunta não pode ser a fonte de um lead time.
""")

md("""
---
## 6 · Custo e janela de contexto

Tokens são a **unidade de cobrança** (entrada e saída costumam ter preços diferentes) e também o **limite** do que cabe numa conversa, a janela de contexto. Preencha os preços com os do seu fornecedor: os valores abaixo são só exemplos.
""")
code('''
def custo_mensal(perguntas_por_dia, tokens_entrada, tokens_saida,
                 preco_entrada_por_milhao, preco_saida_por_milhao, dias=30):
    entrada = perguntas_por_dia * tokens_entrada * dias
    saida = perguntas_por_dia * tokens_saida * dias
    custo = entrada / 1e6 * preco_entrada_por_milhao + saida / 1e6 * preco_saida_por_milhao
    return {"tokens de entrada/mês": f"{entrada:,.0f}".replace(",", "."),
            "tokens de saída/mês": f"{saida:,.0f}".replace(",", "."),
            "custo/mês": round(custo, 2)}

PAGINA = ("Cláusula 7. A entrega ocorrerá em até 3 dias úteis após o faturamento do pedido, para capitais "
          "e regiões metropolitanas do Sul. Em caso de atraso, incide multa de 2% sobre o valor do pedido. ") * 12
tokens_pagina = len(tok.encode(PAGINA, add_special_tokens=False))
entrada = len(tok.encode(PERGUNTA, add_special_tokens=False))
saida = len(tok.encode(responder(PERGUNTA), add_special_tokens=False))
print(f"pergunta: {entrada} tokens | resposta: {saida} tokens | uma página de contrato: {tokens_pagina} tokens\\n")

# Valores de EXEMPLO. Troque pelos preços reais (na moeda que quiser) do modelo que você usa.
print("Só a pergunta, sem contexto:")
print(custo_mensal(2000, entrada, saida, preco_entrada_por_milhao=1.0, preco_saida_por_milhao=4.0))
print("\\nCom 10 páginas de documentos no prompt (RAG):")
print(custo_mensal(2000, entrada + 10 * tokens_pagina, saida, preco_entrada_por_milhao=1.0, preco_saida_por_milhao=4.0))
''')
md("""
Repare que **colocar contexto no prompt multiplica a entrada**. O RAG do Ep. 1 resolve a alucinação, mas cada trecho recuperado é token pago. Por isso escolher bem o `k` e o tamanho do chunk também é decisão de custo, tema do post "Quanto custa rodar IA".

### Quanto cabe na janela?
""")
code('''
janela = getattr(modelo.config, "max_position_embeddings", None) or tok.model_max_length
print(f"Uma 'página' de contrato (~{len(PAGINA)} caracteres) ≈ {tokens_pagina} tokens neste tokenizador")
print(f"Janela de contexto deste modelo: {janela:,} tokens ≈ {janela // tokens_pagina} páginas".replace(",", "."))
''')
md("""
Caber na janela não significa ser bem usado: com contexto muito longo, os modelos tendem a dar menos atenção ao que está no meio. Esse é o tema do Episódio 4 (Contexto e prompt).
""")

md("""
---
## 7 · Ponte com o Episódio 1: a mesma pergunta, com o dado certo

Agora colocamos no prompt um trecho do cadastro de fornecedores, como faria um RAG. Compare a resposta e o gráfico de prazos com os de antes.
""")
code('''
CADASTRO = ("Cadastro de fornecedores (extraído do ERP):\\n"
            "fornecedor: Alfa; item: 7781; lead time contratado: 12 dias úteis; última revisão: 2026-09-30\\n"
            "fornecedor: Beta; item: 7781; lead time contratado: 20 dias úteis; última revisão: 2026-08-12")

print("Sem contexto →", responder(PERGUNTA))
print("Com contexto →", responder(PERGUNTA, contexto=CADASTRO))
comparar_prazos(contexto=CADASTRO, titulo="Com o cadastro no prompt")
''')
md("""
Com o dado no prompt, a probabilidade se concentra no prazo certo. O modelo continua só completando texto, mas agora a continuação mais provável é a que está escrita no contexto. **É por isso que o RAG existe.**

---
## Resumo

| Ideia | Onde você viu |
|---|---|
| O modelo, sozinho, não consulta nada: ele completa texto | Seções 1 e 3 |
| Texto vira tokens; números e português são picados de formas diferentes | Seção 2 |
| A cada passo, o próximo token é sorteado entre os mais prováveis | Seções 3, 4 e 5 |
| Tokens são a unidade de custo e de limite | Seção 6 |
| Com contexto certo, a continuação provável vira a correta | Seção 7 |

### Exercícios
1. Troque `PERGUNTA` por uma de PCP (por exemplo, "Qual o estoque de segurança do item 7781?") e repita as seções 1, 3 e 7.
2. Em `comparar_prazos`, troque " dias" por " semanas". O que acontece com a distribuição?
3. Na seção 6, coloque os preços reais do modelo que sua empresa usa e o volume de perguntas da sua operação.
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata = {"colab": {"provenance": [], "toc_visible": True},
               "kernelspec": {"name": "python3", "display_name": "Python 3"},
               "language_info": {"name": "python"}}
pathlib.Path(PATH).parent.mkdir(parents=True, exist_ok=True)
nbf.write(nb, PATH)
print("ok", PATH, len(cells), "células")
