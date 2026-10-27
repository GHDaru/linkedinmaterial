"""Exporta o elemento #arte de um HTML para PNG no tamanho exato (1200x1200 por padrão).

Uso: python identidade/ghdaru/template/exportar.py entrada.html saida.png [--escala 1]
Requisitos: pip install playwright && playwright install chromium (e a fonte Poppins, ou internet para o Google Fonts).
"""
import argparse, asyncio, pathlib
from playwright.async_api import async_playwright

async def exportar(html, png, escala):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1300, "height": 1300}, device_scale_factor=escala)
        await pg.goto(pathlib.Path(html).resolve().as_uri())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.locator("#arte").screenshot(path=png)
        await b.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html"); ap.add_argument("png")
    ap.add_argument("--escala", type=float, default=1)
    a = ap.parse_args()
    asyncio.run(exportar(a.html, a.png, a.escala))
    print("ok", a.png)
