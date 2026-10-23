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
| | *nenhum ainda* | |

## Estrutura

```
series/<serie>/              uma pasta por série
  README.md                  índice dos episódios
  epNN-tema/                 um episódio: notebook, animação, README
posts/AAAA-MM-DD-tema/       posts avulsos
templates/                   modelos de README para episódio e post
tools/motion/                renderiza animações HTML em GIF e MP4
```

## Como usar os notebooks

Cada notebook tem um botão **Abrir no Colab**. Lá, rode `Ambiente de execução → Executar tudo`. Onde houver geração com o Claude, cadastre `ANTHROPIC_API_KEY` nos *Secrets* do Colab. Sem a chave, os notebooks usam modelos abertos.

## Licença

- Código (notebooks, scripts, HTML): [MIT](LICENSE).
- Conteúdo (textos, GIFs, vídeos, imagens): [CC BY 4.0](LICENSE-CONTENT). Pode reutilizar citando o autor.
