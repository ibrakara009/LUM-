#!/usr/bin/env bash
# Web dosyalarini www/ klasorune kopyala
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cp "$ROOT/index.html" "$ROOT/manifest.json" "$ROOT/sw.js" "$ROOT/www/" 2>/dev/null || true
cp -R "$ROOT/css" "$ROOT/js" "$ROOT/icons" "$ROOT/www/"
echo "www/ guncellendi."
