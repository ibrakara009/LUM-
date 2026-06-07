#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== LUMI Native Setup (Play Store + App Store) ==="

if ! command -v node >/dev/null 2>&1; then
  echo ""
  echo "Node.js bulunamadi."
  echo "1) https://nodejs.org adresinden LTS surumu kur"
  echo "2) Terminali yeniden ac"
  echo "3) Bu scripti tekrar calistir: bash scripts/setup-native.sh"
  exit 1
fi

echo "[1/5] Ikonlar uretiliyor..."
python3 scripts/generate-icons.py

echo "[2/5] npm paketleri kuruluyor..."
npm install

echo "[3/5] Capacitor platformlari ekleniyor..."
if [ ! -d android ]; then npx cap add android; fi
if [ ! -d ios ] && [[ "$(uname)" == "Darwin" ]]; then npx cap add ios; fi

echo "[4/5] Web icerik senkronize ediliyor..."
npx cap sync

echo "[5/5] Store ikonlari uygulaniyor..."
if command -v npx >/dev/null 2>&1; then
  npx @capacitor/assets generate \
    --iconBackgroundColor "#6c5ce7" \
    --iconBackgroundColorDark "#0b0d14" \
    --splashBackgroundColor "#0b0d14" \
    --splashBackgroundColorDark "#0b0d14" 2>/dev/null || echo "(assets generate atlandi — resources/icon.png kullanilacak)"
fi

# Android launcher ikonlarini kopyala
if [ -d resources/android ] && [ -d android/app/src/main/res ]; then
  for d in resources/android/mipmap-*; do
    name=$(basename "$d")
    mkdir -p "android/app/src/main/res/$name"
    cp "$d/ic_launcher.png" "android/app/src/main/res/$name/ic_launcher.png" 2>/dev/null || true
    cp "$d/ic_launcher_round.png" "android/app/src/main/res/$name/ic_launcher_round.png" 2>/dev/null || true
  done
fi

echo ""
echo "=== Hazir ==="
echo "Android (Play Store): npm run open:android"
echo "iOS (App Store):      npm run open:ios"
echo "Detayli rehber:       MAGAZA.md"
