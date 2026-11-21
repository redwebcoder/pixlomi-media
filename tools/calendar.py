"""4 haftalık içerik takvimi CSV'si (23 Kasım - 20 Aralık 2026)."""
import csv, datetime as dt

START = dt.date(2026, 11, 23)
GUN = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# Her haftanın iki ana fikri: (seri, başlık/hook, kısa brief, carousel dosyası, video TR, video EN)
WEEKS = [
    dict(
        f1=("Fotoğraflar Nerede?", "Etkinlik bitti. Fotoğraflar kimde?", "Carousel A (6 kare)", "Reel1_FotograflarNerede_TR.mp4", "Reel1_WhereAreThePhotos_EN.mp4",
            "Düğünden 3 hafta sonra: Drive linki, 847 fotoğraf, sen 2 tanesindesin."),
        f2=("3 Adımda", "Fotoğrafını bulmak 3 adım sürer.", "Carousel B (5 kare)", "Reel2_3Adimda_TR.mp4", "Reel2_3Steps_EN.mp4",
            "QR'ı okut, selfie çek, fotoğrafların telefonunda."),
        story=["Hikaye_ST1.png: Son gittiğin etkinliğin fotoğrafları sana ulaştı mı?",
               "Hikaye_ST2.png: Organizatörlere, etkinlikten sonraki gün en çok gelen mesaj",
               "Hikaye_ST3.png: Kaçırdıysan, bu haftanın organizatör yazısı"],
        long=None, status="Hazır"),
    dict(
        f1=("Organizatör Notu", "5.000 koşucu, 40.000 kare. Herkes kendi fotoğrafını nasıl bulur?",
            "Carousel: koşu organizasyonunda foto teslimi için 5 karar (QR nereye, foto noktaları, start-bitiş, KVKK metni, sonuç maili)",
            "Video: bitiş çizgisi, madalya, telefona düşen kare (çizim + Kare)", "EN versiyon", "Koşucu madalyayı aldı, fotoğraf eve varmadan telefonunda."),
        f2=("Fotoğraflar Nerede?", "\"Fotoğrafları ne zaman göndereceksin?\" Bu soruyu bir daha duymayacaksın.",
            "Carousel: fotoğrafçı için PixlomiUp, makineden Wi-Fi ile galeriye", "Video: deklanşör, yarım saniye sonra galeride (gerçek ekran kaydı istenecek)", "EN versiyon",
            "Fotoğrafçılara meslektaş tonu."),
        story=["Anket karesi: Bir yarışta kendi fotoğrafını bulmak kaç dakikanı aldı?", "Organizatöre soru: Koşuda en çok neyle uğraşıyorsun?", "Hafta özeti: maraton carousel'ine dönüş"],
        long=("Pixlomi ile etkinlik kurulumu: QR, fotoğrafçı linki ve ilk galeri (adım adım)", "TR, 5-7 dk, gerçek ekran kaydı gerekli"),
        status="Üretilecek"),
    dict(
        f1=("Organizatör Notu", "Yılbaşı partisi: fotoğraflar ertesi sabah değil, o gece gelsin.",
            "Carousel: kurumsal yıl sonu partisi için 4 öneri, ekip fotoğrafı, sahne, foto köşesi, canlı ekran",
            "Video: parti biterken telefonlara düşen kareler", "EN versiyon", "Kurumsal iletişim ekiplerine."),
        f2=("3 Adımda", "Yüz tanıma ve KVKK: katılımcıya ne söylemelisiniz?",
            "Carousel: açık onay, şifreli saklama, sadece o etkinlik, silme talebi. Sade ve güven veren dil.",
            "Video: Doğukan'ın 30 sn telefonla anlatımı (çekim gerekli)", "EN: GDPR odaklı versiyon", "Güven içeriği."),
        story=["Soru kutusu: Yüz tanıma hakkında aklına takılan ne?", "Organizatöre: yılbaşı partisi planı yapan var mı?", "Hafta özeti"],
        long=None, status="Üretilecek"),
    dict(
        f1=("Bu Hafta Sahada", "Salondaki ekranda kendini gördüğün an.",
            "Carousel: canlı slayt ve kiosk modu, misafir kendi fotoğrafını büyük ekranda görür",
            "Video: sahadan gerçek kiosk çekimi (3. haftadan itibaren çekim listesi)", "EN versiyon", "Gerçek görüntü yoksa çizimle."),
        f2=("Dene", "İlk etkinliğin bizden: 200 Pix.",
            "Carousel: 200 Pix ile ne yapılır, kurulum 4 adım, hesap aç", "Video: panelde etkinlik oluşturma ekran kaydı", "EN versiyon", "Haftanın tek açık satış çağrısı."),
        story=["Anket: Bu yıl kaç etkinliğe gittin?", "Organizatöre: 2027 takvimini yaptın mı?", "Yıl sonu teşekkür karesi"],
        long=("How to deliver event photos to every guest with one selfie (Pixlomi walkthrough)", "EN, 5-7 dk, gerçek ekran kaydı gerekli"),
        status="Üretilecek"),
]

CAP = {  # 1. hafta için hazır metinler
    ("ig_car1"): "Etkinlik biter, ışıklar kapanır ve ertesi gün aynı soru gelir: Fotoğraflar ne zaman?\n\nFotoğrafçı günlerce ayıklar, link gruba düşer, misafirlerin çoğu kendini hiç bulamaz. En güzel kareler de bir klasörde kalır.\n\nPixlomi'de misafir QR'ı okutup bir selfie çekiyor. Kendi fotoğrafları etkinlik bitmeden telefonuna geliyor.\n\nEtkinlik planlayan birine gönder.\n\nEN: The event ends, the photos sit on a hard drive, and three weeks later a Drive link lands in a group chat. With Pixlomi, guests scan a QR, take a selfie and get their own photos before they leave.\n\n#etkinlikfotoğrafı #organizasyon #etkinlikplanlama #düğünorganizasyonu #pixlomi",
    ("tt_car1"): "Etkinlik bitti, fotoğraflar kimde? Kaydır, sonra etiketle: en son hangi etkinliğin fotoğraflarını bekledin? #etkinlik #düğün #organizasyon #pixlomi",
    ("ig_reel1"): "Aile grubunda 847 fotoğraf var, sen 2 tanesindesin. Bul bakalım.\n\nPixlomi'de selfie çekiyorsun, içinde olduğun kareler kendiliğinden telefonuna geliyor.\n\n#düğün #düğünfotoğrafı #etkinlik #pixlomi",
    ("tt_reel1_en"): "847 photos in the family group chat and you're in 2 of them. Good luck. With Pixlomi, one selfie brings your photos straight to your phone. #weddingphotos #eventphotography #eventplanner #pixlomi",
    ("tt_reel1_tr"): "Düğünden 3 hafta sonra gelen Drive linki. Bir dahakine selfie çek, fotoğrafların telefonuna gelsin. #düğün #fotoğraf #etkinlik #pixlomi",
    ("yt_reel1_tr"): "Başlık: Düğünden 3 hafta sonra gelen Drive linki #shorts\nAçıklama: Pixlomi'de misafir QR'ı okutur, selfie çeker, kendi fotoğrafları telefonuna gelir. pixlomi.com",
    ("yt_reel1_en"): "Title: 3 weeks after the wedding: the Drive link #shorts\nDescription: With Pixlomi, guests scan a QR, take a selfie and get their own photos. pixlomi.com",
    ("ig_car2"): "Uygulama indirmek yok, kayıt formu yok. QR'ı okut, selfie çek, gerisini Pixlomi halleder. Fotoğrafçı çektikçe yeni kareler telefonuna düşmeye devam eder.\n\nOrganizatörsen ilk etkinliğinde 200 Pix bizden. Bağlantı profilde.\n\nEN: Scan the QR, take a selfie and your photos come to you. No app to download. Organizers: your first event is on us.\n\n#pixlomi #etkinlik #qrkod #eventphotography",
    ("ig_reel2"): "Fotoğrafını bulmak üç adım: QR'ı okut, selfie çek, fotoğrafların telefonunda. Uygulama indirmeden.\n\nBir sonraki etkinlikte girişteki QR'a bak.\n\n#pixlomi #etkinlik #koşu #maraton #düğün",
    ("tt_reel2_en"): "3 steps to your own event photos: scan, selfie, done. No app needed. #eventtech #eventphotography #pixlomi",
    ("tt_reel2_tr"): "Koşu bitti, madalya boynunda. Fotoğrafın mı? 3 adımda telefonunda. #koşu #maraton #yarımaraton #pixlomi",
    ("yt_reel2_tr"): "Başlık: Etkinlik fotoğrafını 3 adımda bul #shorts\nAçıklama: QR'ı okut, selfie çek, fotoğrafların telefonunda. pixlomi.com",
    ("yt_reel2_en"): "Title: Find your event photos in 3 steps #shorts\nDescription: Scan the QR, take a selfie, get your photos. pixlomi.com",
}

rows = [["Tarih", "Saat", "Platform", "Format", "Başlık / ilk cümle", "Durum", "Dil", "Seri", "Metin (açıklama)", "Görsel / dosya", "Gün"]]


def add(d, saat, plat, fmt, title, status, dil, seri, metin, dosya):
    rows.append([d.isoformat(), saat, plat, fmt, title, status, dil, seri, metin, dosya, GUN[d.weekday()]])


for w, wk in enumerate(WEEKS):
    mon = START + dt.timedelta(days=7 * w)
    D = lambda i: mon + dt.timedelta(days=i)
    s1, t1, car1, v1, v1en, b1 = wk["f1"]
    s2, t2, car2, v2, v2en, b2 = wk["f2"]
    st = wk["status"]
    first = (w == 0)
    c = (lambda k, alt: CAP[k] if first else alt)
    add(D(0), "09:30", "Instagram", "Hikâye", wk["story"][0], st, "TR", "Etkileşim", "", wk["story"][0].split(":")[0] if first else "")
    add(D(1), "12:30", "Instagram", "Carousel", t1, st, "TR + EN", s1, c("ig_car1", "Ajan cuma üretecek. " + b1), car1)
    add(D(1), "18:00", "YouTube", "Shorts", t1, st, "TR", s1, c("yt_reel1_tr", "Ajan cuma üretecek."), v1)
    add(D(1), "19:30", "TikTok", "Foto carousel", t1, st, "TR", s1, c("tt_car1", "Ajan cuma üretecek."), car1)
    add(D(2), "20:30", "Instagram", "Reels", t1, st, "TR", s1, c("ig_reel1", "Ajan cuma üretecek. " + b1), v1)
    add(D(2), "21:30", "TikTok", "Video", t1, st, "EN", s1, c("tt_reel1_en", "Ajan cuma üretecek."), v1en)
    add(D(3), "09:30", "Instagram", "Carousel", t2, st, "TR + EN", s2, c("ig_car2", "Ajan cuma üretecek. " + b2), car2)
    add(D(3), "17:30", "YouTube", "Shorts", t1, st, "EN", s1, c("yt_reel1_en", "Ajan cuma üretecek."), v1en)
    add(D(3), "19:30", "TikTok", "Video", t1, st, "TR", s1, c("tt_reel1_tr", "Ajan cuma üretecek."), v1)
    add(D(4), "13:00", "Instagram", "Hikâye", wk["story"][1], st, "TR", "Etkileşim", "", wk["story"][1].split(":")[0] if first else "")
    add(D(4), "17:00", "YouTube", "Shorts", t2, st, "TR", s2, c("yt_reel2_tr", "Ajan cuma üretecek."), v2)
    add(D(4), "21:30", "TikTok", "Video", t2, st, "EN", s2, c("tt_reel2_en", "Ajan cuma üretecek."), v2en)
    add(D(5), "20:00", "YouTube", "Shorts", t2, st, "EN", s2, c("yt_reel2_en", "Ajan cuma üretecek."), v2en)
    add(D(5), "21:30", "Instagram", "Reels", t2, st, "TR", s2, c("ig_reel2", "Ajan cuma üretecek. " + b2), v2)
    if wk["long"]:
        add(D(6), "10:00", "YouTube", "Uzun video", wk["long"][0], "Çekim bekliyor", "TR" if w == 1 else "EN", "3 Adımda", wk["long"][1], "Ekran kaydı (Doğukan)")
    add(D(6), "11:00", "Instagram", "Hikâye", wk["story"][2], st, "TR", "Etkileşim", "", wk["story"][2].split(":")[0] if first else "")
    add(D(6), "11:00", "TikTok", "Video", t2, st, "TR", s2, c("tt_reel2_tr", "Ajan cuma üretecek."), v2)

with open("/home/claude/pixlomi/deliver/icerik_takvimi.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)
print(len(rows) - 1, "satır")
