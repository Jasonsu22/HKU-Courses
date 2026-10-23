# COMP7503 Exam Prep (Lectures 1–5)

Revision material for the COMP7503 Multimedia Technologies quiz (Lectures 1–5).

| File | What it is |
|---|---|
| [COMP7503-Cheat-Sheet-A4-Duplex-English.pdf](COMP7503-Cheat-Sheet-A4-Duplex-English.pdf) | One A4 sheet, both sides: slide definitions with one example each, key comparisons, past-paper answer cues. Print at 100%, duplex long-edge. |
| [COMP7503-Cheat-Sheet-A4-Duplex-Bilingual.pdf](COMP7503-Cheat-Sheet-A4-Duplex-Bilingual.pdf) | Same sheet with Chinese glosses for key terms (英文 + 中文术语). |
| [Study-Guide-English.md](Study-Guide-English.md) | Full English revision guide for S01–S05. |
| [Study-Guide.md](Study-Guide.md) | 完整中文复习讲义（S01–S05）。 |
| [cheat-sheet-src/](cheat-sheet-src/) | Cheat-sheet source text and build script. |

## Rebuilding the cheat sheets

Edit the `cheat-en-*.md` files in `cheat-sheet-src/`, then run (needs `reportlab` and `pypdf`; uses the macOS STHeiti font for Chinese):

```bash
python3 cheat-sheet-src/build_duplex_en.py
```

Each line starts with a `**Label:**`. Terms followed by a Chinese gloss, e.g. `hysteresis (迟滞)`, are bolded and underlined automatically; the English build strips the glosses.

## Not in this repository

Past exam papers, the review packs built from them, class recording transcripts, and shared notes from classmates stay local only (they are restricted or belong to others).

These are revision notes, not official answers; the lecture slides and course announcements take precedence.
