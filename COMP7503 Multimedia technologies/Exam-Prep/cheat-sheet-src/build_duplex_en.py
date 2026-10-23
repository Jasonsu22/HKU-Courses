from pathlib import Path
import json
import re
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
FONT = 'Helvetica'
FONT_BOLD = 'Helvetica-Bold'
pdfmetrics.registerFontFamily(FONT, normal='Helvetica', bold='Helvetica-Bold',
                              italic='Helvetica-Oblique', boldItalic='Helvetica-BoldOblique')
pdfmetrics.registerFont(TTFont('CJK', '/System/Library/Fonts/STHeiti Light.ttc', subfontIndex=0))
CJK_RUN = re.compile(r'[←-⇿　-〿㐀-鿿＀-￯]+')
# A Chinese gloss is a (half- or full-width) parenthesis group containing CJK text.
CJK_GLOSS = re.compile(r' ?[(（][^()（）]*[㐀-鿿][^()（）]*[)）]')
W, H = A4
MARGIN, GAP = 14, 8
COL_W = (W - MARGIN * 2 - GAP * 2) / 3
TOP, BOTTOM = H - 14, 14


def normalize(text):
    return text.replace('2ⁿ', '2^n').translate(str.maketrans({
        'ᵢ': 'i', 'ⱼ': 'j', '₀': '0', '₁': '1', '₈': '8',
        'ⁿ': 'n', '–': '-', '—': '-', '−': '-',
    }))


def blocks(text):
    result = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        is_heading = line.startswith('### ')
        if is_heading:
            line = line[4:]
        # **Label:** at the start of a line becomes a coloured bold label
        line = re.sub(r'\*\*(.+?)\*\*', LABEL_OPEN + r'\1' + LABEL_CLOSE, line)
        line = normalize(line.replace('`', ''))
        result.append((is_heading, line))
    return result


def layout(source, size):
    normal = ParagraphStyle('body', fontName=FONT, fontSize=size, leading=size * 1.12,
                            wordWrap='LTR', textColor='#17251f', splitLongWords=True)
    heading = ParagraphStyle('head', parent=normal, fontName=FONT_BOLD, fontSize=size + .65,
                             leading=(size + .65) * 1.18, textColor='#174d3a')
    plan, col, y = [], 0, TOP
    for is_heading, text in source:
        markup = CJK_RUN.sub(lambda m: f'<font name="CJK" color="#7a3b12">{m.group()}</font>', escape(text))
        markup = markup.replace(KEY_OPEN, '<b><u>').replace(KEY_CLOSE, '</u></b>')
        markup = re.sub(r'\be\.g\.', '<i>e.g.</i>', markup)
        markup = markup.replace(LABEL_OPEN, '<b><font color="#0f4c75">').replace(LABEL_CLOSE, '</font></b>')
        p = Paragraph(markup, heading if is_heading else normal)
        if is_heading and y - BOTTOM < heading.leading + normal.leading * 2 + 3:
            col, y = col + 1, TOP
        while True:
            # Six columns flow continuously: 0-2 on the front, 3-5 on the back.
            if col > 5:
                return None
            pw, ph = p.wrap(COL_W, TOP - BOTTOM)
            available = y - BOTTOM
            if ph <= available + .001:
                plan.append((p, col, MARGIN + col % 3 * (COL_W + GAP), y - ph, ph))
                y -= ph + (2.0 if is_heading else 0.5)
                break
            split = p.split(COL_W, available)
            if split and not is_heading:
                first = split[0]
                fw, fh = first.wrap(COL_W, available)
                plan.append((first, col, MARGIN + col % 3 * (COL_W + GAP), y - fh, fh))
                if len(split) == 1:
                    break
                p = split[1]
            col, y = col + 1, TOP
    return plan


draft = ROOT / 'cheat-sheet-src'
body = '\n\n'.join((draft / n).read_text() for n in [
    'cheat-en-a-foundations.md', 'cheat-en-a-applications.md',
    'cheat-en-b-sensors-audio.md', 'cheat-en-b-light.md', 'cheat-en-c-comparisons.md'])

# Key terms are the ones carrying a Chinese gloss; mark them (bold + underline in
# both versions) before the English build strips the glosses.
KEY_OPEN, KEY_CLOSE = '\x01', '\x02'
LABEL_OPEN, LABEL_CLOSE = '\x03', '\x04'
KEY_TERMS = json.loads((draft / 'key_terms.json').read_text())
KEY_RE = re.compile(r'(?<![\w-])(' + '|'.join(map(re.escape, KEY_TERMS)) + r')(?= ?\([^()]*[㐀-鿿])')
body = KEY_RE.sub(lambda m: KEY_OPEN + m.group(1) + KEY_CLOSE, body)


def build(target, title, bilingual):
  c = canvas.Canvas(str(target), pagesize=A4)
  c.setTitle(title)
  c.setAuthor('COMP7503 study notes')
  source = blocks(body if bilingual else CJK_GLOSS.sub('', body))
  plan = None
  for size in [round(8.2 - .05 * i, 2) for i in range(69)]:
    plan = layout(source, size)
    if plan:
      break
  if not plan:
    raise ValueError('Content does not fit one A4 sheet')
  choices = {'font_pt': size, 'paragraphs': len(source)}
  for page_number, label in enumerate([
    'FRONT | Lectures 1–3 (continues overleaf)',
    'BACK | Lectures 4–5 + past-paper answer cues',
  ], 1):
    c.setStrokeColorRGB(.82, .86, .83)
    for separator in [MARGIN + COL_W + GAP / 2, MARGIN + COL_W * 2 + GAP * 1.5]:
        c.line(separator, BOTTOM + 1, separator, TOP)
    for paragraph, col, x, y, height in plan:
      if col // 3 == page_number - 1:
        paragraph.drawOn(c, x, y)
    c.showPage()
  c.save()
  r = PdfReader(target)
  assert len(r.pages) == 2
  for page in r.pages:
    assert abs(float(page.mediabox.width) - W) < .1
    assert abs(float(page.mediabox.height) - H) < .1
  print({'pdf': str(target), 'pages': len(r.pages), 'layout': choices,
         'extracted_characters': [len(p.extract_text() or '') for p in r.pages]})


build(ROOT / 'COMP7503-Cheat-Sheet-A4-Duplex-English.pdf',
      'COMP7503 · Lectures 1–5 · A4 Duplex Cheat Sheet (English)', bilingual=False)
build(ROOT / 'COMP7503-Cheat-Sheet-A4-Duplex-Bilingual.pdf',
      'COMP7503 · Lectures 1–5 · A4 Duplex Cheat Sheet (English + 中文)', bilingual=True)
