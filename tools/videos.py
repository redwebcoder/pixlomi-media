"""Hafta 1 Reels/TikTok/Shorts: R1 'Fotoğraflar nerede?' ve R2 '3 adımda'. 1080x1920, JS zaman çizelgesi.
Her reel için ses olayları (efekt zamanlamaları) videos.json'a yazılır."""
import os, json
from kit import *

W, H = 1080, 1920
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")

JS_BASE = """
<script>
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>1-Math.pow(1-clamp(x),3);
const back=x=>{x=clamp(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
function pop(id,t,t0,d=.35,dy=60){const e=document.getElementById(id);if(!e)return;const p=(t-t0)/d;
  e.style.opacity=clamp(p*1.6);e.style.transform=`translateY(${(1-ease(p))*dy}px) scale(${.9+.1*back(p)})`;}
function scene(id,t,a,b){document.getElementById(id).style.display=(t>=a&&t<b)?'block':'none';}
function svgpop(id,t,t0,d=.3){const e=document.getElementById(id);if(!e)return;const p=clamp((t-t0)/d);
  e.style.opacity=p;e.style.transformBox='fill-box';e.style.transformOrigin='center';e.style.transform=`scale(${.4+.6*back(p)})`;}
</script>
"""

CSS = """
.sc{position:absolute;inset:0;display:none}
.big{position:absolute;left:80px;width:920px;font-weight:800;letter-spacing:-0.03em;line-height:1.05}
.pop{opacity:0;will-change:transform}
.vlogo{position:absolute;left:80px;top:110px;height:96px;z-index:5}
"""


def vlogo(dark_bg=False):
    return f'<img class="vlogo" src="{LOGO_LIME if dark_bg else LOGO_DARK}">'


def tiles(x, y, w, cols, rows, prefix, gap=12):
    pal = [C["lime"], C["sage"], C["pale"], "#FFFFFF"]
    cw = (w - gap * (cols - 1)) / cols
    out, k = [], 0
    for r in range(rows):
        for c in range(cols):
            X, Y = x + c * (cw + gap), y + r * (cw + gap)
            out.append(rrect(X, Y, cw, cw, 8, fill="none", sw=3, extra='stroke-dasharray="10 9" opacity=".4"'))
            out.append(f'<g id="{prefix}{k}" style="opacity:0">{mini_photo(X, Y, cw, cw, pal[(k*7+r) % 4], kind=(k*5+r) % 3)}</g>')
            k += 1
    return "".join(out), k


def bubble_div(i, txt):
    s = svg(0, 0, 720, 170, bubble(10, 10, 680, 110, txt, fill=(C["white"] if i % 2 == 0 else C["lime"]),
                                   side=("left" if i % 2 == 0 else "right"), size=40))
    s = s.replace('style="left:0px;top:0px"', 'style="position:static"')
    return f'<div id="b{i}" class="pop" style="position:absolute;left:{80 if i % 2 == 0 else 300}px;top:{580 + i*190}px">{s}</div>'


def reel1(lang):
    T = dict(
        tr=dict(s1="Düğünden 3 hafta sonra:", b=["drive linki attım", "açılmıyor bende", "beni bulan var mı?", "kaç GB bu ya"],
                grp="Aile grubu · 63 yeni mesaj", n="fotoğraf.", n2="Sen 2 tanesindesin.", s4="Bir de şöyle:",
                s4b="QR'ı okut, selfie çek.<br>Fotoğrafların telefonunda.",
                s5='Fotoğraflar <span class="hld">sahiplerini</span> bulsun.', tag="Fotoğraflar nerede?",
                stamp="QR · SELFIE · HAZIR · "),
        en=dict(s1="3 weeks after the wedding:", b=["sent the drive link", "won't open for me", "anyone found me?", "how many GB is this"],
                grp="Family group · 63 new messages", n="photos.", n2="You're in 2 of them.", s4="Or like this:",
                s4b="Scan the QR, take a selfie.<br>Your photos, on your phone.",
                s5='Every photo finds <span class="hld">its owner.</span>', tag="Where are the photos?",
                stamp="SCAN · SELFIE · DONE · "))[lang]
    g, ntiles = tiles(330, 300, 300, 3, 4, "t")
    bub = "".join(bubble_div(i, txt) for i, txt in enumerate(T["b"]))
    html = f"""
<div class="sc" id="S1" style="background:{C['lime']}">{vlogo()}
  <div class="tag" style="position:absolute;left:80px;top:270px">{T['tag']}</div>
  <div id="s1t" class="big pop" style="top:330px;font-size:150px">{T['s1']}</div>
  <div id="s1k" class="pop" style="position:absolute;left:0;top:0;width:1080px;height:1920px">{photo(0, 170, 760, 740, 900, rot=-3, pos="50% 30%")}</div>
</div>
<div class="sc" id="S2" style="background:{C['cream']}">{vlogo()}
  <div class="tag" style="position:absolute;left:80px;top:300px">{T['grp']}</div>{bub}
</div>
<div class="sc" id="S3" style="background:{C['peri']}">{vlogo()}
  <div class="big" style="top:420px;font-size:260px" id="cnt">0</div>
  <div class="big" style="top:720px;font-size:120px">{T['n']}</div>
  <div id="s3b" class="big pop" style="top:960px;font-size:120px">{T['n2']}</div>
  <div id="s3k" class="pop" style="position:absolute;left:0;top:1260px">{svg(0, 0, 1080, 400, kare(700, 0, .95, mood="wow", arm="shrug"))}</div>
</div>
<div class="sc" id="S4" style="background:{C['ink']};color:{C['cream']}">{vlogo(True)}
  <div id="s4t" class="big pop" style="top:270px;font-size:130px;color:{C['lime']}">{T['s4']}</div>
  <div id="s4b" class="pop body" style="position:absolute;left:80px;top:450px;font-size:42px;color:{C['cream']}">{T['s4b']}</div>
  {photo(1, 50, 820, 560, 760, rot=-4, pos="50% 30%", border=C['lime'], z=1)}
  {svg(340, 640, 1080, 900, phone(300, 120, 360, 720, '', fill=C['cream']) + g)}
</div>
<div class="sc" id="S5" style="background:{C['lime']}">{vlogo()}
  <div id="s5t" class="big pop" style="top:300px;font-size:150px">{T['s5']}</div>
  <div id="s5u" class="pop sticker" style="left:80px;top:880px;background:{C['ink']};color:{C['lime']};font-size:52px;transform:rotate(-3deg)">pixlomi.com</div>
  <div id="s5s" class="pop" style="position:absolute;left:0;top:1060px;width:1080px;height:860px">{photo(5, 80, 30, 560, 680, rot=-3, pos="50% 40%")}{svg(0, 0, 1080, 760, stamp(820, 420, 150, T['stamp'], fill=C['white'], size=32))}</div>
</div>
"""
    js = f"""
<script>
window.render=function(t){{
 scene('S1',t,0,2.3);scene('S2',t,2.3,5.4);scene('S3',t,5.4,7.8);scene('S4',t,7.8,10.5);scene('S5',t,10.5,99);
 pop('s1t',t,.15,.45);pop('s1k',t,.7,.4,120);
 for(let i=0;i<4;i++)pop('b'+i,t,2.45+i*.62,.3,40);
 const c=document.getElementById('cnt');c.textContent=Math.round(847*ease((t-5.5)/1.1)).toLocaleString('tr-TR');
 pop('s3b',t,6.6,.35);pop('s3k',t,6.9,.35,80);
 pop('s4t',t,7.9,.35);pop('s4b',t,8.3,.35);
 for(let i=0;i<{ntiles};i++)svgpop('t'+i,t,8.6+i*.13,.25);
 pop('s5t',t,10.6,.45);pop('s5u',t,11.1,.35);pop('s5s',t,11.3,.4,80);
}};
</script>"""
    ev = [(0.15, "pop"), (0.7, "pop"), (2.1, "whoosh"), (5.2, "whoosh"), (7.6, "whoosh"), (10.3, "whoosh")]
    ev += [(2.45 + i * .62, "msg") for i in range(4)]
    ev += [(5.5 + k * 0.07, "tick") for k in range(15)]
    ev += [(6.6, "pop"), (6.9, "pop"), (7.9, "pop"), (8.3, "pop")]
    ev += [(8.6 + i * .13, "tick") for i in range(ntiles)] + [(8.6 + ntiles * .13, "ding")]
    ev += [(10.6, "chime"), (11.1, "pop"), (11.3, "pop")]
    return page(W, H, C["lime"], html, extra_css=CSS).replace("</body>", JS_BASE + js + "</body>"), 12.6, ev


def reel2(lang):
    T = dict(
        tr=dict(s1='Fotoğrafını bulmak <span class="hld">3 adım</span> sürer.', a="QR'ı okut.", b="Selfie çek.", c="Fotoğrafların telefonunda.",
                ok="eşleşti", e1="Uygulama yok.", e2="Bekleme yok.", tag="3 adımda"),
        en=dict(s1='Your event photos in <span class="hld">3 steps.</span>', a="Scan the QR.", b="Take a selfie.", c="Your photos, on your phone.",
                ok="matched", e1="No app.", e2="No waiting.", tag="3 steps"))[lang]
    g, ntiles = tiles(392, 860, 296, 3, 4, "u")
    big = "font-weight:800;letter-spacing:-0.03em;line-height:1.02;font-size:150px"
    html = f"""
<div class="sc" id="S1" style="background:{C['peri']}">{vlogo()}
  <div class="tag" style="position:absolute;left:80px;top:270px">{T['tag']}</div>
  <div id="a1" class="big pop" style="top:330px;font-size:126px">{T['s1']}</div>
  <div id="a2" class="pop" style="position:absolute;left:0;top:0;width:1080px;height:1920px">{photo(2, 110, 900, 860, 700, rot=-3, pos="50% 30%")}</div>
</div>
<div class="sc" id="S2" style="background:{C['cream']}">{vlogo()}
  <div class="big" style="top:250px;font-size:170px">01</div>
  <div id="b1" class="big pop" style="top:440px;font-size:130px">{T['a']}</div>
  {photo(4, 150, 680, 780, 1000, rot=0, pos="50% 30%", tape=False, z=1)}
  {svg(150, 680, 780, 1000, f'<rect id="scan" x="250" y="250" width="320" height="10" rx="5" fill="{C["lime"]}" stroke="{C["ink"]}" stroke-width="3"/>', rough=False)}
</div>
<div class="sc" id="S3" style="background:{C['lime']}">{vlogo()}
  <div class="big" style="top:250px;font-size:170px">02</div>
  <div id="c1" class="big pop" style="top:440px;font-size:130px">{T['b']}</div>
  {svg(0, 700, 1080, 900, phone(330, 60, 420, 780, f'<circle cx="540" cy="420" r="130" fill="{C["sage"]}" stroke="{INK}" stroke-width="7"/><circle cx="500" cy="400" r="12" fill="{INK}"/><circle cx="580" cy="400" r="12" fill="{INK}"/>' + wob("M495 460 Q540 492 585 460", sw=7) + f'<rect id="frm" x="380" y="250" width="320" height="340" rx="24" fill="none" stroke="{INK}" stroke-width="7" stroke-dasharray="44 230" stroke-dashoffset="22"/>', fill=C['white']))}
  <div id="c2" class="pop sticker" style="left:620px;top:1500px;background:{C['ink']};color:{C['lime']};font-size:44px;transform:rotate(-5deg)">✓ {T['ok']}</div>
</div>
<div class="sc" id="S4" style="background:{C['white']}">{vlogo()}
  <div class="big" style="top:250px;font-size:170px">03</div>
  <div id="d1" class="big pop" style="top:440px;font-size:120px">{T['c']}</div>
  {svg(0, 0, 1080, 1920, phone(350, 760, 380, 760, '', fill=C['white']) + g)}
</div>
<div class="sc" id="S5" style="background:{C['ink']};color:{C['cream']}">{vlogo(True)}
  <div style="position:absolute;left:80px;top:330px;width:920px;display:flex;flex-direction:column;gap:30px;align-items:flex-start">
  <div id="e1" class="pop" style="{big};color:{C['cream']}">{T['e1']}</div>
  <div id="e2" class="pop" style="{big};color:{C['lime']}">{T['e2']}</div>
  <div id="e3" class="pop sticker" style="position:relative;margin-top:60px;background:{C['lime']};color:{C['ink']};font-size:56px;transform:rotate(-3deg)">pixlomi.com</div></div>
</div>
"""
    js = f"""
<script>
window.render=function(t){{
 scene('S1',t,0,2.2);scene('S2',t,2.2,4.7);scene('S3',t,4.7,7.3);scene('S4',t,7.3,9.9);scene('S5',t,9.9,99);
 pop('a1',t,.15,.45);pop('a2',t,.7,.4,120);
 pop('b1',t,2.3,.35);
 const s=document.getElementById('scan');s.setAttribute('y',230+300*(.5-.5*Math.cos((t-2.4)*4.2)));
 pop('c1',t,4.8,.35);
 const f=document.getElementById('frm');f.style.opacity=(t>6.0)?1:(.5+.5*Math.sin(t*14));
 f.setAttribute('stroke-width', t>6.1?'11':'7');
 pop('c2',t,6.15,.3);
 pop('d1',t,7.4,.35);
 for(let i=0;i<{ntiles};i++)svgpop('u'+i,t,7.9+i*.12,.25);
 pop('e1',t,10.0,.35);pop('e2',t,10.45,.35);pop('e3',t,10.9,.35);
}};
</script>"""
    ev = [(0.15, "pop"), (0.7, "pop"), (2.0, "whoosh"), (4.5, "whoosh"), (7.1, "whoosh"), (9.7, "whoosh"),
          (2.3, "pop"), (3.0, "beep"), (3.75, "beep"), (4.25, "ding"), (4.8, "pop"), (5.7, "shutter"), (6.15, "chime"), (7.4, "pop")]
    ev += [(7.9 + i * .12, "tick") for i in range(ntiles)]
    ev += [(10.0, "pop"), (10.45, "pop"), (10.9, "chime")]
    return page(W, H, C["peri"], html, extra_css=CSS).replace("</body>", JS_BASE + js + "</body>"), 12.2, ev


if __name__ == "__main__":
    meta = {}
    for name, fn in (("R1", reel1), ("R2", reel2)):
        for lang in ("tr", "en"):
            html, dur, ev = fn(lang)
            open(os.path.join(OUT, f"{name}_{lang}.html"), "w").write(html)
            meta[f"{name}_{lang}"] = dict(dur=dur, events=ev)
    json.dump(meta, open(os.path.join(OUT, "videos.json"), "w"))
    print({k: v["dur"] for k, v in meta.items()})
