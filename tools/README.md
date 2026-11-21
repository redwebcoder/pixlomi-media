# Pixlomi görsel üretim kiti

Haftalık içerik ajanı bu klasörü kullanır. Stil: koyu yeşil #1B453E, lime #C9F34B,
Funnel Display (başlık), Space Grotesk (metin), Caveat (el yazısı notlar).

## Kurulum
```
cd tools && mkdir -p fonts && cd fonts && npm pack @fontsource/funnel-display @fontsource/space-grotesk @fontsource/caveat \
 && for f in *.tgz; do tar xzf $f && mv package ${f%.tgz}; done && cd ..
pip install playwright pillow numpy --break-system-packages   # chrome: /usr/bin/google-chrome
```

## Üretim
- `carousels.py` → html/*.html ; `python3 render.py 1080 1350 out/png A1 A2 ...`
- `stories.py` → `python3 render.py 1080 1920 out/png ST1 ...`
- `videos.py` → html/R*_tr.html + videos.json ; `python3 capture.py out/video R1_tr ...` (sessiz mp4)
- `python3 audio.py html/videos.json out/video` (müzik + efekt wav) ; sonra
  `ffmpeg -i X_silent.mp4 -i X.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart X.mp4`
- İnsan fotoğrafları `people/pN.jpg` (yapay zekâ ile üretildi, paylaşırken AI etiketi işaretlenir).

## Kurallar
- `<html lang="tr">` (büyük harfte İ, Ü, Ş doğru çıksın). Site adı her yerde küçük harf: pixlomi.com
- Her içerikte bir insan fotoğrafı (photo()), büyük logo (head()), köşede soluk "pix".
- Yazım kontrol listesi strateji dokümanında.
