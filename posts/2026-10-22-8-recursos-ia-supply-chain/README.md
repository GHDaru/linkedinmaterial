# 8 recursos de IA para supply chain e PCP

**Publicado em:** 2026-10-22 · [link do post](https://www.linkedin.com/feed/update/urn:li:share:7518882943445131265/)

**Série relacionada:** nenhum episódio específico; alimenta o vocabulário da série [IA do básico ao avançado](../../series/ia-do-basico-ao-avancado/).

## Texto

```
𝗔 𝗺𝗮𝗶𝗼𝗿𝗶𝗮 𝗱𝗮𝘀 𝗹𝗶𝘀𝘁𝗮𝘀 𝗱𝗲 𝗜𝗔 𝗻ã𝗼 𝘁𝗲𝗺 𝘀𝘂𝗽𝗽𝗹𝘆 𝗰𝗵𝗮𝗶𝗻.

Esta tem: previsão, sequenciamento, documento de fornecedor e teste antes de mexer no plano.
4 para aprender, 4 para construir. 7 dos 8 são gratuitos ou open source.

𝗣𝗮𝗿𝘁𝗲 𝟭: 𝗮𝗽𝗿𝗲𝗻𝗱𝗲𝗿

1. Forecasting: Principles and Practice, versão Python (Hyndman et al.)
↳ Livro online gratuito de previsão de demanda: baseline, sazonalidade, intervalos e como medir erro antes de chamar qualquer modelo de IA.

2. AI Engineering (Chip Huyen)
↳ Como levar um modelo pronto a sistema confiável: avaliação, RAG, agentes e custo de inferência. Livro pago; materiais no GitHub.

3. Hugging Face AI Agents Course
↳ Curso gratuito de agentes com ferramentas (smolagents, LangGraph, LlamaIndex), para prototipar um assistente que consulta carteira, estoque e capacidade.

4. Engenharia de Harness (meu livro, gratuito)
↳ O que fica em volta do modelo: ferramentas, permissões, memória e verificação. É o que separa a demo do agente que pode sugerir a liberação de uma ordem.

𝗣𝗮𝗿𝘁𝗲 𝟮: 𝗰𝗼𝗻𝘀𝘁𝗿𝘂𝗶𝗿

5. StatsForecast (Nixtla)
↳ ETS, ARIMA, Croston e outros modelos estatísticos rodando em milhares de SKUs. O baseline que qualquer modelo de IA precisa vencer.

6. Google OR-Tools
↳ CP-SAT, roteirização e programação inteira para sequenciar ordens com capacidade, setup e janela de entrega reais.

7. Docling
↳ Converte PDF, planilhas e e-mails (EML, MSG) em dados estruturados, com tabelas, para levar pedidos e contratos de fornecedores a um RAG ou agente.

8. promptfoo
↳ Testa prompts, agentes e RAG com seus próprios casos e faz red team, para provar que o assistente de PCP não piorou a cada mudança.

Minha leitura (Teoria das Restrições): a ordem certa é identificar a restrição, explorá-la com o que já existe e só então comprar ferramenta. Um agente que acelera um recurso que não é a restrição só aumenta o estoque em processo. Por isso a lista começa em previsão e sequenciamento, não em agentes.

Qual destes você já levou para produção no planejamento, e onde travou: nos dados, no solver ou na aprovação do planejador?

Links no primeiro comentário, com o livro de harness para leitura online. No segundo, 4 que quase entraram e 1 que ficou de fora.

#IAAplicada #SupplyChain #PCP #TOC
```

Arquivo-fonte: [`texto.txt`](texto.txt).

## Comentários publicados

### Comentário 1 (links dos 8 recursos)

```
Links dos 8 recursos:

Parte 1: aprender
1. Forecasting: Principles and Practice, versão Python (gratuito): https://otexts.com/fpppy/
2. AI Engineering (Chip Huyen; livro pago, materiais gratuitos no GitHub): https://github.com/chiphuyen/aie-book
3. Hugging Face AI Agents Course (gratuito): https://huggingface.co/learn/agents-course
4. Engenharia de Harness (meu livro, gratuito, leitura online): https://harness.ghdaru.com.br/?utm_source=linkedin&utm_medium=comentario&utm_campaign=post_20261022_8recursos

Parte 2: construir
5. StatsForecast (Nixtla, Apache-2.0): https://github.com/Nixtla/statsforecast
6. Google OR-Tools (Apache-2.0): https://developers.google.com/optimization
7. Docling (MIT): https://github.com/docling-project/docling
8. promptfoo (hoje parte da OpenAI, segue open source e MIT): https://github.com/promptfoo/promptfoo

```

### Comentário 2 (quase entraram)

```
Outros 4 que quase entraram:
- LangGraph: orquestração de agentes com estado e pausa para aprovação humana (o curso da Hugging Face já apresenta). https://github.com/langchain-ai/langgraph
- Hands-On Large Language Models: código aberto do livro de Alammar e Grootendorst sobre LLMs, embeddings e busca semântica. https://github.com/HandsOnLLM/Hands-On-Large-Language-Models
- HiGHS: solver open source de programação linear e inteira (MIP). https://highs.dev
- MCP Python SDK: para expor ERP, WMS ou planilhas como ferramentas para agentes. https://github.com/modelcontextprotocol/python-sdk

Ficou de fora: Microsoft GraphRAG, que o próprio README declara em grande parte em modo de manutenção (sem novas funcionalidades).

```

## Materiais

| Arquivo | O que é |
|---|---|
| [`imagem.png`](imagem.png) | Imagem final do post (1080×1350, 4:5) |
| [`texto.txt`](texto.txt) | Texto publicado |
| [`comentario.txt`](comentario.txt) | Comentário 1 com links |
| [`comentario2.txt`](comentario2.txt) | Comentário 2 (quase entraram) |

## Referências

HYNDMAN, Rob J. et al. *Forecasting: Principles and Practice, the Pythonic Way*. Disponível em: https://otexts.com/fpppy/. Acesso em: 22 out. 2026.

HUYEN, Chip. *AI Engineering*. O'Reilly, 2025. Materiais: https://github.com/chiphuyen/aie-book.

HUGGING FACE. AI Agents Course. Disponível em: https://huggingface.co/learn/agents-course. Acesso em: 22 out. 2026.

DARÚ, Gilsiley Henrique. *Engenharia de Harness*. Disponível em: https://harness.ghdaru.com.br. Acesso em: 22 out. 2026.

NIXTLA. StatsForecast. Disponível em: https://github.com/Nixtla/statsforecast. Acesso em: 22 out. 2026.

GOOGLE. OR-Tools. Disponível em: https://developers.google.com/optimization. Acesso em: 22 out. 2026.

DOCLING. Docling. Disponível em: https://github.com/docling-project/docling. Acesso em: 22 out. 2026.

PROMPTFOO. promptfoo. Disponível em: https://github.com/promptfoo/promptfoo. Acesso em: 22 out. 2026.
