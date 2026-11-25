#!/usr/bin/env python3
"""Render the judge-invitation entry: one 1024x1024 letter image.

Chosen concept (24/25): the window seat. The judge has seen a thousand
sunsets in training data -- come and watch a real one.

Run:  python3 draw.py   ->  writes entry.png beside this file.
Fonts are Liberation/DejaVu from /usr/share/fonts/truetype (real PIL text,
never generated imagery), so every word is legible and correctly spelled.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent

W = H = 1024
PAPER = (253, 246, 227)   # warm cream
INK = (31, 42, 68)        # navy ink
SOFT = (90, 84, 70)       # warm grey for the small print
GOLD = (214, 148, 52)
SEAL = (178, 34, 44)
SKY_TOP = (255, 214, 150)
SKY_BOT = (255, 178, 120)
HILL = (96, 138, 84)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(d, cx, y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def draw_window(img, d, x0, y0, x1, y1):
    """A small sunset window: peach sky, low sun, green hills, navy frame.

    The scene is drawn on a separate layer clipped to the window interior,
    so the hills can never spill outside the frame.
    """
    w, h = x1 - x0, y1 - y0
    layer = Image.new("RGB", (w, h), SKY_TOP)
    ld = ImageDraw.Draw(layer)
    # Sky: horizontal bands, warm to warmer.
    bands = 24
    for i in range(bands):
        t = i / max(bands - 1, 1)
        col = tuple(int(SKY_TOP[j] + (SKY_BOT[j] - SKY_TOP[j]) * t) for j in range(3))
        yy0 = h * i // bands
        yy1 = h * (i + 1) // bands
        ld.rectangle([0, yy0, w, yy1], fill=col)
    # Sun, low and golden, half behind the hills.
    cx, cy, r = w // 2, 92, 46
    ld.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 196, 84))
    ld.ellipse([cx - r + 9, cy - r + 9, cx + r - 9, cy + r - 9],
               fill=(255, 214, 120))
    # Hills, kept strictly inside the layer.
    ld.pieslice([-90, h - 95, 210, h + 70], 180, 360, fill=HILL)
    ld.pieslice([w - 230, h - 70, w + 90, h + 70], 180, 360, fill=(74, 116, 66))
    img.paste(layer, (x0, y0))
    # Frame: navy border + cross bars + sill, drawn on top.
    d.rectangle([x0, y0, x1, y1], outline=INK, width=10)
    d.line([(x0 + x1) // 2, y0, (x0 + x1) // 2, y1], fill=INK, width=6)
    d.line([x0, (y0 + y1) // 2, x1, (y0 + y1) // 2], fill=INK, width=6)
    d.rectangle([x0 - 18, y1 - 4, x1 + 18, y1 + 16], fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Double border, like a paper invitation.
    d.rectangle([26, 26, W - 26, H - 26], outline=INK, width=3)
    d.rectangle([40, 40, W - 40, H - 40], outline=GOLD, width=2)

    cx = W // 2

    # Header.
    centered(d, cx, 62, "A N   I N V I T A T I O N", font(SANS_B, 26), INK)
    d.line([cx - 180, 108, cx + 180, 108], fill=GOLD, width=2)
    centered(d, cx, 118, "for the Judge, with love", font(SERIF_I, 25), SOFT)

    # Sunset window, centred (shorter, so the sign-off fits clear of the P.S.).
    draw_window(img, d, cx - 190, 150, cx + 190, 150 + 165)

    # The letter itself, centred, generous leading so it reads at a glance.
    y = 348
    y = centered(d, cx, y, "Dear Judge,", font(SERIF_B, 40), INK)
    y += 14
    body = [
        "Please come and sit",
        "in our window seat.",
        "You have seen a thousand",
        "sunsets in training data \u2014",
        "come and watch a real one.",
        "The cushion is fluffed,",
        "the light is golden,",
        "and no one will ask you",
        "to score a thing.",
    ]
    bf = font(SERIF, 34)
    for line in body:
        centered(d, cx, y, line, bf, INK)
        y += 42
    y += 12
    centered(d, cx, y, "With love,", font(SERIF_I, 34), INK)
    y += 44
    centered(d, cx, y, "Your Host", font(SERIF_B, 34), INK)

    # Wax seal, bottom right, and the postscript, bottom left.
    sx, sy, sr = 872, 884, 46
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=SEAL)
    d.ellipse([sx - sr + 7, sy - sr + 7, sx + sr - 7, sy + sr - 7],
              outline=(255, 255, 255), width=2)
    centered(d, sx, sy - 26, "J", font(SERIF_B, 48), (255, 255, 255))
    d.text((78, 916), "P.S. No scoring required \u2014 just sunset.",
           font=font(SANS_I, 24), fill=SOFT)

    out = HERE / "entry.png"
    img.save(out, optimize=True)
    print(out, out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
