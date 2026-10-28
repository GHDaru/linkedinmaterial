# Tipos de modelos de linguagem

**Status:** rascunho para 29/10/2026, fora da grade do orquestrador. Encaixe a definir com o Darú.
**Material:** `tipos-de-modelos.mp4` (1080×1350, 32 s) · `tipos-de-modelos.gif` (720 px) · fonte em `animacao.html` · orientações em [`orientacoes.md`](orientacoes.md)

## Texto do post

Numa doca de recebimento, três modelos de IA diferentes podem trabalhar no mesmo fluxo:

• um modelo de visão lê a nota e a etiqueta e cruza com o pedido de compra;
• um modelo pequeno no coletor faz a mesma checagem sem internet;
• um modelo barato classifica as ocorrências que o motorista escreve.

Cada um foi escolhido por uma restrição diferente: ler imagem, funcionar sem rede, custar pouco em volume alto. Para fazer essa escolha, vale conhecer as siglas que aparecem em toda proposta de IA:

• LLM (Large Language Model): modelo grande, treinado em texto em escala da web. A maioria gera a resposta prevendo o próximo token (pedaço de palavra). É a base do GPT, do Claude e do Gemini.
• SLM (Small Language Model): versão compacta, de centenas de milhões a cerca de 10 bilhões de parâmetros (o tamanho do modelo; quanto maior, mais caro de rodar). Os menores rodam no celular ou no coletor.
• VLM (Vision Language Model): lê imagem e texto juntos. A foto da etiqueta e a nota viram dados conferíveis.
• MoE (Mixture of Experts): modelo grande que custa como médio, porque cada token usa só alguns "especialistas". O DeepSeek-V3 tem 671 bilhões de parâmetros e ativa 37 bilhões por token. Economiza cálculo, não memória.
• LRM (Large Reasoning Model): treinado para pensar passo a passo antes de responder. Vale quando o problema tem várias regras. Conta simples, o sistema já faz.

As siglas não são excludentes: cada uma responde a uma pergunta diferente (tamanho, o que entra, arquitetura, como responde). O DeepSeek-R1 é LLM, MoE e de raciocínio ao mesmo tempo.

E há outros que valem acompanhar. O mais importante é a difusão (dLLM): em vez de escrever da esquerda para a direita, refina vários tokens por passo. Mercury (Inception Labs) e Gemini Diffusion (Google) geram muito mais rápido, mas ainda perdem em raciocínio difícil. Para a operação, hoje quase nunca são a primeira escolha.

Voltando à doca: ninguém escolheu "o melhor modelo". Cada etapa tem uma restrição, e a restrição escolheu o modelo.

Escolha o modelo pela restrição, não pelo ranking.

Qual processo seu travaria primeiro se a IA errasse?

Inspirado no infográfico "Top 5 Types of Language Models", de Jean Lee.

GHDARU · processos agênticos · ghdaru@ghdaru.com.br

#IA #SupplyChain #TeoriaDasRestrições

## Primeiro comentário

Material do post (animação e fonte) no repositório: https://github.com/GHDaru/linkedinmaterial/tree/main/posts/2026-10-29-tipos-de-modelos

## Referências

- Imagem "Top 5 Types of Language Models", de Jean Lee (crédito obrigatório se for usada).
- Difusão: [Inception Labs, Mercury](https://inceptionlabs.ai/news) · [Mercury e Gemini Diffusion, comparação de velocidade](https://tech-insider.org/?p=21391)
- Híbridos: [Sebastian Raschka, galeria de arquiteturas com atenção híbrida](https://sebastianraschka.com/llm-architecture-gallery/hybrid-attention/)
- VLA: [Google DeepMind, Gemini Robotics](https://deepmind.google/models/gemini-robotics/) · [Gemini Robotics, artigo](https://arxiv.org/abs/2503.20020v1)
- DeepSeek-V3: 671 bi de parâmetros, 37 bi ativos por token (relatório técnico do DeepSeek-V3, dez/2024).
