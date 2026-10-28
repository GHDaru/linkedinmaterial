"""Gera a assinatura gráfica GHDARU (SVG com texto em contornos + PNG).

Uso (da raiz do repositório):
    python identidade/ghdaru/_gerar.py
Requisitos: pip install fonttools playwright && playwright install chromium; fonte Poppins
(Google Fonts, licença OFL) em /usr/share/fonts/truetype/google-fonts ou na pasta indicada por POPPINS_DIR.
"""
import asyncio, os, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

AQUI = pathlib.Path(__file__).resolve().parent
SAIDA = AQUI / "assinatura"
FONTES = pathlib.Path(os.environ.get("POPPINS_DIR", "/usr/share/fonts/truetype/google-fonts"))

NAVY, CARTAO, LARANJA, BRANCO = "#0B1F3A", "#123D63", "#FF9F43", "#FFFFFF"
LARANJA_ESCURO = "#B35A00"  # laranja para fundo claro (contraste AA)
NOME, LINHA, EMAIL = "GHDARU", "consultoria e implantação de processos agênticos", "ghdaru@ghdaru.com.br"

_cache = {}
def fonte(peso):
    if peso not in _cache:
        f = TTFont(FONTES / f"Poppins-{peso}.ttf")
        _cache[peso] = (f, f.getBestCmap(), f.getGlyphSet(), f["hmtx"], f["head"].unitsPerEm)
    return _cache[peso]

def largura(texto, peso, tam, track=0.0):
    f, cmap, gs, hmtx, upm = fonte(peso)
    w = sum(hmtx[cmap[ord(c)]][0] for c in texto) * tam / upm
    return w + track * tam * (len(texto) - 1)

def texto_em_contorno(texto, peso, tam, x, y, cor, track=0.0):
    """Devolve um <path> com o texto desenhado a partir da linha de base (x, y)."""
    f, cmap, gs, hmtx, upm = fonte(peso)
    esc = tam / upm
    pen = SVGPathPen(gs)
    cx = x
    for c in texto:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(pen, (esc, 0, 0, -esc, cx, y)))
        cx += hmtx[g][0] * esc + track * tam
    return f'<path fill="{cor}" d="{pen.getCommands()}"/>'

def marca(x, y, s, cor_bloco, cor_restricao=LARANJA):
    """Marca: três etapas de um fluxo. A do meio, laranja, é a mais estreita: a restrição (o gargalo)."""
    lado_w, lado_h = s * 0.30, s * 0.86
    meio_w, meio_h = s * 0.18, s * 0.40
    gap = s * 0.06
    xs = [x, x + lado_w + gap, x + lado_w + gap + meio_w + gap]
    ws, hs = [lado_w, meio_w, lado_w], [lado_h, meio_h, lado_h]
    cores = [cor_bloco, cor_restricao, cor_bloco]
    partes = []
    for xi, wi, hi, ci in zip(xs, ws, hs, cores):
        yi = y + (s - hi) / 2
        partes.append(f'<rect x="{xi:.2f}" y="{yi:.2f}" width="{wi:.2f}" height="{hi:.2f}" rx="{wi/2:.2f}" fill="{ci}"/>')
    return "".join(partes), xs[-1] + ws[-1] - x

def svg(w, h, corpo, fundo=None, rotulo=None):
    bg = f'<rect width="{w}" height="{h}" fill="{fundo}"/>' if fundo else ""
    rotulo = rotulo or f"{NOME} · {LINHA} · {EMAIL}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{rotulo}">{bg}{corpo}</svg>\n')

VARIANTES = {  # nome: (fundo, texto principal, texto secundário, blocos da marca, e-mail/restrição)
    "navy": (NAVY, BRANCO, "#C9D4E3", "#2F6FA6", LARANJA),
    "escuro-transparente": (None, BRANCO, "#C9D4E3", "#2F6FA6", LARANJA),
    "claro": (None, NAVY, "#3C4E66", CARTAO, LARANJA_ESCURO),
}

def horizontal(v):
    """Rodapé para artes de 1200 px de largura: duas linhas, texto >= 28 px (legível no celular)."""
    fundo, c1, c2, cb, ce = VARIANTES[v]
    W, H = 1200, 120
    m, mw = marca(48, 16, 52, cb, ce)
    x = 48 + mw + 20
    corpo = m + texto_em_contorno(NOME, "Bold", 40, x, 56, c1, track=0.06)
    ew = largura(EMAIL, "Medium", 28)
    corpo += texto_em_contorno(EMAIL, "Medium", 28, W - 48 - ew, 54, ce)
    corpo += texto_em_contorno(LINHA, "Regular", 28, 48, 102, c2)
    return svg(W, H, corpo, fundo)

def compacta(v):
    """Bloco para o canto inferior de uma arte 1200x1200: três linhas, texto >= 28 px."""
    fundo, c1, c2, cb, ce = VARIANTES[v]
    pad = 32
    lw = largura(LINHA, "Regular", 28)
    W, H = int(pad * 2 + lw + 2), 196
    m, mw = marca(pad, 26, 56, cb, ce)
    corpo = m + texto_em_contorno(NOME, "Bold", 44, pad + mw + 18, 70, c1, track=0.06)
    corpo += texto_em_contorno(LINHA, "Regular", 28, pad, 128, c2)
    corpo += texto_em_contorno(EMAIL, "Medium", 28, pad, 170, ce)
    return svg(W, H, corpo, fundo)

AUTOR = "Gilsiley H. Darú"
# O template usa peso 600; sem Poppins SemiBold instalada o navegador cai no Bold, que é o que o PNG exportado mostra.
PESO_AUTOR = "SemiBold" if (FONTES / "Poppins-SemiBold.ttf").exists() else "Bold"

def autor_e_email(x_dir, y, c1, c2, ce):
    """'Gilsiley H. Darú · e-mail' alinhado à direita em x_dir, linha de base y (igual ao template)."""
    wa, wp, we, gap = largura(AUTOR, PESO_AUTOR, 30), largura("·", "Regular", 28), largura(EMAIL, "Medium", 28), 14
    x = x_dir - (wa + gap + wp + gap + we)
    corpo = texto_em_contorno(AUTOR, PESO_AUTOR, 30, x, y, c1)
    corpo += texto_em_contorno("·", "Regular", 28, x + wa + gap, y, c2)
    corpo += texto_em_contorno(EMAIL, "Medium", 28, x + wa + gap + wp + gap, y, ce)
    return corpo

def horizontal_nome(v):
    """Rodapé 1200 px com o nome (decisão de 27/10): marca + GHDARU à esquerda, autor · e-mail à direita, linha embaixo."""
    fundo, c1, c2, cb, ce = VARIANTES[v]
    W, H = 1200, 120
    m, mw = marca(48, 16, 52, cb, ce)
    corpo = m + texto_em_contorno(NOME, "Bold", 40, 48 + mw + 20, 56, c1, track=0.06)
    corpo += autor_e_email(W - 48, 54, c1, c2, ce)
    corpo += texto_em_contorno(LINHA, "Regular", 28, 48, 102, c2)
    return svg(W, H, corpo, fundo, rotulo=f"{NOME} · {AUTOR} · {EMAIL} · {LINHA}")

def compacta_nome(v):
    """Canto inferior de arte 1200x1200 com o nome: quatro linhas, texto >= 28 px."""
    fundo, c1, c2, cb, ce = VARIANTES[v]
    pad = 32
    W, H = int(pad * 2 + largura(LINHA, "Regular", 28) + 2), 240
    m, mw = marca(pad, 26, 56, cb, ce)
    corpo = m + texto_em_contorno(NOME, "Bold", 44, pad + mw + 18, 70, c1, track=0.06)
    corpo += texto_em_contorno(AUTOR, PESO_AUTOR, 30, pad, 128, c1)
    corpo += texto_em_contorno(LINHA, "Regular", 28, pad, 172, c2)
    corpo += texto_em_contorno(EMAIL, "Medium", 28, pad, 214, ce)
    return svg(W, H, corpo, fundo, rotulo=f"{NOME} · {AUTOR} · {LINHA} · {EMAIL}")

def so_marca(fundo):
    m, _ = marca(64, 64, 384, "#2F6FA6")
    return svg(512, 512, m, fundo)

async def png(arquivos):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(device_scale_factor=2)
        for f in arquivos:
            await pg.goto(f.as_uri())
            el = pg.locator("svg")
            await el.screenshot(path=str(f.with_suffix(".png")), omit_background=True)
        await b.close()

def main():
    SAIDA.mkdir(exist_ok=True)
    feitos = []
    for v in VARIANTES:
        for nome, fn in (("horizontal", horizontal), ("compacta", compacta),
                         ("horizontal-nome", horizontal_nome), ("compacta-nome", compacta_nome)):
            f = SAIDA / f"ghdaru-{nome}-{v}.svg"
            f.write_text(fn(v), encoding="utf-8"); feitos.append(f)
    for nome, fundo in (("marca-navy", NAVY), ("marca-transparente", None)):
        f = SAIDA / f"ghdaru-{nome}.svg"; f.write_text(so_marca(fundo), encoding="utf-8"); feitos.append(f)
    asyncio.run(png(feitos))
    for f in feitos:
        print(f.relative_to(AQUI), "+ .png")

if __name__ == "__main__":
    main()
