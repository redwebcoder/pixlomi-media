import sys, os, asyncio
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))


async def main(names, w, h, outdir):
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": w, "height": h})
        for n in names:
            await pg.goto("file://" + os.path.join(HERE, "html", n + ".html"))
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(150)
            await pg.locator(".page").screenshot(path=os.path.join(outdir, n + ".png"))
        await b.close()

if __name__ == "__main__":
    w, h = int(sys.argv[1]), int(sys.argv[2])
    asyncio.run(main(sys.argv[4:], w, h, sys.argv[3]))
