# IA do básico ao avançado

Série de 10 episódios, do conceito mais básico ao mais avançado. Cada episódio explica um conceito com uma animação e um notebook executável, e prepara um ou mais posts avançados.

| # | Episódio | Notebook | Prepara |
|---|---|---|---|
| 1 | [RAG em duas fases](ep01-rag/) | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GHDaru/linkedinmaterial/blob/main/series/ia-do-basico-ao-avancado/ep01-rag/rag_duas_fases.ipynb) | Governança (01/11), "o modelo virou commodity" |
| 2 | LLM e tokens | em breve | Custo de rodar IA |
| 3 | Embeddings e busca semântica | em breve | Grafo de conhecimento |
| 4 | Contexto e prompt | em breve | Os 8 recursos, pauta de conceitos |
| 5 | Ferramentas e MCP | em breve | Agentes no PCP |
| 6 | Agente ou automação | em breve | Agent washing, série "Automatize Hoje" |
| 7 | Harness | em breve | Livro, governança (01/11) |
| 8 | Evals | em breve | Governança (01/11), projetos que travam no piloto |
| 9 | Grafo de conhecimento | em breve | Risco de fornecimento, GraphRAG |
| 10 | Modelos de mundo | em breve | Post de 20/10 |

**Reservas para episódios extras:** custo da IA e cache · guardrails com humano no circuito · ML clássico versus IA generativa.

## Padrão de cada episódio

```
epNN-tema/
  README.md              resumo e link do post (modelo em templates/episodio)
  <tema>.ipynb           notebook executável no Colab
  <tema>.gif / .mp4      animação do post
  animacao.html          fonte da animação (renderize com tools/motion)
  _gerar_notebook.py     opcional: script que gera o notebook
```
