# Modelos de IA: o processo escolhe

**Mídia:** `tipos-de-modelos.mp4` (1080×1350, 35 s) · `tipos-de-modelos.gif` (720 px) · fonte da animação em `animacao.html`

## Texto do post

𝗠𝗢𝗗𝗘𝗟𝗢𝗦 𝗗𝗘 𝗜𝗔: 𝗢 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗢 𝗘𝗦𝗖𝗢𝗟𝗛𝗘
Numa doca, três modelos de IA trabalham juntos. Nenhum é "o melhor".

No mesmo recebimento:

• um modelo de visão lê a etiqueta rasgada, sem código legível, e a foto da avaria, e cruza com o pedido de compra;
• uma versão pequena desse modelo roda no próprio coletor e faz a checagem sem internet;
• um modelo barato classifica as ocorrências que o motorista escreve.

Cada um foi escolhido pela restrição de uma etapa: ler imagem, funcionar sem rede, custar pouco em volume alto. Para fazer essa escolha, vale conhecer as siglas que aparecem em toda proposta de IA:

• LLM (Large Language Model): modelo grande, treinado com uma quantidade enorme de texto da internet. A maioria gera a resposta prevendo o próximo token (pedaço de palavra). É a base do GPT, do Claude e do Gemini.
• SLM (Small Language Model): versão compacta, em geral de centenas de milhões a cerca de 10 bilhões de parâmetros (não há fronteira oficial; parâmetros são o tamanho do modelo: quanto maior, mais caro de rodar). Os menores rodam no celular ou no coletor.
• VLM (Vision Language Model): lê imagem e texto juntos. A foto da etiqueta e da avaria vira dado conferível.
• MoE (Mixture of Experts): modelo grande dividido em blocos ("especialistas"); um roteador escolhe poucos blocos para cada token. O DeepSeek-V3 tem 671 bilhões de parâmetros e usa 37 bilhões por token. Calcula como médio, mas precisa de memória de grande.
• LRM (Large Reasoning Model): treinado para raciocinar passo a passo antes de responder; hoje costuma ser um modo do mesmo modelo. Vale quando há várias regras ao mesmo tempo, como alocar docas com janelas, prioridades e tipos de veículo. Para uma conta simples, o WMS ou o TMS já resolve.

As siglas não são excludentes: cada uma responde a uma pergunta diferente (tamanho, o que entra, como é construído por dentro, como raciocina). O DeepSeek-R1 é LLM, MoE e de raciocínio ao mesmo tempo. O modelo pequeno de visão do coletor é SLM e VLM.

Fora da lista, vale acompanhar os modelos de difusão: em vez de escrever palavra por palavra, refinam um rascunho inteiro. Detalhes no primeiro comentário.

Voltando à doca: ninguém escolheu "o melhor modelo". Cada etapa tem uma condição que não pode falhar, e é ela que escolhe o modelo. Se a doca é o gargalo do CD, o modelo que importa é o que não para a doca quando cai o sinal.

Escolha o modelo pela restrição, não pelo ranking.

Na sua operação, o que escolheria o modelo primeiro: custo em volume alto ou funcionar sem rede?

Inspirado no infográfico "Top 5 Types of Language Models", de Jean Lee.

GHDARU · consultoria e implantação de processos agênticos
ghdaru@ghdaru.com.br

#InteligenciaArtificial #SupplyChain #TeoriaDasRestricoes

## Primeiro comentário

Bônus, modelos de difusão (dLLM): em vez de gerar um token por vez, refinam vários tokens por passo, partindo de um rascunho mascarado. Mercury (Inception Labs) e Gemini Diffusion (Google) são várias vezes mais rápidos, segundo dados dos fabricantes, mas ainda ficam atrás em raciocínio difícil.

Material do post (animação e fonte): https://github.com/GHDaru/linkedinmaterial/tree/main/posts/2026-10-29-tipos-de-modelos

## Referências

- Infográfico "Top 5 Types of Language Models", de Jean Lee (inspiração; crédito no post).
- DeepSeek-V3: 671 bi de parâmetros, 37 bi ativos por token (relatório técnico do DeepSeek-V3, dez/2024).
- Difusão: [Inception Labs, Mercury](https://inceptionlabs.ai/news) · [Mercury e Gemini Diffusion](https://tech-insider.org/?p=21391)
