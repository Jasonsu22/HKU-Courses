"""Rebuilds Figure 2 (six-frame storyboard) from stills of the finished video.

    python3 make_storyboard.py <stills_dir> <out.png>
stills_dir holds f1.jpg .. f6.jpg (16:9 frames).
"""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1], sys.argv[2]
W, PAD, GAP = 2032, 22, 20
CW = (W - 2 * PAD - GAP) // 2          # card width
IH = int(CW * 9 / 16)                  # image height
TH = 260                               # text block height
CH = IH + TH
H = PAD * 2 + 3 * CH + 2 * GAP
BG, CARD, EDGE = (250, 245, 236), (255, 255, 255), (214, 200, 182)

F = "/System/Library/Fonts/HelveticaNeue.ttc"
title_f = ImageFont.truetype(F, 40, index=1)   # bold
body_f = ImageFont.truetype(F, 29, index=0)
badge_f = ImageFont.truetype(F, 23, index=1)

cards = [
    ("LOCAL PROBLEM", (178, 58, 50), "1  Local problem & user",
     "Mei, 29, Kwun Tong. Yoghurt hidden at the back, spinach bought twice; at 6:40 pm takeaway wins. "
     "HK landfills ~3,000 t of food waste a day, 67% from homes."),
    ("(a) SENSING", (24, 120, 120), "2  Signal received",
     "A photo of groceries and the receipt. The Sense Agent drafts items, labels and printed dates, flagging "
     "low-confidence rows. Nothing is saved until Mei checks it (D1)."),
    ("(b) SEIZING", (88, 128, 40), "3  Agents coordinate",
     "The Steward ranks spinach and eggs first; the Concierge drafts a 15-minute skillet using eligible stock "
     "only. Mei must approve before anything changes."),
    ("SURPRISE", (176, 128, 24), "4  Unexpected change",
     "Ka-ho has started avoiding dairy, and chicken left out overnight is marked “Check needed”. A saved "
     "yoghurt bowl and the chicken are now conflicts."),
    ("(d) STOP · ESCALATION", (178, 58, 50), "5  Verification & stop",
     "The Guardrail vetoes both; chat cannot override. “No safe meal” returns the decision to Mei, who "
     "inspects and bins the chicken. The app refuses to invent dates, override allergies or buy food."),
    ("OUTCOME · FEEDBACK", (110, 70, 150), "6  Outcome & learning",
     "Mei approves and cooks; stock updates in one transaction. 2 use-first items used, 1 takeaway avoided "
     "(illustrative). Cooked/tossed logs feed a weekly human review."),
]


def wrap(d, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur]


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
for i, (badge, col, title, body) in enumerate(cards):
    x = PAD + (i % 2) * (CW + GAP)
    y = PAD + (i // 2) * (CH + GAP)
    d.rounded_rectangle((x, y, x + CW, y + CH), 18, fill=CARD, outline=EDGE, width=3)
    fr = Image.open(f"{src}/f{i + 1}.jpg").convert("RGB")
    fr = fr.resize((CW - 6, int((CW - 6) * fr.height / fr.width)), Image.LANCZOS)
    fr = fr.crop((0, (fr.height - IH) // 2, fr.width, (fr.height - IH) // 2 + IH))
    mask = Image.new("L", fr.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, fr.width, fr.height + 30), 16, fill=255)
    img.paste(fr, (x + 3, y + 3), mask)
    bw = d.textlength(badge, font=badge_f) + 30
    d.rounded_rectangle((x + CW - bw - 16, y + 16, x + CW - 16, y + 56), 20, fill=col)
    d.text((x + CW - bw - 1, y + 23), badge, font=badge_f, fill="white")
    ty = y + IH + 22
    d.text((x + 22, ty), title, font=title_f, fill=col)
    for k, line in enumerate(wrap(d, body, body_f, CW - 60)):
        d.text((x + 22, ty + 58 + k * 40), line, font=body_f, fill=(40, 36, 32))
img.save(out)
print("saved", out, img.size)
