"""Sıklaştırma paketi: tekli gönderiler (S1-S4), kısa Reels (V3-V6, TR/EN), hikâye kareleri (ST4-ST13)."""
import os, json, base64
from kit import *
from videos import JS_BASE, CSS as VCSS, vlogo

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "html")

SINGLES = {
    "S1": dict(bg=C["sage"], tag="Fotoğrafçılar için", photo=3, pos="50% 25%",
               title='Çektiğin kare, <span class="hld">saniyesinde</span> galeride.',
               body="PixlomiUp makineden Wi-Fi ile yükler. \"Fotoğraflar ne zaman?\" sorusu biter.",
               en=dict(tag="For photographers", title='Your shot, in the gallery <span class="hld">in seconds.</span>',
                       body="PixlomiUp uploads straight from the camera over Wi-Fi. No more \"when do we get the photos?\"")),
    "S2": dict(bg=C["lime"], tag="Koşucular için", photo=2, pos="50% 30%",
               title='Madalyayı al, <span class="hld">fotoğrafını</span> telefondan al.',
               body="Bitişteki QR'ı okut, selfie çek. Yarış fotoğrafların sana gelir.",
               en=dict(tag="For runners", title='Grab your medal, <span class="hld">get your photos</span> on your phone.',
                       body="Scan the QR at the finish, take a selfie. Your race photos come to you.")),
    "S3": dict(bg=C["cream"], tag="Merak edilen", photo=4, pos="50% 35%",
               title='Yüz verin <span class="hl">sadece o etkinlikte</span> kullanılır.',
               body="Açık onayla alınır, şifreli saklanır, başka hiçbir yerde kullanılmaz. KVKK uyumlu.",
               en=dict(tag="Good to know", title='Your face data is used <span class="hl">for that event only.</span>',
                       body="Collected with explicit consent, stored encrypted, never used anywhere else.")),
    "S4": dict(bg=C["ink"], tag="Organizatörlere", photo=5, pos="50% 40%", dark=True,
               title='İlk etkinliğin <span class="hl">bizden.</span>',
               body="Hesap aç, 200 Pix hediye. QR'ını oluştur, fotoğrafçına linki gönder, gerisi kendiliğinden.",
               en=dict(tag="For organizers", title='Your first event <span class="hl">is on us.</span>',
                       body="Sign up and get 200 Pix. Create your QR, send the link to your photographer, done.")),
}


def single(key):
    s = SINGLES[key]
    dark = s.get("dark")
    ink = C["cream"] if dark else C["ink"]
    inner = head(0, 1, color=(C["cream"] if dark else None)).replace('<div class="prog"><b class="on"></b></div>', '') + f"""
<div class="tag" style="position:absolute;left:72px;top:160px;color:{C['lime'] if dark else C['ink']}">{s['tag']}</div>
<h1 style="position:absolute;left:72px;top:215px;width:936px;font-size:104px;color:{ink}">{s['title']}</h1>
""" + photo(s["photo"], 72, 660, 560, 620, rot=-3, pos=s["pos"], border=(C["lime"] if dark else C["ink"])) + f"""
<p class="body" style="position:absolute;left:670px;top:700px;width:340px;font-size:32px;color:{ink}">{s['body']}</p>
<div class="sticker" style="left:670px;top:1150px;background:{C['ink'] if not dark else C['lime']};color:{C['lime'] if not dark else C['ink']};font-size:34px;transform:rotate(-3deg)">pixlomi.com</div>
"""
    return page(1080, 1350, s["bg"], inner, color=ink)


def short_reel(key, lang):
    s = SINGLES[key]
    t = s if lang == "tr" else dict(s, **s["en"])
    dark = s.get("dark")
    ink = C["cream"] if dark else C["ink"]
    end = 'Fotoğraflar <span class="hld">sahiplerini</span> bulsun.' if lang == "tr" else 'Every photo finds <span class="hld">its owner.</span>'
    html = f"""
<div class="sc" id="S1" style="background:{s['bg']};color:{ink}">{vlogo(bool(dark))}
  <div class="tag" style="position:absolute;left:80px;top:270px;color:{C['lime'] if dark else C['ink']}">{t['tag']}</div>
  <div id="h1" class="big pop" style="top:330px;font-size:124px;color:{ink}">{t['title']}</div>
  <div id="ph" class="pop" style="position:absolute;left:0;top:0;width:1080px;height:1920px">{photo(s['photo'], 150, 860, 780, 820, rot=-3, pos=s['pos'], border=(C['lime'] if dark else C['ink']))}</div>
  <div id="bd" class="pop sticker" style="left:110px;top:1600px;width:860px;background:{C['white']};color:{C['ink']};font-size:36px;font-weight:600;line-height:1.3;transform:rotate(1.5deg);z-index:5">{t['body']}</div>
</div>
<div class="sc" id="S2" style="background:{C['lime']}">{vlogo()}
  <div id="e1" class="big pop" style="top:420px;font-size:150px">{end}</div>
  <div id="e2" class="pop sticker" style="left:80px;top:1000px;background:{C['ink']};color:{C['lime']};font-size:60px;transform:rotate(-3deg)">pixlomi.com</div>
  <div id="e3" class="pop" style="position:absolute;left:0;top:1150px">{svg(0, 0, 1080, 600, stamp(800, 260, 170, "QR · SELFIE · HAZIR · " if lang == "tr" else "SCAN · SELFIE · DONE · ", fill=C['white'], size=34))}</div>
</div>"""
    js = """
<script>
window.render=function(t){
 scene('S1',t,0,6.2);scene('S2',t,6.2,99);
 pop('h1',t,.15,.45);pop('ph',t,1.2,.45,120);pop('bd',t,3.0,.4,60);
 pop('e1',t,6.3,.45);pop('e2',t,6.9,.35);pop('e3',t,7.2,.4,80);
};
</script>"""
    ev = [(0.15, "pop"), (1.2, "pop"), (1.25, "shutter"), (3.0, "msg"), (6.0, "whoosh"), (6.3, "chime"), (6.9, "pop"), (7.2, "pop")]
    return page(1080, 1920, s["bg"], html, extra_css=VCSS).replace("</body>", JS_BASE + js + "</body>"), 9.0, ev


def img64(path, mime="image/png"):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


STORIES = [
    # (anahtar, tür, zemin, başlık, alt yazı, küçük resim)
    ("ST4", "new", C["ink"], "Yeni Reels", "Aile grubunda 847 fotoğraf. Sen 2 tanesindesin.", "thumb_R1.png"),
    ("ST5", "ask", C["lime"], "Bu hafta sonu hangi etkinlikteydin?", "Yanıtla, fotoğraflarına ne kadar sürede ulaştığını da yaz.", None),
    ("ST6", "new", C["cream"], "Yeni gönderi", "Etkinlik bitti. Fotoğraflar kimde?", "A1.png"),
    ("ST7", "tip", C["sage"], "Bilmeyen kalmasın", "Fotoğrafını bulmak için uygulama indirmen gerekmiyor. QR'ı okut, selfie çek, yeter.", None),
    ("ST8", "new", C["lime"], "Yeni Reels", "Fotoğrafçılar için: çektiğin kare, saniyesinde galeride.", "thumb_V3.png"),
    ("ST9", "ask", C["ink"], "Etkinlikten sonraki gün en çok neyle uğraşıyorsun?", "Organizatörlere soruyoruz. Yanıtla, bir sonraki Organizatör Notu'nu ona göre hazırlayalım.", None),
    ("ST10", "new", C["cream"], "Yeni gönderi", "Fotoğrafını bulmak 3 adım sürer.", "B1.png"),
    ("ST11", "new", C["ink"], "Yeni Reels", "QR'ı okut, selfie çek, fotoğrafların telefonunda.", "thumb_R2.png"),
    ("ST12", "tip", C["lime"], "Merak edilen", "Yüz verin sadece o etkinlikte kullanılır. Açık onayla alınır, şifreli saklanır.", None),
    ("ST13", "new", C["sage"], "Yeni gönderi", "Madalyayı al, fotoğrafını telefondan al.", "S2.png"),
]


def story(k, kind, bg, title, sub, thumb):
    dark = bg == C["ink"]
    ink = C["cream"] if dark else C["ink"]
    logo = f'<img src="{LOGO_LIME if dark else LOGO_DARK}" style="position:absolute;left:80px;top:130px;height:84px">'
    if kind == "new":
        im = img64(os.path.join(HERE, "out/png", thumb))
        is_video = thumb.startswith("thumb_")
        w, h = (560, 996) if is_video else (640, 800)
        body = f"""
<div class="tag" style="position:absolute;left:80px;top:300px;color:{C['lime'] if dark else C['ink']}">{title}</div>
<h1 style="position:absolute;left:80px;top:360px;width:920px;font-size:84px;color:{ink}">{sub}</h1>
<img src="{im}" style="position:absolute;left:{(1080-w)//2}px;top:680px;width:{w}px;height:{h}px;object-fit:cover;border:7px solid {C['lime'] if dark else C['ink']};border-radius:30px;transform:rotate(-3deg)">
<div class="sticker" style="left:600px;top:1600px;background:{C['lime'] if not dark else C['cream']};color:{C['ink']};font-size:40px;transform:rotate(4deg)">profilde ↗</div>"""
    elif kind == "ask":
        body = f"""
<div class="tag" style="position:absolute;left:80px;top:300px;color:{C['lime'] if dark else C['ink']}">Soru</div>
<h1 style="position:absolute;left:80px;top:360px;width:920px;font-size:112px;color:{ink}">{title}</h1>
<p class="body" style="position:absolute;left:80px;top:1000px;width:880px;font-size:42px;color:{ink}">{sub}</p>
<div class="sticker" style="left:80px;top:1300px;width:920px;height:150px;background:{C['white']};color:#8a8a8a;font-size:40px;font-weight:500;display:flex;align-items:center">Bu hikâyeyi yanıtla ↓</div>
"""
    else:
        body = f"""
<div class="tag" style="position:absolute;left:80px;top:300px;color:{C['lime'] if dark else C['ink']}">{title}</div>
<h1 style="position:absolute;left:80px;top:360px;width:920px;font-size:96px;color:{ink}">{sub}</h1>
""" + svg(0, 1180, 1080, 600, kare(560, 60, 1.2, mood="wow", arm="point"))
    return page(1080, 1920, bg, logo + body, color=ink)


if __name__ == "__main__":
    meta = {}
    for k in SINGLES:
        open(os.path.join(OUT, f"{k}.html"), "w").write(single(k))
        for lang in ("tr", "en"):
            html, dur, ev = short_reel(k, lang)
            v = {"S1": "V3", "S2": "V4", "S3": "V5", "S4": "V6"}[k]
            open(os.path.join(OUT, f"{v}_{lang}.html"), "w").write(html)
            meta[f"{v}_{lang}"] = dict(dur=dur, events=ev)
    m = json.load(open(os.path.join(OUT, "videos.json")))
    m.update(meta)
    json.dump(m, open(os.path.join(OUT, "videos.json"), "w"))
    print("ok", list(meta))
