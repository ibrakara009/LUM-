#!/usr/bin/env python3
"""LUMI store icon & splash generator (Play Store + App Store)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "resources"
WWW = ROOT / "www" / "icons"

BG_TOP = (108, 92, 231)
BG_BOT = (0, 206, 201)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def gradient(size):
    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        c = lerp(BG_TOP, BG_BOT, y / max(size - 1, 1))
        for x in range(size):
            px[x, y] = c
    return img


def draw_icon(size, radius_ratio=0.22):
    img = gradient(size).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size, size), int(size * radius_ratio), fill=255)
    img.putalpha(mask)

    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", int(size * 0.17))
    except OSError:
        font = ImageFont.load_default()

    text = "LUMI"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - tw) / 2, (size - th) / 2 + size * 0.04), text, fill=(255, 255, 255, 255), font=font)
    return img


def save_png(path, img):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    print("  ", path.relative_to(ROOT))


def main():
    print("Generating LUMI store assets...")
    icon1024 = draw_icon(1024)
    save_png(RES / "icon.png", icon1024)

    splash = Image.new("RGB", (2732, 2732), (11, 13, 20))
    sicon = draw_icon(512)
    splash.paste(sicon, ((2732 - 512) // 2, (2732 - 512) // 2 - 80), sicon)
    save_png(RES / "splash.png", splash)

    android_sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    for folder, sz in android_sizes.items():
        save_png(RES / "android" / folder / "ic_launcher.png", draw_icon(sz, 0.2))
        save_png(RES / "android" / folder / "ic_launcher_round.png", draw_icon(sz, 0.2))

    save_png(RES / "play-store" / "icon-512.png", draw_icon(512))
    save_png(WWW / "icon-192.png", draw_icon(192))
    save_png(WWW / "icon-512.png", draw_icon(512))

    ios_sizes = [20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024]
    for sz in ios_sizes:
        name = f"icon-{sz}.png" if sz != 1024 else "icon-1024.png"
        save_png(RES / "ios" / name, draw_icon(sz, 0.22 if sz >= 100 else 0.18))

    print("Done.")


if __name__ == "__main__":
    main()
