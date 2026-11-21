"""Hafta 1 carousel'leri: A (Fotoğraflar Nerede? #01) ve B (3 Adımda #01). 1080x1350."""
import os
from kit import *

W, H = 1080, 1350
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
os.makedirs(OUT, exist_ok=True)


def save(name, html):
    open(os.path.join(OUT, name + ".html"), "w").write(html)


# ---------------- Carousel A ----------------
A = []

# A1 kapak
inner = head(0, 6) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px">Fotoğraflar nerede? · 01</div>
<h1 style="position:absolute;left:72px;top:210px;width:900px;font-size:128px">Etkinlik bitti.<br>Fotoğraflar<br><span class="hld">kimde?</span></h1>
""" + photo(0, 80, 700, 540, 600, rot=-3, pos="50% 30%") + svg(0, 660, W, 690, f"""
  {phone(650, 50, 320, 580, gallery(684, 140, 252, rows=4, filled=0))}
  <text x="720" y="400" font-family="Hand" font-weight="700" font-size="54" fill="{INK}" transform="rotate(-6 760 400)">boş...</text>
""") + f"""
<div class="sticker" style="right:72px;top:612px;background:{C['white']};transform:rotate(3deg)">Organizatörler için</div>
"""
A.append(page(W, H, C["lime"], inner))

# A2 Gün 1
inner = head(1, 6) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px;background:{C['ink']};color:{C['cream']};padding:8px 16px;border-radius:8px">Gün 1</div>
<h1 style="position:absolute;left:72px;top:230px;width:930px;font-size:96px">Fotoğrafçı 4.000 kare çekti.</h1>
<p class="body" style="position:absolute;left:72px;top:470px;width:820px">Hepsi tek bir harici diskte. Misafirler çoktan evine dönmüş.</p>
""" + svg(0, 640, W, 700, f"""
  {rrect(250, 150, 420, 300, 40, fill=C['peri'], sw=8)}
  <rect x="270" y="330" width="380" height="100" rx="22" fill="url(#dots)" opacity=".3"/>
  <circle cx="610" cy="200" r="14" fill="{C['lime']}" stroke="{INK}" stroke-width="5"/>
  {rrect(290, 210, 290, 70, 14, fill=C['white'], sw=6)}
  <text x="308" y="256" font-family="Mono" font-weight="700" font-size="30" fill="{INK}">ETKİNLİK_SON</text>
  {wob("M460 450 C470 540 300 520 330 600 C350 650 520 610 560 660 C600 710 760 640 820 700", sw=8)}
  {rrect(800, 680, 70, 44, 10, fill=C['orange'], sw=6)}
  {kare(770, 220, .8, mood="worried", arm="hold")}
""")
A.append(page(W, H, C["cream"], inner))

# A3 Gün 9
inner = head(2, 6) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px;background:{C['ink']};color:{C['peri']};padding:8px 16px;border-radius:8px">Gün 9</div>
<h1 style="position:absolute;left:72px;top:230px;width:930px;font-size:96px">Drive linki WhatsApp grubuna düştü.</h1>
""" + svg(0, 560, W, 790, f"""
  {bubble(80, 80, 560, 96, "link: drive.google...", side="left", size=30)}
  {bubble(340, 230, 600, 96, "açılmıyor bende :(", fill=C['lime'], side="right", size=34)}
  {bubble(80, 380, 640, 96, "beni bulan var mı?", side="left", size=34)}
  {bubble(380, 530, 560, 96, "kaç GB bu ya", fill=C['lime'], side="right", size=34)}
  <text x="90" y="740" font-family="Hand" font-weight="700" font-size="58" fill="{INK}" transform="rotate(-3 90 740)">+ 63 okunmamış mesaj</text>
""")
A.append(page(W, H, C["peri"], inner))

# A4 Gün 21
inner = head(3, 6) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px;background:{C['ink']};color:{C['orange']};padding:8px 16px;border-radius:8px">Gün 21</div>
<h1 style="position:absolute;left:72px;top:230px;width:930px;font-size:96px">Misafirlerin çoğu kendini <span class="hl">hiç aramadı.</span></h1>
<p class="body" style="position:absolute;left:72px;top:600px;width:520px">Etkinlik unutuldu. Paylaşılabilecek yüzlerce kare klasörde kaldı.</p>
""" + svg(560, 520, 520, 800, f"""
  {rrect(40, 120, 380, 420, 30, fill=C['white'], sw=8)}
  <rect x="40" y="120" width="380" height="110" rx="30" fill="{INK}"/>
  <rect x="40" y="190" width="380" height="40" fill="{INK}"/>
  {rrect(110, 90, 26, 70, 13, fill=C['cream'], sw=6)}{rrect(324, 90, 26, 70, 13, fill=C['cream'], sw=6)}
  <text x="230" y="460" text-anchor="middle" font-family="Brico" font-weight="800" font-size="220" fill="{INK}">21</text>
  <text x="230" y="205" text-anchor="middle" font-family="Mono" font-weight="700" font-size="36" fill="{C['cream']}">GÜN SONRA</text>
  <rect x="60" y="560" width="340" height="60" rx="14" fill="url(#dots)" opacity=".4"/>
""")
A.append(page(W, H, C["orange"], inner))

# A5 bir de şöyle
inner = head(4, 6, color=C["cream"]) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px;color:{C['lime']}">Bir de şöyle olsaydı</div>
<h1 style="position:absolute;left:72px;top:210px;width:930px;font-size:92px;color:{C['cream']}">Misafir QR'ı okutur, <span class="hl">selfie çeker.</span></h1>
<p class="body" style="position:absolute;left:72px;top:440px;width:880px;color:{C['cream']}">Kendi fotoğrafları etkinlik bitmeden telefonuna düşer. Drive yok, grup yok, arama yok.</p>
""" + photo(1, 72, 700, 500, 600, rot=-3, pos="50% 30%", border=C["lime"]) + svg(0, 600, W, 750, f"""
  {phone(620, 60, 340, 620, gallery(654, 150, 272, rows=4, filled=12, highlight=[1, 4, 9]), fill=C['cream'], sw=7)}
  <text x="640" y="740" font-family="Hand" font-weight="700" font-size="50" fill="{C['lime']}" transform="rotate(-4 640 740)">hepsi onun kareleri</text>
""")
A.append(page(W, H, C["ink"], inner, color=C["cream"]))

# A6 CTA
inner = head(5, 6) + f"""
<h1 style="position:absolute;left:72px;top:200px;width:930px;font-size:132px">Fotoğraflar <span class="hld">sahiplerini</span> bulsun.</h1>
<p class="body" style="position:absolute;left:72px;top:640px;width:480px">İlk etkinliğinde 200 Pix bizden. Kurulum birkaç dakika.</p>
<div class="sticker" style="left:72px;top:820px;background:{C['ink']};color:{C['lime']};font-size:34px;text-transform:none;transform:rotate(-3deg)">pixlomi.com</div>
<p class="tag" style="position:absolute;left:72px;bottom:96px;width:560px;line-height:1.4">Etkinlik planlayan birine gönder ↗</p>
""" + photo(5, 590, 640, 420, 520, rot=4, pos="50% 40%") + svg(330, 880, 270, 270, f"""
  {stamp(135, 135, 110, "QR · SELFIE · HAZIR · ", fill=C['white'], size=26)}
""")
A.append(page(W, H, C["lime"], inner))

for i, h in enumerate(A, 1):
    save(f"A{i}", h)

# ---------------- Carousel B ----------------
B = []
inner = head(0, 5) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px">3 adımda · 01</div>
<h1 style="position:absolute;left:72px;top:210px;width:930px;font-size:124px">Fotoğrafını bulmak <span class="hld">3 adım</span> sürer.</h1>
<p class="en" style="position:absolute;left:72px;top:640px">EN · Your own event photos, in 3 steps.</p>
""" + photo(2, 80, 720, 640, 520, rot=-3, pos="50% 30%") + svg(640, 760, 440, 560, f"""
  {kare(150, 60, .95, mood="happy", arm="point")}
  <g transform="translate(0 0) scale(-1 1) translate(-260 0)"></g>
""") + f"""<div class="sticker" style="left:620px;top:1210px;background:{C['lime']};transform:rotate(-4deg)">madalya + fotoğraf</div>"""
B.append(page(W, H, C["peri"], inner))

steps = [
    ("01", "QR'ı okut.", "Masadaki kartı ya da girişteki afişi telefonunla okut. Uygulama indirmen gerekmiyor.",
     "Scan the QR at the venue. No app to download.", C["cream"], "qr"),
    ("02", "Selfie çek.", "Yapay zekâ seni binlerce karenin içinde bulur. Yüz verin yalnızca o etkinlikte kullanılır.",
     "Take a selfie. We find you among thousands of photos.", C["lime"], "selfie"),
    ("03", "Fotoğrafların telefonunda.", "Fotoğrafçı çektikçe yeni kareler düşer. Orijinal çözünürlükte indir, paylaş.",
     "New shots land on your phone as they're taken.", C["orange"], "gallery"),
]
for k, (num, title, body, en, bg, ill) in enumerate(steps, 1):
    ph = ""
    if ill == "qr":
        ph = photo(4, 110, 790, 400, 420, rot=-3, pos="50% 35%")
        art = f"""{phone(640, 80, 300, 560, f'<rect x="668" y="190" width="244" height="244" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="26 190" stroke-dashoffset="13"/>{qr(700, 222, 180, seed=9)}', sw=7)}
              {wob("M560 330 Q600 300 630 330", sw=7)}
              <text x="600" y="620" font-family="Hand" font-weight="700" font-size="50" fill="{INK}" transform="rotate(-4 600 620)">uygulama yok</text>"""
    elif ill == "qr_old":
        art = f"""<g transform="translate(150 70)">{rrect(0, 0, 330, 440, 26, fill=C['white'], sw=8)}
              <text x="165" y="70" text-anchor="middle" font-family="Mono" font-weight="700" font-size="30" fill="{INK}">FOTOĞRAFLARIN</text>
              <text x="165" y="108" text-anchor="middle" font-family="Mono" font-weight="700" font-size="30" fill="{INK}">BURADA</text>
              {qr(55, 140, 220, seed=9)}</g>
              {phone(600, 150, 260, 470, f'<rect x="628" y="220" width="204" height="204" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="26 150" stroke-dashoffset="13"/>{qr(660, 252, 140, seed=9)}', sw=7)}
              {wob("M500 300 Q550 270 590 300", sw=7)}"""
    elif ill == "selfie":
        art = f"""{phone(140, 60, 300, 540, f'<circle cx="290" cy="300" r="96" fill="{C["peri"]}" stroke="{INK}" stroke-width="6"/><circle cx="262" cy="290" r="9" fill="{INK}"/><circle cx="318" cy="290" r="9" fill="{INK}"/>' + wob("M262 330 Q290 352 318 330", sw=6) + f'<rect x="200" y="200" width="180" height="200" rx="20" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="30 110" stroke-dashoffset="15"/><circle cx="290" cy="530" r="30" fill="{C["lime"]}" stroke="{INK}" stroke-width="6"/>', sw=7)}
              {gallery(560, 120, 360, cols=4, rows=4, filled=16, gap=12, highlight=[2, 7, 13])}
              <text x="560" y="600" font-family="Hand" font-weight="700" font-size="52" fill="{INK}" transform="rotate(-4 560 600)">işte sen!</text>"""
    else:
        ph = photo(3, 110, 790, 400, 420, rot=-3, pos="50% 25%")
        art = f"""{wifi(560, 330, 1.0)}
              {phone(600, 40, 300, 560, gallery(632, 120, 236, rows=4, filled=10, highlight=[9]), sw=7)}
              <text x="600" y="660" font-family="Hand" font-weight="700" font-size="46" fill="{INK}" transform="rotate(-3 600 660)">yeni kare düştü</text>"""
    inner = head(k, 5) + f"""
<div style="position:absolute;left:72px;top:140px;width:936px;display:flex;flex-direction:column;gap:22px">
<div style="font-weight:800;font-size:150px;line-height:1;letter-spacing:-6px">{num}</div>
<h1 style="font-size:100px">{title}</h1>
<p class="body" style="width:880px">{body}</p></div>
<p class="en" style="position:absolute;left:72px;bottom:30px;width:900px">EN · {en}</p>
""" + ph + svg(150, 790, 780, 505, art, vb="0 0 1080 700")
    B.append(page(W, H, bg, inner))

inner = head(4, 5, color=C["cream"]) + f"""
<div class="tag" style="position:absolute;left:72px;top:150px;color:{C['lime']}">Organizatörsen</div>
<h1 style="position:absolute;left:72px;top:210px;width:930px;font-size:96px;color:{C['cream']}">QR kodun, fotoğrafçı linkin ve raporların <span class="hl">tek panelde.</span></h1>
<p class="body" style="position:absolute;left:72px;top:600px;width:600px;color:{C['cream']}">İlk etkinliğin için 200 Pix hediye. Abonelik yok.</p>
<div class="sticker" style="left:72px;top:780px;background:{C['lime']};color:{C['ink']};font-size:34px;text-transform:none;transform:rotate(-3deg)">pixlomi.com</div>
<p class="en" style="position:absolute;left:72px;bottom:72px;width:900px;color:{C['cream']}">EN · Organizers: one panel for QR codes, photographer links and reports. Your first event is on us.</p>
""" + svg(600, 680, 480, 560, f"""
  {stamp(260, 200, 170, "KVKK UYUMLU · 8 DİL · ABONELİK YOK · ", fill=C['lime'], size=26)}
""")
B.append(page(W, H, C["ink"], inner, color=C["cream"]))

for i, h in enumerate(B, 1):
    save(f"B{i}", h)
print("ok", len(A), len(B))
