# RAG: como a IA responde usando os seus documentos (Ep. 1)

**Publicado em:** 2026-10-24 · [link do post](https://www.linkedin.com/feed/update/urn:li:activity:7519773053938012161/)

**Série relacionada:** Episódio 1 de [IA do básico ao avançado](../../series/ia-do-basico-ao-avancado/ep01-rag/) — notebook, animação GIF/MP4 e fontes da animação ficam na pasta da série; aqui só o texto e a capa do post.

## Texto

```
𝗥𝗔𝗚: 𝗖𝗢𝗠𝗢 𝗔 𝗜𝗔 𝗥𝗘𝗦𝗣𝗢𝗡𝗗𝗘 𝗨𝗦𝗔𝗡𝗗𝗢 𝗢𝗦 𝗦𝗘𝗨𝗦 𝗗𝗢𝗖𝗨𝗠𝗘𝗡𝗧𝗢𝗦

Você pergunta ao assistente de IA qual é o prazo de entrega do pedido 4521. Ele responde na hora, cita a cláusula do contrato e parece seguro. Só que o contrato venceu no mês passado.

O problema não está no modelo, e trocar de LLM não resolve. O modelo não conhece os seus pedidos: ele responde com o que encontra nos seus documentos. Isso tem nome: RAG.

RAG (Retrieval-Augmented Generation) busca os trechos certos nos documentos da empresa e os entrega, junto com a pergunta, ao modelo: o LLM, a IA que escreve a resposta. Ele não é retreinado nem 'aprende' seus documentos: o conhecimento que ganhou no treinamento continua o mesmo. O que muda é o que ele lê antes de responder, como um analista que consulta o contrato antes de atender o cliente.

Na animação, a pergunta do 4521 passa por duas fases:

1. Preparação (antes da pergunta). Contrato e SLA viram trechos curtos, como fichas de arquivo. Cada um ganha uma etiqueta numérica do seu significado (embedding): trechos parecidos ficam perto.

2. Busca e resposta (na hora). O sistema separa os poucos trechos mais parecidos com a pergunta, pelo sentido, pela palavra exata ou pelos dois: cláusula 7, saída do CD em 24 h e status do 4521. O modelo os recebe com a ordem "responda só com base neles, cite a fonte e diga quando não souber".

Ressalva: status muda toda hora e, na prática, vem de consulta direta ao ERP, não da busca (tema do episódio 5). Números ilustrativos.

𝗤𝘂𝗮𝗻𝗱𝗼 𝘂𝘀𝗮𝗿
Texto que muda pouco: contratos, SLAs, políticas de devolução, procedimentos de CD, normas fiscais.

𝗤𝘂𝗮𝗻𝗱𝗼 𝗻𝗮𝗼 𝘂𝘀𝗮𝗿
- Dado vivo (estoque, posição do caminhão): consulta direta ao ERP ou ao TMS.
- Cálculo: "some as multas do trimestre" pede consulta ao banco de dados.
- Formato fixo de resposta: aí é fine-tuning (ajustar o próprio modelo).

𝗢𝗻𝗱𝗲 𝗳𝗮𝗹𝗵𝗮
- Busca ruim, resposta ruim. Cláusula cortada no meio perde a condição.
- Documento vencido gera resposta errada com fonte citada, que parece confiável. Foi o caso do 4521.
- Sem controle de acesso, o assistente mostra contrato a quem não devia ver.

𝗠𝗶𝗻𝗵𝗮 𝗹𝗲𝗶𝘁𝘂𝗿𝗮
Pela Teoria das Restrições, a restrição de um projeto de RAG raramente é o modelo. É a governança dos documentos: quem é dono de cada política, quem atualiza quando a regra muda, quem tira o contrato vencido da base. Se ninguém é dono da cláusula 7, o assistente vai citar a versão errada com toda a confiança.

Na sua empresa, quem deveria ser o dono desses documentos: TI ou a área de negócio? Se a resposta honesta for 'ninguém', a restrição está aí.

Este é o episódio 1 da série IA do básico ao avançado: um conceito por semana, aplicado a supply chain. Notebook do exemplo no primeiro comentário.

Próximo: LLM e tokens, ou por que o assistente inventa um lead time quando não acha a resposta.

#RAG #SupplyChain #TOC

```

Arquivo-fonte: [`texto.txt`](texto.txt).

## Comentários publicados

### Comentário 1 (Colab)

```
Notebook do Colab para rodar o exemplo, com os mesmos documentos e a mesma pergunta da animação (roda sem instalar nada): https://colab.research.google.com/github/GHDaru/linkedinmaterial/blob/main/series/ia-do-basico-ao-avancado/ep01-rag/rag_duas_fases.ipynb

No notebook, o status do pedido entra no índice só para simplificar; em produção ele viria do ERP.

Minha resposta: a área de negócio é dona da regra, e a TI cuida da base. E na sua empresa?

```

### Comentário 2 (Harness)

```
Quem quiser ir além do RAG e entender como se monta o ambiente em volta do modelo (ferramentas, contexto, verificação e limites), deixei gratuito o livro Engenharia de Harness: https://harness.ghdaru.com.br

```

## Materiais

| Arquivo | O que é |
|---|---|
| [`capa.png`](capa.png) | Capa / frame do post (1080×960) |
| [`texto.txt`](texto.txt) | Texto publicado |
| [`comentario1.txt`](comentario1.txt) | Comentário com link do Colab |
| [`comentario2.txt`](comentario2.txt) | Comentário com link do livro Harness |

Materiais da série (não duplicados aqui): [`series/ia-do-basico-ao-avancado/ep01-rag/`](../../series/ia-do-basico-ao-avancado/ep01-rag/).

## Referências

Conceito de RAG (Retrieval-Augmented Generation) aplicado a documentos operacionais de supply chain. Ver notebook e animação no episódio da série.
