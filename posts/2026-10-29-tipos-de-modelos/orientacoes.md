# Orientações do post · Tipos de modelos de linguagem

## Objetivo

Pegar uma imagem que circula bastante e acrescentar o que ela não diz: as categorias se sobrepõem, faltam tipos importantes, e a escolha do modelo depende da restrição do processo. A voz é a de sempre: IA e supply chain pela TOC (restrição, regra, modelo, resultado).

## Formato

| Item | Orientação |
|---|---|
| Mídia | **A animação em MP4** (`tipos-de-modelos.mp4`, 1080×1350, 28 s, em português). O LinkedIn aceita um tipo de mídia por post, então escolha entre a animação e a imagem original. |
| Imagem da Jean Lee | Só com crédito no texto ("Imagem de referência: Jean Lee"), e de preferência repostando o post original dela. A animação é material próprio e evita o problema. |
| Se a animação não servir | Gerar uma arte 1200×1200 no template da GHDARU com o título "Não são 5 caixas. São eixos." e a tabela dos eixos (última cena da animação). |
| Tamanho do texto | Cerca de 2.300 caracteres. As 2–3 primeiras linhas são o gancho: precisam funcionar antes do "ver mais". |
| Link | No primeiro comentário, não no corpo do post. |
| Hashtags | 3, no fim. |

## Estrutura do texto

1. **Gancho:** "a imagem é um bom começo, mas tem uma armadilha".
2. **Os cinco em uma linha cada**, com um exemplo de operação quando couber (coletor do armazém, foto do palete).
3. **A crítica:** são eixos, não caixas. Um exemplo concreto (DeepSeek-R1).
4. **O que ficou de fora:** difusão primeiro (é o mais visual e o mais novo), depois híbridos, VLA e embeddings.
5. **A virada TOC:** escolher o modelo pela restrição do processo, com quatro casos de supply chain.
6. **Pergunta para comentários.**

## A crítica da imagem

O que está certo: as cinco definições estão corretas no essencial e os desenhos ajudam a entender.

O que precisa de ressalva:

1. **As categorias não são do mesmo tipo.** LLM e SLM falam de tamanho, VLM de modalidade, MoE de arquitetura e LRM de comportamento na inferência. Um modelo pode ser tudo isso: o Qwen3-235B-A22B é grande, MoE e tem modo de raciocínio; o DeepSeek-R1 é MoE e de raciocínio.
2. **O desenho do MoE simplifica demais.** O roteamento não acontece uma vez depois do tokenizador: acontece **a cada camada, para cada token**. "2 de 8 especialistas" é o Mixtral 8x7B. O DeepSeek-V3, citado logo abaixo, tem 256 especialistas roteados mais 1 compartilhado e ativa 8 por token. E os "especialistas" não são especialistas em assuntos; a divisão é aprendida e pouco interpretável.
3. **Raciocínio virou modo, não família.** Claude, Gemini, Qwen3 e o GPT-5 têm modo de pensar dentro do mesmo modelo. O3 e R1 já foram substituídos como exemplos de ponta. E a cadeia de pensamento exibida nem sempre é fiel ao que o modelo de fato fez.
4. **SLM: as três técnicas fazem coisas diferentes.** Destilação treina um modelo menor com o maior. Poda remove pesos ou camadas. Quantização **não reduz o número de parâmetros**: guarda cada um com menos bits (16 para 4, por exemplo). O limite de "1 a 10 bilhões" é convenção, não regra.
5. **LLM: prever o próximo token é só o pré-treino.** O que transforma o modelo em assistente é o pós-treino (ajuste por instrução e por reforço).
6. **VLM: hoje o padrão é multimodal nativo**, com áudio e vídeo na entrada, e às vezes imagem e fala na saída (modelos "omni").
7. **Os exemplos envelhecem rápido.** Vale tratar os nomes como ilustração.

## O que ficou de fora

| Tipo | Eixo | O que é | Exemplos |
|---|---|---|---|
| **Difusão (dLLM)** | como gera | Parte de uma sequência mascarada e refina todos os tokens em poucas passadas paralelas. Muito mais rápido; ainda atrás em raciocínio difícil. | Mercury (Inception Labs), Gemini Diffusion (Google), LLaDA |
| **Híbridos SSM / atenção linear** | arquitetura | Trocam parte das camadas de atenção por camadas recorrentes (Mamba, Gated DeltaNet), mais baratas em contexto longo. | Nemotron-H e Nemotron 3 (NVIDIA), Qwen3-Next, Jamba |
| **VLA** | saída | Visão e linguagem que viram **ação motora** de robô. | Gemini Robotics, π0 (Physical Intelligence) |
| **Embeddings** | saída | Não gera texto: converte texto em vetor para busca e classificação. Base do RAG. | modelos de embedding da OpenAI, Gemini, BGE, E5 |
| **Omni** | entrada e saída | Áudio, vídeo e fala nativos, nos dois sentidos. | GPT-4o, Qwen-Omni |
| **Modelos de mundo** | outro objetivo | Preveem o próximo estado do ambiente, não o próximo token. | ver post de 20/10 |

Para o post, difusão é o principal (foi o exemplo do Darú e é o mais fácil de mostrar). Os outros entram em uma linha cada; omni e modelos de mundo ficam fora do texto para não alongar.

## Encaixe na grade

- **Data:** a grade do orquestrador tem posts a cada 2 dias (28/10 custo, 30/10 previsão). 29/10 cai fora da cadência. O Darú decide se entra como extra (como o de 21/10) ou se troca com outro.
- **Ligação com a série:** prepara o Ep.3 (embeddings) e o Ep.5 (ferramentas). Também apoia o post de custo: SLM, MoE e difusão são alavancas de custo.
- **Não publicar sem OK do Darú.**

## Checagem antes de publicar

- [ ] Números do DeepSeek-V3 (671 bi total, 37 bi ativos) conferidos no relatório técnico
- [ ] Nomes dos modelos de difusão e de VLA conferidos nas fontes do README
- [ ] Crédito à Jean Lee, se a imagem dela for usada
- [ ] Assinatura de texto da GHDARU conforme `identidade/ghdaru/assinatura-texto.md`
- [ ] Link do repositório no primeiro comentário
