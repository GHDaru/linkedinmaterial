# Motion: HTML → GIF e MP4

Transforma uma animação feita em HTML num GIF em loop e num MP4, quadro a quadro. Como cada quadro é calculado por tempo, e não gravado em tempo real, o resultado sai sempre liso, sem quadros perdidos.

## Contrato da página

- Um elemento `#frame` com o tamanho final, por exemplo 1080×960.
- Uma função global `render(t)` que desenha o estado no instante `t`, em segundos.
- O último quadro deve ser igual ao primeiro, para o loop não "pular".

## Uso

```bash
pip install playwright && playwright install chromium   # e ffmpeg instalado
python tools/motion/render.py series/ia-do-basico-ao-avancado/ep01-rag/animacao.html --duracao 16 --saida rag-duas-fases
```

Os arquivos saem na mesma pasta do HTML. Padrões: 30 fps no MP4, 15 fps e 810 px de largura no GIF, que fica com uns 2 MB para 16 s.

## Brief usado nas animações

Peça baseada no modelo "Anatomy of a Claude Motion Prompt": um objeto principal, uma mudança por etapa, física de mola, vidro fosco com sombras em camadas, só azul `#0A84FF` e verde `#30D158`. Sem emoji, sem ícones genéricos e sem fundo escuro.
