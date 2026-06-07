# APK Nasıl Alınır?

Bilgisayarında Node/Java yoksa **GitHub üzerinden ücretsiz APK** üretebilirsin.

## Adımlar

### 1) GitHub hesabı aç
https://github.com

### 2) Yeni repo oluştur
- Repo adı: `lumi-app` (veya istediğin)
- Public veya Private

### 3) Projeyi yükle

Terminalde (sadece `lumi` klasörünü repo yap — en kolay yol):

```bash
cd "/Users/ibrahimkara/cursor projelerım/lumi"
git init
git add .
git commit -m "LUMI app"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADIN/lumi-app.git
git push -u origin main
```

`KULLANICI_ADIN` yerine kendi GitHub kullanıcı adını yaz.

### 4) APK'yı indir

1. GitHub repo → **Actions** sekmesi
2. **Build LUMI APK** workflow'unu seç
3. **Run workflow** → Run
4. 5–10 dk bekle (yeşil tik)
5. Sayfanın altında **Artifacts** → **LUMI-debug-apk** indir
6. ZIP'i aç → **app-debug.apk** dosyasını telefona at

### 5) Telefona kur

- APK'yı telefona gönder (AirDrop, Drive, USB)
- **Bilinmeyen kaynaklardan yükleme** izni ver
- APK'ya dokun → Kur

> Bu **debug APK**'dır — kendi telefonunda test için. Play Store'a yüklemek için imzalı **AAB** gerekir (MAGAZA.md).

---

## Bilgisayarında APK üretmek istersen

1. Node.js kur: https://nodejs.org  
2. Android Studio kur: https://developer.android.com/studio  
3. Terminal:
   ```bash
   cd "/Users/ibrahimkara/cursor projelerım/lumi"
   bash scripts/setup-native.sh
   cd android && ./gradlew assembleDebug
   ```
4. APK: `lumi/android/app/build/outputs/apk/debug/app-debug.apk`
