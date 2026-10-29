# LinkedIn Material

Materiais de apoio aos posts de **Gilsiley Henrique Darú** no LinkedIn sobre IA aplicada, dados e supply chain: notebooks executáveis, animações e fontes dos posts.

## Séries

| Série | Episódios | Status |
|---|---|---|
| [IA do básico ao avançado](series/ia-do-basico-ao-avancado/) | 10 + extras | Em andamento · Ep. 1 publicado |

## Posts avulsos

Posts que não fazem parte de uma série ficam em [`posts/`](posts/), um por pasta, com o nome `AAAA-MM-DD-tema`.

| Data | Post | Material |
|---|---|---|
| 2026-10-18 | [4 quadrantes TOC](posts/2026-10-18-quadrantes-toc/) | texto + `quadrada.png` |
| 2026-10-20 | [Modelos de mundo](posts/2026-10-20-modelos-de-mundo/) | [post](https://www.linkedin.com/feed/update/urn:li:share:7518312859643187201/) · texto + `imagem.png` |
| 2026-10-21 | [IA Aplicada · 4 casos](posts/2026-10-21-ia-aplicada-4-casos/) | texto + `imagem.png` |
| 2026-10-22 | [8 recursos de IA para SC](posts/2026-10-22-8-recursos-ia-supply-chain/) | [post](https://www.linkedin.com/feed/update/urn:li:share:7518882943445131265/) · texto + `imagem.png` |
| 2026-10-24 | [RAG ep.1](posts/2026-10-24-rag-ep1/) | [post](https://www.linkedin.com/feed/update/urn:li:activity:7519773053938012161/) · texto + `capa.png` · [série](series/ia-do-basico-ao-avancado/ep01-rag/) |
| 2026-10-25 | [Apuração mapa](posts/2026-10-25-apuracao-mapa/) | [post](https://www.linkedin.com/feed/update/urn:li:share:7520242340351864832/) · texto + `arte_linkedin.png` |
| 2026-10-29 | [Modelos de IA: o processo escolhe](posts/2026-10-29-tipos-de-modelos/) | texto + `tipos-de-modelos.mp4` |

Brief de storytelling out/nov: [`posts/plano-storytelling-out-nov-2026/`](posts/plano-storytelling-out-nov-2026/).

## Identidade visual

[GHDARU](identidade/ghdaru/): paleta, tipografia, marca, assinatura gráfica (SVG e PNG), template de arte 1200×1200 e bloco de texto dos posts.

## Estrutura

```
series/<serie>/              uma pasta por série
  README.md                  índice dos episódios
  epNN-tema/                 um episódio: notebook, animação, README
posts/AAAA-MM-DD-tema/       posts avulsos
templates/                   modelos de README para episódio e post
tools/motion/                renderiza animações HTML em GIF e MP4
identidade/ghdaru/           marca, assinatura e template de arte
```

## Como usar os notebooks

Cada notebook tem um botão **Abrir no Colab**. Lá, rode `Ambiente de execução → Executar tudo`. Onde houver geração com o Claude, cadastre `ANTHROPIC_API_KEY` nos *Secrets* do Colab. Sem a chave, os notebooks usam modelos abertos.

## Licença

- Código (notebooks, scripts, HTML): [MIT](LICENSE).
- Conteúdo (textos, GIFs, vídeos, imagens): [CC BY 4.0](LICENSE-CONTENT). Pode reutilizar citando o autor.
