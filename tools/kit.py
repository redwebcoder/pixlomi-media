"""Pixlomi görsel kiti: renkler, fontlar, el çizimi SVG parçaları ve sayfa iskeleti."""
import random, math, base64, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTDIR = os.path.join(HERE, "fonts")

# Pixlomi marka renkleri (logo dosyalarından): koyu yeşil #1B453E, lime #C9F34B, açık gri zemin
C = dict(lime="#C9F34B", ink="#1B453E", cream="#EEEEE8", peri="#BCD7CE",
         orange="#FFFFFF", lilac="#E3F7A4", white="#FFFFFF", green="#1B453E", sage="#BCD7CE", pale="#E3F7A4")


def _font_face(family, path, weight, rng):
    data = base64.b64encode(open(path, "rb").read()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:normal;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');unicode-range:{rng};}}")


def font_css():
    out = []
    latin = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
    ext = "U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
    for fam, pkg, prefix, weights in [
        ("Brico", "funnel-display", "funnel-display", [400, 500, 600, 700, 800]),
        ("Mono", "space-grotesk", "space-grotesk", [400, 500, 600, 700]),
        ("Hand", "caveat", "caveat", [400, 700]),
    ]:
        d = glob.glob(os.path.join(FONTDIR, f"fontsource-{pkg}-*/files"))[0]
        for w in weights:
            for sub, rng in (("latin", latin), ("latin-ext", ext)):
                p = os.path.join(d, f"{prefix}-{sub}-{w}-normal.woff2")
                if os.path.exists(p):
                    out.append(_font_face(fam, p, w, rng))
    return "\n".join(out)


FONT_CSS = font_css()
LOGO_DARK = "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "brand", "logo_koyu.png"), "rb").read()).decode()
LOGO_LIME = "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "brand", "logo_lime.png"), "rb").read()).decode()

# ---------- filtreler: titrek çizgi + kâğıt dokusu ----------
DEFS = """
<defs>
  <filter id="rough" x="-5%" y="-5%" width="110%" height="110%">
    <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="4.5" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <pattern id="dots" width="11" height="11" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
    <circle cx="3" cy="3" r="2.1" fill="#1B453E"/>
  </pattern>
  <pattern id="dotsSmall" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
    <circle cx="2" cy="2" r="1.4" fill="#1B453E"/>
  </pattern>
</defs>
"""

GRAIN = ("data:image/svg+xml;base64," + base64.b64encode(
    b"<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='g'>"
    b"<feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/>"
    b"<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.55 0'/></filter>"
    b"<rect width='100%' height='100%' filter='url(#g)'/></svg>").decode())

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#222}
.page{position:relative;overflow:hidden;font-family:'Brico';color:#17171A}
.grain{position:absolute;inset:0;background-image:url(%s);opacity:.16;mix-blend-mode:multiply;pointer-events:none;z-index:50}
.head{position:absolute;left:72px;right:72px;top:52px;display:flex;align-items:center;justify-content:space-between;z-index:5}
.logo img{display:block;height:76px;width:auto}
.prog{display:flex;gap:8px}
.prog b{display:block;width:34px;height:9px;border-radius:5px;background:currentColor;opacity:.22}
.prog b.on{opacity:1}
.tag{font-family:'Mono';font-weight:600;font-size:28px;letter-spacing:0}
.hl{background:linear-gradient(transparent 14%%,#C9F34B 14%%,#C9F34B 96%%,transparent 96%%);color:#1B453E;padding:0 .14em;border-radius:.14em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hld{background:linear-gradient(transparent 14%%,#1B453E 14%%,#1B453E 96%%,transparent 96%%);color:#C9F34B;padding:0 .14em;border-radius:.14em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.pix{position:absolute;right:-30px;bottom:-110px;font-family:'Brico';font-weight:800;font-size:520px;letter-spacing:-0.06em;line-height:1;color:currentColor;opacity:.06;pointer-events:none}
h1{font-weight:800;letter-spacing:-0.03em;line-height:1.02}
.body{font-family:'Mono';font-size:34px;line-height:1.38;font-weight:400}
.en{font-family:'Mono';font-size:24px;line-height:1.35;opacity:.75}
.hand{font-family:'Hand';font-weight:700}
.sticker{position:absolute;padding:14px 28px;border:4px solid #1B453E;border-radius:18px;font-family:'Mono';font-weight:700;font-size:28px;z-index:6}
svg.ill{position:absolute;overflow:visible;z-index:2}
""" % GRAIN


def page(w, h, bg, inner, color=None, extra_css="", pix=True):
    color = color or C["ink"]
    pixmark = '<div class="pix">pix</div>' if pix else ''
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{FONT_CSS}{BASE_CSS}{extra_css}</style></head>
<body><div class="page" style="width:{w}px;height:{h}px;background:{bg};color:{color}">
{pixmark}{inner}
<div class="grain"></div></div></body></html>"""


def head(n, total, color=None, label="pixlomi"):
    bars = "".join(f'<b class="{"on" if i == n else ""}"></b>' for i in range(total))
    src = LOGO_LIME if color and color != C["ink"] else LOGO_DARK
    return f'<div class="head" style="color:{color or C["ink"]}"><div class="logo"><img src="{src}"></div><div class="prog">{bars}</div></div>'


# ---------- el çizimi parçalar (SVG) ----------
INK = C["ink"]


def wob(d, sw=6, fill="none", stroke=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def rrect(x, y, w, h, r, fill="none", sw=6, stroke=INK, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def qr(x, y, s, seed=3, color=INK, bg="#FFFDF8"):
    rnd = random.Random(seed)
    n = 21
    c = s / n
    out = [f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{bg}"/>']
    finder = {(0, 0), (0, n - 7), (n - 7, 0)}

    def in_finder(i, j):
        for fi, fj in finder:
            if fi - 1 <= i <= fi + 7 and fj - 1 <= j <= fj + 7:
                return True
        return False
    for i in range(n):
        for j in range(n):
            if not in_finder(i, j) and rnd.random() < 0.48:
                out.append(f'<rect x="{x + j * c:.1f}" y="{y + i * c:.1f}" width="{c + .4:.1f}" height="{c + .4:.1f}" fill="{color}"/>')
    for fi, fj in finder:
        X, Y = x + fj * c, y + fi * c
        out.append(f'<rect x="{X + c/2:.1f}" y="{Y + c/2:.1f}" width="{6*c:.1f}" height="{6*c:.1f}" fill="none" stroke="{color}" stroke-width="{c:.1f}"/>')
        out.append(f'<rect x="{X + 2*c:.1f}" y="{Y + 2*c:.1f}" width="{3*c:.1f}" height="{3*c:.1f}" fill="{color}"/>')
    return "".join(out)


def mini_photo(x, y, w, h, bg, kind=0):
    """Galerideki küçük fotoğraf: zemin + basit pictogram (dağ/güneş, iki kişi, kalabalık)."""
    s = [rrect(x, y, w, h, 8, fill=bg, sw=4)]
    if kind == 0:   # dağ + güneş
        s.append(f'<circle cx="{x + w*.72}" cy="{y + h*.3}" r="{w*.1}" fill="{INK}"/>')
        s.append(wob(f"M{x+6} {y+h-6} L{x+w*.38} {y+h*.45} L{x+w*.6} {y+h*.7} L{x+w*.75} {y+h*.55} L{x+w-6} {y+h-6}", sw=4, fill=INK))
    elif kind == 1:  # iki kişi
        for cx in (x + w*.36, x + w*.64):
            s.append(f'<circle cx="{cx}" cy="{y + h*.38}" r="{w*.1}" fill="{INK}"/>')
            s.append(wob(f"M{cx - w*.15} {y+h-6} Q{cx} {y + h*.48} {cx + w*.15} {y+h-6}", sw=4, fill=INK))
    else:            # kalabalık başlar
        for k in range(5):
            cx = x + w*(.14 + k*.18)
            s.append(f'<circle cx="{cx}" cy="{y + h*(.62 if k % 2 else .55)}" r="{w*.075}" fill="{INK}"/>')
        s.append(f'<rect x="{x+4}" y="{y+h*.72}" width="{w-8}" height="{h*.28-4}" rx="4" fill="{INK}"/>')
    return "".join(s)


def phone(x, y, w, h, screen="", fill="#FFFDF8", sw=7):
    r = w * 0.16
    out = [rrect(x, y, w, h, r, fill=fill, sw=sw),
           rrect(x + w*.36, y + 16, w*.28, 14, 7, fill=INK, sw=0)]
    out.append(screen)
    return "".join(out)


def gallery(x, y, w, cols=3, rows=4, filled=12, gap=10, highlight=None, palette=None):
    palette = palette or [C["lime"], C["sage"], C["pale"], "#FFFFFF"]
    cw = (w - gap * (cols - 1)) / cols
    out = []
    k = 0
    for r in range(rows):
        for c in range(cols):
            X, Y = x + c * (cw + gap), y + r * (cw + gap)
            if k < filled:
                out.append(mini_photo(X, Y, cw, cw, palette[(k * 7 + r) % len(palette)], kind=(k * 5 + r) % 3))
                if highlight and k in highlight:
                    out.append(rrect(X - 6, Y - 6, cw + 12, cw + 12, 12, sw=5, stroke=INK, extra='stroke-dasharray="2 10"'))
            else:
                out.append(rrect(X, Y, cw, cw, 8, fill="none", sw=3, extra='stroke-dasharray="10 9" opacity=".45"'))
            k += 1
    return "".join(out)


def kare(x, y, s=1.0, mood="happy", arm="wave", color=None):
    """'Kare' maskotu: vizör kafalı çizgi figür. (x,y)= kafanın sol üstü, kafa 150px * s."""
    color = color or C["white"]
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    # bacaklar
    g.append(wob("M60 230 Q52 300 40 352", sw=8))
    g.append(wob("M92 230 Q104 298 122 350", sw=8))
    g.append(wob("M18 356 Q40 340 60 356 Z", sw=7, fill=INK))
    g.append(wob("M112 352 Q134 338 152 356 Z", sw=7, fill=INK))
    # gövde
    g.append(rrect(40, 158, 72, 82, 26, fill=C["lime"], sw=7))
    g.append(f'<rect x="46" y="200" width="60" height="34" rx="14" fill="url(#dotsSmall)" opacity=".35"/>')
    # kollar
    if arm == "wave":
        g.append(wob("M44 180 Q8 160 -10 118", sw=8))
        g.append(wob("M108 182 Q150 200 168 236", sw=8))
    elif arm == "point":
        g.append(wob("M44 182 Q14 210 4 246", sw=8))
        g.append(wob("M108 178 Q160 160 200 150", sw=8))
        g.append(wob("M198 150 l14 -8 M198 150 l16 6", sw=7))
    elif arm == "hold":
        g.append(wob("M44 180 Q30 210 60 222", sw=8))
        g.append(wob("M108 180 Q126 212 96 222", sw=8))
    elif arm == "shrug":
        g.append(wob("M44 180 Q0 176 -14 140", sw=8))
        g.append(wob("M108 180 Q152 176 166 140", sw=8))
    # kafa: vizör
    g.append(rrect(0, 0, 152, 150, 34, fill=color, sw=8))
    for (a, b, c_, d) in [("M18 46", "V22", "Q18 18 22 18", "H46"), ("M106 18", "H130", "Q134 18 134 22", "V46"),
                         ("M134 104", "V128", "Q134 132 130 132", "H106"), ("M46 132", "H22", "Q18 132 18 128", "V104")]:
        g.append(wob(f"{a} {b} {c_} {d}", sw=6))
    # yüz
    if mood == "happy":
        g.append(f'<circle cx="56" cy="66" r="8" fill="{INK}"/><circle cx="96" cy="66" r="8" fill="{INK}"/>')
        g.append(wob("M54 92 Q76 112 98 92", sw=6))
    elif mood == "worried":
        g.append(f'<circle cx="56" cy="70" r="8" fill="{INK}"/><circle cx="96" cy="70" r="8" fill="{INK}"/>')
        g.append(wob("M44 58 L62 49 M108 58 L90 49", sw=5))
        g.append(wob("M58 104 Q76 94 94 104", sw=6))
    elif mood == "wow":
        g.append(f'<circle cx="56" cy="64" r="9" fill="{INK}"/><circle cx="96" cy="64" r="9" fill="{INK}"/>')
        g.append(f'<ellipse cx="76" cy="100" rx="11" ry="14" fill="{INK}"/>')
    g.append('</g>')
    return "".join(g)


def stamp(cx, cy, r, text, fill=None, color=INK, rot=-12, size=27):
    fill = fill or C["lime"]
    pid = f"st{abs(hash((cx, cy, text))) % 10**6}"
    return (f'<g transform="rotate({rot} {cx} {cy})">'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*.56}" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<path id="{pid}" d="M{cx - r*.78} {cy} a{r*.78} {r*.78} 0 1 1 {r*1.56} 0 a{r*.78} {r*.78} 0 1 1 {-r*1.56} 0" fill="none"/>'
            f'<text font-family="Mono" font-weight="700" font-size="{size}" letter-spacing="3" fill="{color}">'
            f'<textPath href="#{pid}" textLength="{2*math.pi*r*.78*.97:.0f}" lengthAdjust="spacing">{text}</textPath></text></g>')


def bubble(x, y, w, h, text, fill="#FFFDF8", side="left", size=34, tcolor=INK):
    tail = (f"M{x+30} {y+h-4} L{x+8} {y+h+30} L{x+70} {y+h-4}" if side == "left"
            else f"M{x+w-30} {y+h-4} L{x+w-8} {y+h+30} L{x+w-70} {y+h-4}")
    return (wob(tail, sw=6, fill=fill) + rrect(x, y, w, h, 28, fill=fill, sw=6) +
            f'<rect x="{x+20}" y="{y+h-14}" width="{70 if side=="left" else 0}" height="10" fill="{fill}"/>' * 0 +
            f'<text x="{x+30}" y="{y+h/2+size*.36}" font-family="Mono" font-weight="700" font-size="{size}" fill="{tcolor}">{text}</text>')


def camera(x, y, s=1.0, fill=None):
    fill = fill or C["white"]
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    g.append(wob("M60 40 L84 6 H176 L200 40", sw=8, fill=fill))
    g.append(rrect(0, 40, 280, 180, 28, fill=fill, sw=8))
    g.append(f'<rect x="12" y="150" width="256" height="58" rx="18" fill="url(#dots)" opacity=".35"/>')
    g.append(f'<circle cx="140" cy="130" r="70" fill="{C["ink"]}" stroke="{INK}" stroke-width="8"/>')
    g.append(f'<circle cx="140" cy="130" r="44" fill="{C["lime"]}" stroke="{INK}" stroke-width="6"/>')
    g.append(f'<circle cx="124" cy="114" r="12" fill="{C["white"]}"/>')
    g.append(rrect(214, 60, 44, 24, 8, fill=C["lime"], sw=5))
    g.append('</g>')
    return "".join(g)


def wifi(cx, cy, s=1.0, sw=8, color=INK):
    out = []
    for i, r in enumerate((26, 52, 78)):
        r *= s
        out.append(f'<path d="M{cx - r*.75} {cy - r*.66} A{r} {r} 0 0 1 {cx + r*.75} {cy - r*.66}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{8*s}" fill="{color}"/>')
    return "".join(out)


def svg(x, y, w, h, inner, rough=True, vb=None):
    vb = vb or f"0 0 {w} {h}"
    filt = ' filter="url(#rough)"' if rough else ""
    return (f'<svg class="ill" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="{vb}" '
            f'xmlns="http://www.w3.org/2000/svg">{DEFS}<g{filt}>{inner}</g></svg>')


def _img64(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


PEOPLE = {i: _img64(os.path.join(HERE, "people", f"p{i}.jpg")) for i in range(6)}


def photo(i, x, y, w, h, rot=-3, pos="center", z=2, tape=True, border=None):
    """Gerçekçi insan fotoğrafı, marka çerçevesiyle (yeşil kenar, hafif eğik, bant)."""
    border = border or C["ink"]
    t = ""
    if tape:
        t = (f'<div style="position:absolute;left:{w/2-70}px;top:-26px;width:140px;height:44px;background:{C["lime"]};'
             f'opacity:.92;transform:rotate({-rot*2+3}deg);border:3px solid {C["ink"]};border-radius:6px;z-index:3"></div>')
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);z-index:{z}">'
            f'<div style="position:absolute;inset:0;border:7px solid {border};border-radius:30px;overflow:hidden;background:#000">'
            f'<img src="{PEOPLE[i]}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};display:block"></div>{t}</div>')
