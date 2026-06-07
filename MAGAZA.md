# LUMI — Play Store & App Store Yükleme Rehberi

Bu rehber, LUMI prototipini **Google Play Store** ve **Apple App Store**'a yüklemek için gereken adımları anlatır.

> **Önemli:** Mağazalara yükleme senin geliştirici hesabınla yapılır. Ben senin adına yükleyemem; ama proje tamamen buna hazır.

---

## Ön koşullar

| Gereksinim | Play Store | App Store |
|------------|------------|-----------|
| Geliştirici hesabı | Google Play Console — **$25** (tek sefer) | Apple Developer — **$99/yıl** |
| Bilgisayar | Windows / Mac / Linux | **Mac zorunlu** (Xcode) |
| Yazılım | Node.js, Android Studio | Node.js, Xcode |
| Dosya | **AAB** (App Bundle) | **IPA** (Archive) |
| Gizlilik politikası | **Zorunlu URL** | **Zorunlu URL** |

---

## Adım 1 — Node.js kur

1. https://nodejs.org → **LTS** indir ve kur
2. Terminali kapat/aç
3. Kontrol: `node -v` ve `npm -v`

---

## Adım 2 — Native projeyi oluştur

Terminalde:

```bash
cd "/Users/ibrahimkara/cursor projelerım/lumi"
bash scripts/setup-native.sh
```

Bu komut:
- Store ikonlarını üretir (`resources/`)
- Capacitor Android + iOS projelerini oluşturur
- Web uygulamasını (`www/`) native kabuğa gömer

---

## Adım 3 — Gizlilik politikasını yayınla

Mağazalar **canlı bir URL** ister. `www/privacy.html` dosyasını şuraya yükle:

- GitHub Pages
- Kendi domainin
- Netlify / Vercel (ücretsiz)

Örnek URL: `https://senin-domain.com/lumi/privacy.html`

Play Console ve App Store Connect'e bu URL'yi yazacaksın.

---

## Google Play Store

### A) Android Studio ile imzalı AAB üret

```bash
npm run open:android
```

Android Studio'da:
1. **Build → Generate Signed Bundle / APK**
2. **Android App Bundle (AAB)** seç
3. Yeni keystore oluştur (şifreyi kaybetme!)
4. **release** build al
5. Çıktı: `android/app/release/app-release.aab`

### B) Play Console

1. https://play.google.com/console → Uygulama oluştur
2. **Uygulama adı:** LUMI
3. **Paket adı:** `com.lumi.social` (değiştirme)
4. Store listesi → `store/play-store-tr.txt` içeriğini kullan
5. **Grafikler:**
   - Uygulama ikonu: `resources/play-store/icon-512.png`
   - Ekran görüntüleri: telefondan 4–8 adet (1080×1920)
6. **Gizlilik politikası URL** ekle
7. **İçerik derecelendirmesi** anketi doldur
8. **AAB** dosyasını yükle → İncelemeye gönder

İlk inceleme genelde **1–7 gün** sürer.

---

## Apple App Store

### A) Xcode ile Archive

```bash
npm run open:ios
```

Xcode'da:
1. Sol üstten **Any iOS Device** seç
2. **Signing & Capabilities** → Apple Developer hesabınla team seç
3. Bundle ID: `com.lumi.social`
4. **Product → Archive**
5. **Distribute App → App Store Connect**

### B) App Store Connect

1. https://appstoreconnect.apple.com → Yeni uygulama
2. **Ad:** LUMI
3. **Bundle ID:** com.lumi.social
4. Açıklama → `store/app-store-tr.txt` kullan
5. **Gizlilik politikası URL**
6. **App Privacy** anketi (bu prototipte veri cihazda kalır → minimal toplama)
7. Ekran görüntüleri: iPhone 6.7" ve 6.5" zorunlu
8. **1024×1024 ikon:** `resources/ios/icon-1024.png`
9. Build seç → **Submit for Review**

Apple incelemesi **1–3 gün** (bazen daha uzun).

---

## Store listesi metinleri

- Play Store: `store/play-store-tr.txt`
- App Store: `store/app-store-tr.txt`

---

## Sık sorulan sorular

**Backend olmadan yayınlanır mı?**  
Evet — demo/prototip olarak yayınlanabilir. Açıklamada "demo" veya "beta" olduğunu belirt.

**Hesap açmadan test?**  
Android: APK'yı doğrudan yükle (internal testing).  
iOS: TestFlight (Developer hesabı gerekir).

**Paket adını değiştirmek istersem?**  
`capacitor.config.json` → `appId` alanını değiştir, `setup-native.sh` tekrar çalıştır.

---

## Hızlı komut özeti

```bash
npm run serve          # Web önizleme (www/)
bash scripts/setup-native.sh   # İlk kurulum
npm run open:android   # Play Store build
npm run open:ios       # App Store build
npm run build:android:release  # AAB (imza sonrası)
```

---

Sorun olursa: Android Studio / Xcode hata mesajını paylaş, birlikte çözeriz.
