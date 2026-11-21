"""Telifsiz, sıfırdan üretilen müzik ve efekt sesleri. Her reel için olay listesine göre miks yapar."""
import numpy as np, wave, sys, json, os

SR = 44100
rng = np.random.default_rng(7)


def t_(d):
    return np.arange(int(d * SR)) / SR


def env(n, a=0.005, r=0.2):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    na = min(na, n); e[:na] = np.linspace(0, 1, na)
    nr = min(nr, n); e[-nr:] *= np.linspace(1, 0, nr) ** 2
    return e


def note(f):
    return 440.0 * 2 ** ((f - 69) / 12)


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); s = 0.0
    for i in range(len(x)):
        s = (1 - a) * x[i] + a * s; y[i] = s
    return y


# ---------- müzik parçaları ----------
def kick():
    t = t_(0.35); f = 50 + 90 * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 0.9


def clap():
    t = t_(0.22); n = rng.standard_normal(len(t))
    e = np.exp(-t * 22) + 0.6 * np.exp(-((t - 0.012) % 0.011) * 300) * (t < 0.035)
    return lowpass(n, 2600) * e * 0.55


def hat(open_=False):
    t = t_(0.18 if open_ else 0.05); n = rng.standard_normal(len(t))
    hp = n - lowpass(n, 6000)
    return hp * np.exp(-t * (18 if open_ else 70)) * 0.22


def bass(f, d):
    t = t_(d); x = np.sign(np.sin(2 * np.pi * f * t)) * 0.5 + np.sin(2 * np.pi * f * t)
    return lowpass(x, 420) * env(len(t), 0.004, 0.06) * 0.32


def pluck(f, d=0.28):
    t = t_(d)
    x = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t))
    return x * np.exp(-t * 11) * 0.16


def pad(fs, d):
    t = t_(d); x = np.zeros(len(t))
    for f in fs:
        for det in (-0.12, 0.12):
            x += 2 * ((t * f * 2 ** (det / 12)) % 1) - 1
    x = lowpass(x / (len(fs) * 2), 1100)
    return x * env(len(t), 0.15, 0.4) * 0.11


def music(dur, bpm=112):
    beat = 60 / bpm; bar = beat * 4
    out = np.zeros(int((dur + 2) * SR))
    side = np.ones_like(out)

    def put(sig, at, gain=1.0):
        i = int(at * SR); j = min(len(out), i + len(sig))
        if i < len(out): out[i:j] += sig[:j - i] * gain

    chords = [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]  # C Am F G
    roots = [36, 33, 29, 31]
    arp = [0, 1, 2, 1, 2, 0, 1, 2]
    nbars = int(np.ceil(dur / bar)) + 1
    for b in range(nbars):
        t0 = b * bar; ch = chords[b % 4]
        put(pad([note(n) for n in ch], bar), t0)
        for k in range(8):
            put(bass(note(roots[b % 4] + (12 if k in (3, 7) else 0)), beat / 2 * 0.9), t0 + k * beat / 2)
            put(pluck(note(ch[arp[k]] + 12)), t0 + k * beat / 2, 0.9 if k % 2 == 0 else 0.6)
            put(hat(open_=(k == 7)), t0 + k * beat / 2, 1.0 if k % 2 else 0.6)
        for k in range(4):
            if b == 0 and k < 2:
                continue  # yumuşak giriş
            put(kick(), t0 + k * beat)
            i = int((t0 + k * beat) * SR)
            dk = int(0.18 * SR)
            if i < len(side):
                seg = np.linspace(0.45, 1, min(dk, len(side) - i))
                side[i:i + len(seg)] = np.minimum(side[i:i + len(seg)], seg)
            if k in (1, 3):
                put(clap(), t0 + k * beat)
    out = out * side
    return out[:int(dur * SR)]


# ---------- efektler ----------
def sfx_pop():
    t = t_(0.12); f = 900 * np.exp(-t * 18) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 30) * 0.5


def sfx_msg():
    t = t_(0.16); f = 1250 + 500 * (t > 0.05)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 22) * 0.35


def sfx_whoosh(d=0.45):
    t = t_(d); n = rng.standard_normal(len(t))
    sweep = np.zeros_like(n); s = 0.0
    for i in range(len(n)):
        c = 300 + 5000 * (i / len(n)) ** 1.5
        a = np.exp(-2 * np.pi * c / SR); s = (1 - a) * n[i] + a * s; sweep[i] = s
    e = np.sin(np.pi * t / d) ** 2
    return sweep * e * 0.55


def sfx_tick():
    t = t_(0.025); return np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 200) * 0.25


def sfx_ding():
    t = t_(0.9)
    x = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * k) * g for f, k, g in ((1318.5, 5, .5), (1975.5, 7, .3), (2637, 9, .15)))
    return x * 0.38


def sfx_chime():
    out = np.zeros(int(1.3 * SR))
    for i, n in enumerate((72, 76, 79, 84)):
        t = t_(0.9); s = np.sin(2 * np.pi * note(n) * t) * np.exp(-t * 4) * 0.25
        j = int(i * 0.09 * SR); out[j:j + len(s)] += s
    return out


def sfx_shutter():
    out = np.zeros(int(0.25 * SR))
    for at in (0.0, 0.07):
        t = t_(0.05); n = rng.standard_normal(len(t)) * np.exp(-t * 90)
        j = int(at * SR); out[j:j + len(n)] += lowpass(n, 4000) * 0.7
    return out


def sfx_beep():
    t = t_(0.12); return np.sin(2 * np.pi * 1760 * t) * env(len(t), 0.003, 0.05) * 0.25


SFX = dict(pop=sfx_pop, msg=sfx_msg, whoosh=sfx_whoosh, tick=sfx_tick, ding=sfx_ding, chime=sfx_chime,
           shutter=sfx_shutter, beep=sfx_beep)


def mix(dur, events, out_wav, vo=None):
    m = music(dur)
    fx = np.zeros_like(m)
    cache = {}
    for at, kind in events:
        s = cache.setdefault(kind, SFX[kind]())
        i = int(at * SR); j = min(len(fx), i + len(s))
        if 0 <= i < len(fx): fx[i:j] += s[:j - i]
    music_gain = 0.55
    if vo is not None:
        music_gain = 0.28
    y = m * music_gain + fx
    if vo is not None:
        y[:len(vo)] += vo[:len(y)]
    # giriş/çıkış ve sınırlama
    fi, fo = int(0.25 * SR), int(0.8 * SR)
    y[:fi] *= np.linspace(0, 1, fi); y[-fo:] *= np.linspace(1, 0, fo)
    y = np.tanh(y * 1.2) / np.tanh(1.2)
    y = y / max(1e-9, np.abs(y).max()) * 0.89
    st = np.stack([y, y], 1)
    st[:, 1] = np.roll(y, int(0.008 * SR)) * 0.96 + y * 0.04  # hafif stereo genişlik
    pcm = (st * 32767).astype(np.int16)
    with wave.open(out_wav, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


if __name__ == "__main__":
    meta = json.load(open(sys.argv[1]))
    for name, m in meta.items():
        mix(m["dur"], m["events"], os.path.join(sys.argv[2], name + ".wav"))
        print("ok", name)
