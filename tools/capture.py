import sys, os, json, asyncio, subprocess
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 30


async def cap(name, dur, outdir):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + os.path.join(HERE, "html", name + ".html"))
        await pg.evaluate("document.fonts.ready")
        out = os.path.join(outdir, name + "_silent.mp4")
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
                               "-an", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        n = int(dur * FPS)
        for i in range(n):
            await pg.evaluate(f"window.render({i / FPS})")
            buf = await pg.screenshot(type="jpeg", quality=93)
            ff.stdin.write(buf)
        ff.stdin.close(); ff.wait()
        # kapak karesi
        await b.close()
    return out


async def main(names, outdir):
    meta = json.load(open(os.path.join(HERE, "html", "videos.json")))
    os.makedirs(outdir, exist_ok=True)
    await asyncio.gather(*[cap(n, meta[n]["dur"], outdir) for n in names])

if __name__ == "__main__":
    asyncio.run(main(sys.argv[2:], sys.argv[1]))
