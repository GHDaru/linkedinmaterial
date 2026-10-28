# Tipos de modelos de linguagem

**Status:** rascunho para 29/10/2026, fora da grade do orquestrador. Encaixe a definir com o Darú.
**Material:** `tipos-de-modelos.mp4` (1080×1350, 28 s) · `tipos-de-modelos.gif` (720 px) · fonte em `animacao.html` · orientações em [`orientacoes.md`](orientacoes.md)

## Texto do post

Vi esta imagem com os 5 tipos de modelos de linguagem e ela é um bom começo. Mas tem uma armadilha: dá a impressão de que você escolhe um dos cinco. Não escolhe.

Os cinco, em uma linha cada:

• LLM: prevê o próximo token. É a base do GPT, do Claude e do Gemini.
• SLM: versão compacta, de 1 a 10 bilhões de parâmetros, que roda no notebook, no celular ou no coletor do armazém. Rápida, barata e sem mandar dado para fora.
• VLM: lê imagem e texto juntos. A foto do palete com a pergunta "quantas caixas?" vira resposta.
• MoE: o modelo tem muitos especialistas, e cada token usa só alguns. O DeepSeek-V3 tem 671 bilhões de parâmetros e ativa 37 bilhões por token.
• LRM: pensa passo a passo antes de responder. Demora mais e acerta mais em cálculo e lógica.

Onde a imagem engana: as cinco categorias respondem a perguntas diferentes. Tamanho (LLM ou SLM). O que entra (texto ou imagem). Arquitetura (densa ou MoE). Como responde (direto ou raciocinando). O DeepSeek-R1 é LLM, MoE e modelo de raciocínio ao mesmo tempo. E hoje o raciocínio costuma ser um modo do mesmo modelo, não outro modelo.

E o que ficou de fora:

• Difusão: em vez de escrever da esquerda para a direita, parte de um rascunho mascarado e refina todos os tokens em paralelo. Mercury (Inception Labs) e Gemini Diffusion (Google) geram muito mais rápido, mas ainda perdem em raciocínio difícil.
• Híbridos com Mamba ou atenção linear (Nemotron, Qwen3-Next): trocam parte da atenção por camadas mais baratas, para aguentar textos longos.
• VLA, visão, linguagem e ação: o modelo vê, entende a instrução e move o robô (Gemini Robotics, π0).
• Embeddings: não geram texto, transformam texto em vetor. São a base da busca no RAG.

Para quem opera supply chain, a pergunta útil não é "qual o melhor modelo". É "qual é a restrição do processo".

Latência no coletor pede um modelo pequeno. Nota fiscal e foto de avaria pedem visão. Cálculo de reposição pede raciocínio, e de preferência uma ferramenta que faz a conta. Volume alto com resposta simples pede o mais barato que acerta.

Escolha o modelo pela restrição, não pelo ranking.

Qual destes você já usa sem saber que usa?

Imagem de referência: Jean Lee.

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
