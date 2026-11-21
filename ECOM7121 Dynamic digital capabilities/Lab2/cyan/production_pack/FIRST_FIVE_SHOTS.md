# Household Inventory: script for shots 1–5 (0:00–0:50)

Every shot is 10 seconds, so the version-one voiceover, subtitles and top-left cards stay in sync.
Pictures: the start frame is drawn in ComfyUI (gpt-image-2.6) from the approved references, then animated with MiniMax-H3 (2K, 10 s).
Sound: Elio's English voiceover from version one. The characters don't speak in shots 1–5.

| # | Time | Picture | Camera | Voiceover (Elio) | Top-left card |
|---|---|---|---|---|---|
| 1 | 0:00–0:10 | 6:40 pm, a crowded MTR carriage. Mei holds the yellow pole and scrolls food pictures on her one phone. She pauses, tries to remember what's in her fridge, sighs, then taps a picture: takeaway again. | Very slow push-in, from medium shot to her face and phone | "Six-forty, on the MTR home to Kwun Tong. Mei can't remember what's in her fridge, so takeaway wins, again." | Household Inventory · Team Climbing Cat · Group Cyan (0.4 s); Illustrative scenario · Mei is fictional (3.0 s) |
| 2 | 0:10–0:20 | **Approved Clip 2, unchanged.** Mei opens the fridge; the camera glides in to the yoghurt hidden at the back, then pans to two clear bags of spinach on the counter; she realises, sighs and touches her forehead. | Slow glide in, then pan right | "At home, the fridge tells the real story: a yoghurt hidden at the back, and a second bag of spinach she didn't need." | none |
| 3 | 0:20–0:30 | Later that week, same kitchen. Mei holds the now-wilted bag of spinach and the unopened yoghurt, sighs and drops both into the pedal bin. | Gentle drift down with the food into the bin, then back up to her face | "By Friday, both go in the bin. Hong Kong throws away about three thousand tonnes of food a day, and two-thirds of it comes from homes like this one." | ~3,000 t of food waste a day · 67% from homes, EPD 2024 (23.0 s) |
| 4 | 0:30–0:40 | No people. The dining table: a handwritten shopping list and an open recipe book. Out of the window a plain white van drives past far below. The camera ends on the closed fridge in the open kitchen. | Hold on the table, rise to the window, pan right to the fridge | "Shopping lists remember what to buy. Food banks rescue surplus from shops. None of them knows what's in Mei's fridge." | none |
| 5 | 0:40–0:50 | Mei lays out her shopping on the counter (eggs, spinach, tomatoes, chicken, soy milk, receipt) and photographs it once. A cyan glowing line traces each item, then she smiles at her phone. | Slow push toward the counter | "Meet Household Inventory. Mei snaps her shopping, and the Sense Agent turns it into a list, flagging anything it isn't sure about." | Working prototype · fictional data · cyan-household.vercel.app (41.0 s) |

## Continuity rules (all shots)

- **Mei:** the approved A-pose sheet (low ponytail, cream blouse with rolled sleeves, grey trousers, dark belt), right-handed, only ever one phone.
- **Kitchen:** the approved kitchen. The fridge has its handle on the left edge and is hinged on the right. There's a blue checked tea towel, and the window looks out on lit housing towers.
- **Flat:** layout A. The kitchen opens straight onto the dining area, with no door between them.
- **Spinach:** flat, sealed, clear produce bags, as in Clip 2.
- **Look:** clean and tidy. No readable text, no logos and no watermark marks.

## Files

- **Video prompts:** `minimax/shots.json` (`shot01_final`, `shot03_final`, `shot04_final`, `shot05_final`).
- **Start-frame prompts:** `production_pack/asset_library/build_startframes_workflow.py`, which is the ComfyUI workflow "Cyan_Start_Frames".
- **Clips:**
  - `minimax/clips/shotNN_final.mp4` (2K, 10 s; MiniMax's own sound is not used);
  - `minimax/clips/shot02_h3b.mp4` (the approved Clip 2).
- **Review cut:** `minimax/review/Shots01-05_review.mp4` (all five joined at 1080p, with the version-one voiceover, subtitles and cards).

## Known notes

- **Shot 3:** for about 2 s, as she bends over the bin, the camera drifts down and her head leaves the frame.
- **Shot 4:** ends on the window with the van; it does not pan on to the fridge.
