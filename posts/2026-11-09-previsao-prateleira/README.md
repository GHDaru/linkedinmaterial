# 40% menos erro no total, 3% perto da prateleira

## No LinkedIn

- Post: https://www.linkedin.com/feed/update/urn:li:share:7525518665274896384/
- No ar: 09/11/2026 (segunda), por volta de 10:50 (horário de Brasília)
- Observação: publicado pelo próprio Gilsiley. Comentário 1 publicado ~20:50 (horário de Brasília); não fixado. Pasta nomeada pela data de publicação (09/11).

**Série relacionada:** TOC Fundamentos · Continua a tese do post [A ruptura não é falta de previsão](../2026-11-06-reposicao-varejo/) (previsão × regra de reposição).

## Texto

```
𝟰𝟬% 𝗠𝗘𝗡𝗢𝗦 𝗘𝗥𝗥𝗢 𝗡𝗢 𝗧𝗢𝗧𝗔𝗟, 𝟯% 𝗣𝗘𝗥𝗧𝗢 𝗗𝗔 𝗣𝗥𝗔𝗧𝗘𝗟𝗘𝗜𝗥𝗔

A previsão do mês bateu no total, e mesmo assim deu ruptura (produto faltando na gôndola) numa loja e sobrou na outra. O M5, competição de previsão com dados do Walmart, ajuda a entender: no total da empresa, o erro médio dos melhores modelos caiu cerca de 40% em relação a um método estatístico de referência; perto da prateleira (produto, produto por estado e produto por loja), só cerca de 3%.

E vem a pergunta da vez: "e se a gente trocar o modelo por IA generativa?"

1. O M5 foi em 2020, antes dos LLMs, os modelos de linguagem como o do ChatGPT. Em 42.840 séries de vendas, venceu o aprendizado de máquina clássico: uma média de modelos LightGBM, que somam milhares de regras simples de decisão. Na média de todos os níveis, o vencedor errou 22,4% menos que o melhor método estatístico de referência.

2. Os 40% e os 3% do início são a média das 50 melhores equipes contra esse método. Perto da prateleira, algumas ficaram até piores que ele.

3. E os LLMs? Um estudo do NeurIPS 2024, uma das maiores conferências de IA, testou três métodos que usam LLM em 13 bases de energia, trânsito, clima, saúde, câmbio e economia, nenhuma de vendas de varejo. Sem o LLM, ou com uma peça simples no lugar, o resultado ficou igual ou melhor na maioria dos casos, com custo muito menor.

4. IA generativa não é só LLM. O Chronos, da Amazon, também é generativo: um modelo de fundação, pré-treinado com muitas séries históricas, e não com texto, para servir de ponto de partida. Sem treino na base da empresa, chega perto de modelos treinados para cada base. O Chronos-2, relatório técnico de out/2025 ainda sem revisão por pares, passou a aceitar variáveis externas, como promoções e feriados.

Minha leitura pela Teoria das Restrições (TOC):

Goldratt propunha perguntar, diante de toda tecnologia nova, que regra precisa mudar para ela dar resultado.

Minha posição: trocar o modelo por IA generativa sem mudar a regra de reposição é investir justamente onde o ganho medido no M5 foi de 3%. As regras que mudam estão no post de sexta (06/11), "A ruptura não é falta de previsão". Os LLMs podem ajudar o planejador a juntar o contexto que a série não mostra, como eventos e atrasos do fornecedor.

Das últimas 5 melhorias de previsão na sua empresa, quantas mudaram alguma política ou regra de reposição?

Fontes no primeiro comentário.

GHDARU · consultoria e implantação de processos agênticos
ghdaru@ghdaru.com.br

#InteligenciaArtificial #SupplyChain #PrevisaoDeDemanda

```

## Comentário 1 (fontes)

```
Fontes e números:
M5 Accuracy competition (Makridakis, Spiliotis e Assimakopoulos, IJF 2022; competição de 2020): 42.840 séries do Walmart; métrica WRMSSE; vencedor 22,4% melhor que o melhor benchmark (suavização exponencial bottom-up), na média de todos os níveis. Média dos 50 melhores: 40% no nível 1 (total), ~23% nos níveis 5–7 e ~3% nos níveis 10–12 (produto, produto-estado e produto-loja), p. 17 do preprint: https://doi.org/10.1016/j.ijforecast.2021.11.013
Versão aberta (preprint): https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf
Tan et al., "Are Language Models Actually Useful for Time Series Forecasting?" (NeurIPS 2024; 13 bases de energia, trânsito, clima, saúde, câmbio e economia): https://arxiv.org/abs/2406.16964
Ansari et al., "Chronos: Learning the Language of Time Series" (Amazon, TMLR 2024; só o histórico): https://arxiv.org/abs/2403.07815
Ansari et al., "Chronos-2: From Univariate to Universal Forecasting" (Amazon, preprint de out/2025, sem revisão por pares; aceita promoções e feriados; caso em varejo): https://arxiv.org/abs/2510.15821
Pergunta de Goldratt: Necessary But Not Sufficient (Goldratt, Schragenheim e Ptak, 2000).

```

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [`texto.txt`](texto.txt) | Texto publicado |
| [`comentario1.txt`](comentario1.txt) | Primeiro comentário (publicado; não fixado) |
| [`imagem.png`](imagem.png) | Arte 1080×1350 (4:5) |
