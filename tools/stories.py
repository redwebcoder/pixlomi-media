"""Hafta 1 hikâye kareleri, 1080x1920."""
import os, base64
from kit import *

W, H = 1080, 1920
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
logo = lambda src: f'<img src="{src}" style="position:absolute;left:80px;top:130px;height:58px">'

S = []
# ST1 pazartesi
S.append(page(W, H, C["lime"], logo(LOGO_DARK) + f"""
<div class="tag" style="position:absolute;left:80px;top:300px">Haftanın sorusu</div>
<h1 style="position:absolute;left:80px;top:370px;width:920px;font-size:120px">Son gittiğin etkinliğin fotoğrafları <span class="hld">sana ulaştı mı?</span></h1>
<p class="body" style="position:absolute;left:80px;top:1010px;width:820px">Hikâyeyi yanıtla, kaç gün beklediğini yaz.</p>
""" + svg(0, 1180, W, 560, kare(560, 60, 1.2, mood="worried", arm="shrug") +
          f'<text x="90" y="230" font-family="Hand" font-weight="700" font-size="76" fill="{INK}" transform="rotate(-6 90 230)">hâlâ bekliyorum...</text>')))

# ST2 cuma, organizatöre
S.append(page(W, H, C["ink"], logo(LOGO_LIME) + f"""
<div class="tag" style="position:absolute;left:80px;top:300px;color:{C['lime']}">Organizatörlere</div>
<h1 style="position:absolute;left:80px;top:370px;width:920px;font-size:112px;color:{C['cream']}">Etkinlikten sonraki gün en çok hangi mesaj geliyor?</h1>
""" + svg(0, 900, W, 800, bubble(80, 60, 700, 120, "fotoğraflar ne zaman gelir?", fill=C['lime'], size=42) +
          bubble(300, 260, 700, 120, "beni çeken oldu mu?", fill=C['cream'], side="right", size=42) +
          bubble(80, 460, 700, 120, "drive linki açılmıyor", fill=C['lime'], size=42)) + f"""
<p class="body" style="position:absolute;left:80px;bottom:240px;width:880px;color:{C['cream']}">Yanıtla, bir sonraki Organizatör Notu'nu buna göre hazırlayalım.</p>
""", color=C["cream"]))

# ST3 pazar, carousel'e dönüş
thumb = "data:image/png;base64," + base64.b64encode(open(os.path.join(os.path.dirname(OUT), "out/png/A1.png"), "rb").read()).decode()
S.append(page(W, H, C["cream"], logo(LOGO_DARK) + f"""
<div class="tag" style="position:absolute;left:80px;top:300px">Kaçırdıysan</div>
<h1 style="position:absolute;left:80px;top:370px;width:920px;font-size:104px">Bu haftanın <span class="hl">organizatör</span> yazısı.</h1>
<img src="{thumb}" style="position:absolute;left:190px;top:720px;width:700px;border:6px solid {C['ink']};border-radius:28px;transform:rotate(-3deg)">
<div class="sticker" style="left:560px;top:1560px;background:{C['lime']};transform:rotate(4deg);font-size:36px">profilde seni bekliyor</div>
"""))

for i, h in enumerate(S, 1):
    open(os.path.join(OUT, f"ST{i}.html"), "w").write(h)
print("ok")
