"""Renderiza uma animação HTML em GIF e MP4, quadro a quadro.

A página precisa ter:
  - um elemento #frame com o tamanho final do vídeo (ex.: 1080x960);
  - uma função global render(t) que desenha o estado no instante t (segundos).

Uso:
  python tools/motion/render.py caminho/animacao.html --duracao 16 --saida nome
Requisitos: pip install playwright && playwright install chromium; ffmpeg no PATH.
"""
import argparse, asyncio, pathlib, shutil, subprocess, tempfile
from playwright.async_api import async_playwright


async def capturar(html, pasta, duracao, fps, largura, altura):
    async with async_playwright() as p:
        nav = await p.chromium.launch()
        pg = await nav.new_page(viewport={"width": largura, "height": altura})
        await pg.goto(pathlib.Path(html).resolve().as_uri())
        await pg.wait_for_timeout(800)  # fontes e layout
        quadro = pg.locator("#frame")
        for i in range(int(duracao * fps)):
            await pg.evaluate(f"render({i / fps})")
            await quadro.screenshot(path=str(pasta / f"{i:05d}.png"))
        await nav.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--duracao", type=float, required=True, help="segundos do loop")
    ap.add_argument("--saida", default="animacao", help="nome base dos arquivos")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--gif-fps", type=int, default=15)
    ap.add_argument("--gif-largura", type=int, default=810)
    ap.add_argument("--largura", type=int, default=1080)
    ap.add_argument("--altura", type=int, default=960)
    a = ap.parse_args()

    destino = pathlib.Path(a.html).resolve().parent
    pasta = pathlib.Path(tempfile.mkdtemp())
    try:
        asyncio.run(capturar(a.html, pasta, a.duracao, a.fps, a.largura, a.altura))
        entrada = ["-framerate", str(a.fps), "-i", str(pasta / "%05d.png")]
        mp4, gif = destino / f"{a.saida}.mp4", destino / f"{a.saida}.gif"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entrada, "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", str(mp4)], check=True)
        filtro = (f"fps={a.gif_fps},scale={a.gif_largura}:-1:flags=lanczos,split[a][b];"
                  "[a]palettegen=max_colors=192:stats_mode=diff[p];"
                  "[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *entrada, "-vf", filtro,
                        "-loop", "0", str(gif)], check=True)
        print(f"{mp4} ({mp4.stat().st_size/1e6:.1f} MB)\n{gif} ({gif.stat().st_size/1e6:.1f} MB)")
    finally:
        shutil.rmtree(pasta, ignore_errors=True)


if __name__ == "__main__":
    main()
