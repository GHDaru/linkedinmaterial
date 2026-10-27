# Identidade visual GHDARU

**GHDARU** · consultoria e implantação de processos agênticos · ghdaru@ghdaru.com.br

Guia breve para artes, capas e rodapés dos posts no LinkedIn. A identidade segue as artes já publicadas (navy, acento laranja, tipografia geométrica). Ela não cria um visual novo: dá nome e assinatura ao que já existe.

![Exemplo de arte 1200×1200](template/exemplo-arte-1200.png)

## 1. A marca

![Marca](assinatura/ghdaru-marca-navy.png)

Três etapas de um fluxo. A do meio, laranja e mais estreita, é a **restrição**: o gargalo que define o resultado do sistema inteiro. É a tese das artes ("quem dita o resultado é o gargalo", post de 20/10) desenhada como símbolo. Em tamanho pequeno, as três barras também lembram um "H".

| Arquivo | Uso |
|---|---|
| `assinatura/ghdaru-marca-navy.svg` / `.png` | Avatar, favicon, selo em fundo navy |
| `assinatura/ghdaru-marca-transparente.svg` / `.png` | Selo sobre fundo escuro já existente |

## 2. Assinatura gráfica

| Arquivo | Tamanho | Onde usar |
|---|---|---|
| `assinatura/ghdaru-horizontal-navy` | 1200 × 120 | Rodapé de arte 1200 px, com fundo navy próprio |
| `assinatura/ghdaru-horizontal-escuro-transparente` | 1200 × 120 | Rodapé sobre o navy da própria arte |
| `assinatura/ghdaru-horizontal-claro` | 1200 × 120 | Rodapé sobre fundo branco ou claro (slides, documentos) |
| `assinatura/ghdaru-compacta-navy` | ~780 × 196 | Canto inferior de arte 1200 × 1200 |
| `assinatura/ghdaru-compacta-escuro-transparente` | ~780 × 196 | Canto inferior sobre navy ou cartão |
| `assinatura/ghdaru-compacta-claro` | ~780 × 196 | Canto inferior sobre fundo claro |

Cada variante existe em **SVG** (texto convertido em contornos, então abre igual em qualquer máquina) e em **PNG** com o dobro da resolução e fundo transparente quando o nome diz `transparente` ou `claro`.

**Regras**
- **Tamanho:** use os arquivos no tamanho nativo numa arte de 1200 px. Não reduza. A arte aparece com ~1/3 do tamanho no feed do celular, e 28 px na arte viram ~9 px na tela, que é o mínimo legível.
- **Respiro:** deixe livre em volta da assinatura pelo menos a largura da marca.
- **Não fazer:** trocar as cores da marca, esticar, rotacionar, aplicar sombra, ou pôr a versão escura sobre fundo claro (e o contrário).

Para gerar de novo: `python identidade/ghdaru/_gerar.py`.

## 3. Paleta

As cores foram **extraídas dos pixels** das artes publicadas (18/10 a 25/10), não estimadas.

| Nome | Hex | Uso |
|---|---|---|
| Navy | `#0B1F3A` | Fundo das artes |
| Cartão | `#123D63` | Cartões e blocos sobre o navy |
| Laranja | `#FF9F43` | Acento: destaque no título, "Minha leitura:", restrição, e-mail |
| Branco | `#FFFFFF` | Texto principal sobre navy |
| Texto secundário | `#C9D4E3` | Subtítulos, linha da assinatura, fontes |
| Azul da marca | `#2F6FA6` | As duas etapas laterais da marca |
| Laranja escuro | `#B35A00` | Laranja **só para fundo claro** |

**Contraste medido (WCAG):**

| Par | Contraste |
|---|---|
| Branco sobre navy | 16,5 : 1 |
| Laranja sobre navy | 8,1 : 1 |
| Laranja sobre cartão | 5,5 : 1 |
| Secundário sobre navy | 11,0 : 1 |
| Laranja escuro sobre branco | 4,8 : 1 |

O laranja `#FF9F43` sobre branco dá só 2,0 : 1 e não deve ser usado. Em fundo claro, use o laranja escuro.

## 4. Tipografia

**Poppins** (Google Fonts, licença OFL), a mesma das artes publicadas.

| Papel | Peso | Tamanho na arte 1200 |
|---|---|---|
| Rótulo (eyebrow) | 700, caixa alta, espaçamento 0,14 em | 30 px |
| Título | 800 | 72–80 px |
| Título do cartão | 600 | 40 px |
| Texto | 500 | 34–36 px |
| Nota, fonte, assinatura | 400–500 | **28 px no mínimo** |
| Nome GHDARU | 700, espaçamento 0,06 em | 40–44 px |

## 5. GHDARU e Gilsiley Darú

Proposta, a confirmar pelo Darú:

- **Gilsiley Darú** é o **autor**. Ele assina as ideias: o perfil, a voz do texto e o "Minha leitura" das artes.
- **GHDARU** é a **marca da consultoria**. Ela aparece como assinatura: no fechamento do texto do post e no rodapé da arte.
- Na arte, a assinatura GHDARU **substitui** o "Gilsiley Darú" que hoje fica no rodapé. A linha de fonte (por exemplo, "Definição: Google DeepMind") continua acima da assinatura.
- Escreva sempre **GHDARU**, em caixa alta e numa palavra só. Não use "GH Daru", "Ghdaru" nem "GHDaru" na arte (GHDaru com minúsculas é o usuário do GitHub, não a marca).

## 6. Tom e voz

A marca entra na voz que os posts já têm. Ela não muda essa voz.

- **A ordem da tese:** primeiro a restrição, depois a regra, só então a ferramenta, e o resultado medido em throughput. A IA aparece como meio para elevar uma restrição, nunca como fim.
- **Sem hype:** nada de "revolucionário", "disruptivo" ou "o futuro chegou". Números vêm com a fonte ou marcados como ilustrativos.
- **Concreto, de operação:** pedido, lead time, CD, SKU, gargalo. A cena vem antes do termo técnico.
- **Ressalva honesta:** quando um número é do fornecedor ou é ilustrativo, a arte diz.
- **"Processos agênticos"** quer dizer agentes que executam etapas de um processo dentro de regras e com um humano no circuito. A marca vende implantação com governança, não autonomia sem controle.

## 7. Template de arte

`template/arte-1200.html` é uma arte 1200 × 1200 com rótulo, título, cartões, "Minha leitura", linha de fonte e o rodapé GHDARU. Edite só os blocos marcados com `EDITAR` e exporte:

```bash
python identidade/ghdaru/template/exportar.py identidade/ghdaru/template/arte-1200.html saida.png
```

O resultado é um PNG de exatamente 1200 × 1200. O exemplo exportado está em `template/exemplo-arte-1200.png`, com texto ilustrativo.

## 8. Bloco de texto do post

Está em [`assinatura-texto.md`](assinatura-texto.md). Ele vai antes das hashtags.

---

*O que fica de fora de propósito:* CNPJ, telefone e site. Só o e-mail `ghdaru@ghdaru.com.br` foi informado.
