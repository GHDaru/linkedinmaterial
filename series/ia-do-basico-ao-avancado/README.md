# IA do básico ao avançado

Série de 10 episódios, do conceito mais básico ao mais avançado. Cada episódio explica um conceito com uma animação e um notebook executável, e prepara um ou mais posts avançados.

| # | Episódio | Notebook | Prepara |
|---|---|---|---|
| 1 | [RAG em duas fases](ep01-rag/) | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GHDaru/linkedinmaterial/blob/main/series/ia-do-basico-ao-avancado/ep01-rag/rag_duas_fases.ipynb) | Governança (01/11), "o modelo virou commodity" |
| 2 | [LLM e tokens](ep02-llm-tokens/) | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GHDaru/linkedinmaterial/blob/main/series/ia-do-basico-ao-avancado/ep02-llm-tokens/llm_tokens.ipynb) | Quanto custa rodar IA (28/10), "o modelo virou commodity" |
| 3 | Embeddings e busca semântica | em breve | Grafo de conhecimento |
| 4 | Contexto e prompt | em breve | Os 8 recursos, pauta de conceitos |
| 5 | Ferramentas e MCP | em breve | Agentes no PCP |
| 6 | Agente ou automação | em breve | Agent washing (depois deste episódio), série "Automatize Hoje" |
| 7 | Evals | em breve | Governança, projetos que travam no piloto |
| 8 | Harness | em breve | Livro, governança |
| 9 | Grafo de conhecimento | em breve | Risco de fornecimento, GraphRAG |
| 10 | Modelos de mundo | em breve | Post de 20/10 |

**Extras:** ML clássico versus IA generativa (post avançado de 30/10, previsão de demanda) · custo da IA e cache · guardrails com humano no circuito.

O post de governança, previsto para 01/11, depende dos Eps. 7 e 8. A data está em revisão.

## Padrão de cada episódio

```
epNN-tema/
  README.md              resumo e link do post (modelo em templates/episodio)
  <tema>.ipynb           notebook executável no Colab
  <tema>.gif / .mp4      animação do post
  animacao.html          fonte da animação (renderize com tools/motion)
  _gerar_notebook.py     opcional: script que gera o notebook
```
