# Household Inventory: explainer video production pack

**Team:** Climbing Cat · Group Cyan · ECOM7121 Innovation Lab 2
**Target length:** under 3:00 (current cut: 2:52 = 2.5 s photo opener + 17 shots)
**Format:** 16:9, 1080p, 24–30 fps

## Files in this folder

| File | Use |
|---|---|
| `team_photo.jpg` | Opening card, held 2.5 s, with the team title in the top-left |
| `style_refs/ref_mei_scene1.jpg` | **Main character and style reference.** Mei on the MTR. Attach to every shot that shows Mei. |
| `style_refs/ref_mei_scene6.jpg` | Mei indoors (kitchen light). Use for home scenes with Mei. |
| `style_refs/ref_kitchen_scene7.jpg` | Style-only reference with no people. Use for object and building shots. |
| `scene_refs/sceneNN.jpg` | A still from each finished shot of the current cut. Use as start frame or composition reference. |
| `subtitles.json` | Narration subtitles with start and end times (for the current cut) |

---

## 1. Global style (paste at the start of every prompt)

> Urban-sketcher animation: loose ink pen lines with visible rough pencil construction lines, soft uneven transparent watercolour washes, muted warm palette, textured cream paper grain, slightly imperfect hand-drawn look (not clean, not glossy, not 3D). Hong Kong setting. Gentle natural motion, one continuous shot, no cuts, no mirroring. No text, no letters, no logos, no readable signs or screens.

**Don't:** use clean vector or anime gloss, show dirty, damp or run-down interiors (homes are tidy and middle-class), add duplicate props, or let objects appear or disappear mid-shot.

## 2. Characters (use the same wording every time)

| Character | Description | Reference |
|---|---|---|
| **Mei** | 29-year-old Hong Kong woman with a youthful, smooth-skinned face (late twenties, no age lines), shoulder-length black hair in a low ponytail, cream button blouse, grey trousers, canvas tote bag. Right-handed. | `ref_mei_scene1.jpg` |
| **Ka-ho** | Mei's partner, 31-year-old Hong Kong man with short black hair, thin round glasses and a navy hoodie | `scene_refs/scene09.jpg` |
| **Volunteer (scene 14)** | Friendly woman in a yellow apron leading a community cooking class | `scene_refs/scene14.jpg` |

**Dialogue:** characters only speak **Cantonese**, quietly. The English narrator carries the story.

**Mix:** narrator at 100%. Clip audio at 100% but **ducked** (automatically lowered) under the narration, so Cantonese chatter and ambience are heard only in the gaps.

## 3. Continuity rules

- **Fridge:** a single fridge on the right of the frame, door hinged on the right, handle on the left. It opens to the right and stays there.
- **Cooking:** pan handle points left; Mei's right hand holds the wooden spatula from the right side and stays on the right.
- **Dining:** Mei holds chopsticks in her right hand. **No phones or screens** in this shot.
- **Lock:** one notebook and one small brass padlock, no keys, no switch. The hand closes the notebook and locks it.
- **Phone (scenes 1, 5, 6, 8, 11):** one phone only, held by Mei.

---

## 4. Shot list

Times are for the current cut, after the 2.5 s photo opener. Each shot is 10 s unless noted.

### Opener (0:00–0:02.5)
- **Visual:** `team_photo.jpg`, fitted on cream paper.
- **Card (top-left, pops in and out):** **Team Climbing Cat · Group Cyan** / *Household Inventory · ECOM7121 Innovation Lab 2*
- **Audio:** none.

### Shot 1: Problem: the commute (10 s)
- **Reference:** `ref_mei_scene1.jpg`
- **Prompt:** [global style] 6:40 pm inside a crowded Hong Kong MTR carriage heading to Kwun Tong. Mei [character text] holds the handrail and scrolls a food-delivery app on her phone, looking tired; she glances out at passing city lights and sighs. Slow push-in on her face.
- **Voiceover:** "Six-forty, on the MTR home to Kwun Tong. Mei can't remember what's in her fridge, so takeaway wins, again."
- **Cards:** "Household Inventory / Team Climbing Cat · Group Cyan" at 0.4 s; "Illustrative scenario · Mei is fictional" at 3 s.

### Shot 2: Problem: the fridge (10 s)
- **Reference:** `ref_mei_scene1.jpg` (start frame option: `scene_refs/scene02.jpg`)
- **Prompt:** [global style] ONE continuous static medium shot. Evening, a tidy small middle-class Hong Kong flat kitchen. A single narrow fridge stands on the right; door hinged on the RIGHT edge, handle on the LEFT. Mei stands on the left, pulls the handle; the door swings open to the right and stays there. Inside, leftover boxes hide a small yoghurt pot at the back; on the counter beside her lie two identical bags of spinach. She pauses, realising she bought spinach twice. Quiet.
- **Voiceover:** "At home, the fridge tells the real story: a yoghurt hidden at the back, and a second bag of spinach she didn't need."

### Shot 3: Problem: waste (10 s)
- **Reference:** `ref_mei_scene1.jpg`
- **Prompt:** [global style] Late evening in the same tidy kitchen. Mei (youthful, late twenties) gives a small disappointed sigh and drops a wilted bag of spinach and an unopened yoghurt pot into a small pedal bin. Through the window, lit housing towers at dusk. Quiet.
- **Voiceover:** "By Friday, both go in the bin. Hong Kong throws away about three thousand tonnes of food a day, and two-thirds of it comes from homes like this one."
- **Card:** "~3,000 t of food waste a day · 67% from homes / EPD, waste statistics for 2024" at about 23 s.

### Shot 4: Alternatives and the gap (10 s)
- **Reference:** `ref_kitchen_scene7.jpg` (style only)
- **Prompt:** [global style] No people. A slow pan around a clean, tidy, comfortable middle-class Hong Kong flat at dusk: a small dining table with a handwritten shopping list and an open recipe book, then out of the window to a neat street where a small white food-bank van drives past, ending on a closed white fridge in a well-kept kitchen corner. Clean painted walls, no stains or damp.
- **Voiceover:** "Shopping lists remember what to buy. Food banks rescue surplus from shops. None of them knows what's in Mei's fridge."

### Shot 5: Sense Agent (10 s)
- **Reference:** `ref_mei_scene6.jpg`
- **Prompt:** [global style] In the tidy kitchen, Mei unpacks fresh groceries and a paper receipt on the counter and photographs them with her phone. As she takes the photo, a soft cyan-teal glow traces the outline of each grocery item one by one, like a magic pencil line.
- **Voiceover:** "Meet Household Inventory. Mei snaps her shopping, and the Sense Agent turns it into a list, flagging anything it isn't sure about."
- **Card:** "Working prototype · fictional data / cyan-household.vercel.app" at about 41 s.

### Shot 6: Human check (D1) (10 s)
- **Reference:** `ref_mei_scene6.jpg`
- **Prompt:** [global style] Over-the-shoulder close-up of Mei holding her phone above the counter. The screen shows simple coloured cards with small food pictures and no words; one card glows amber. She turns a yoghurt pot to read its label, taps the amber card, and it turns cyan-teal with a small tick.
- **Voiceover:** "Nothing is saved until Mei checks it. The app never guesses an expiry date; if the label isn't clear, it asks."

### Shot 7: Steward Agent (10 s)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] View from inside an open, neatly organised small fridge looking out into the kitchen. One by one the food items light up with a soft cyan-teal glow in order: spinach and eggs brightest, then tomatoes, then the rest more faintly, as if quietly ranking what to use first.
- **Voiceover:** "The Steward Agent keeps track of every batch, and ranks what to use first."

### Shot 8: Kitchen Concierge (10 s)
- **Reference:** `ref_mei_scene6.jpg`
- **Prompt:** [global style] Mei sits on a small sofa in her tidy flat looking at her phone. Above it a dreamy watercolour vision blooms: a steaming spinach and egg skillet with a small clock showing fifteen minutes. She smiles, relieved.
- **Voiceover:** "The Kitchen Concierge drafts dinner from what she already has: a fifteen-minute spinach and egg skillet."

### Shot 9: Unexpected change (10 s)
- **Reference:** `ref_mei_scene6.jpg` + `scene_refs/scene09.jpg`
- **Prompt:** [global style] Medium-wide shot with BOTH characters fully in frame, side by side in the tidy kitchen: Mei and Ka-ho [character text]. Ka-ho holds up a milk carton and a yoghurt bowl and apologises to Mei, speaking only in Cantonese. The camera then drifts to the counter where a raw chicken pack has been left out overnight.
- **Voiceover:** "Then things change. Ka-ho has started avoiding dairy, and the chicken was left out overnight."
- **Card:** "Unexpected change" at about 81 s.

### Shot 10: Guardrail veto (10 s)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] Close-up on a kitchen counter with a yoghurt bowl and a raw chicken pack side by side. A translucent cyan-teal shield of light sweeps across and stops in front of both; they drain to grey pencil sketch while a bold red ink circle with a diagonal line is brushed over each. Calm, decisive.
- **Voiceover:** "The Guardrail blocks both. It re-checks every ingredient, and no chat message can talk its way past it."
- **Card:** "Guardrail veto" at about 91 s.

### Shot 11: No safe meal (10 s)
- **Reference:** `ref_mei_scene6.jpg`
- **Prompt:** [global style] Mei looks at her phone, which shows a small picture of a chicken glowing red. She frowns, picks up the raw chicken pack, inspects it closely, and drops it into the kitchen bin.
- **Voiceover:** "Even if an agent suggests the chicken again, the answer is: no safe meal. The decision goes back to Mei, and she bins it."

### Shot 12: Approve and cook (6.5 s, trimmed)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] ONE short locked-off close-up. A spinach and egg skillet in a black frying pan on a small gas stove; pan handle points LEFT. Mei's right hand in a cream sleeve holds a wooden spatula from the RIGHT and gives two quick stirs; the hand stays on the right. Steam rises.
- **Voiceover:** "Once Mei approves, she cooks, and only then does the app update the stock."

### Shot 13: Outcome and learning (10 s)
- **Reference:** `ref_mei_scene6.jpg` (use only for her face and the style)
- **Prompt:** [global style] Evening, the tidy dining corner of a clean middle-class Hong Kong flat (warm lamp, sofa and plant behind, window with city lights). Mei and Ka-ho sit side by side sharing a spinach and egg skillet with two bowls of rice. Mei holds chopsticks in her RIGHT hand throughout; they laugh and chat softly in Cantonese. NO phones, screens or devices anywhere.
- **Voiceover:** "Two use-first items eaten, one takeaway skipped. Every cooked or tossed tap feeds a weekly human review."

### Shot 14: Value and who pays (10 s)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] A gentle continuous move: the facade of a Kwun Tong public housing block with lit kitchen windows; then inside a bright community centre, a friendly volunteer leads a small cooking class for older residents and young parents around a table of vegetables. Everyone speaks only Cantonese.
- **Voiceover:** "Households waste less and save money. Community NGOs and estates reach families cheaply, and a small subscription plus partner licences pays the bills. No ads, no data sales."
- **Card:** "No organisation has endorsed this proposal / HK$28/month tier is illustrative".

### Shot 15: Privacy (10 s)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] ONE continuous static close-up on a clean wooden desk. A small open notebook with a small brass padlock and strap beside it. A single hand closes the notebook, wraps the strap over it and snaps the one padlock shut, then rests on it. Exactly one notebook and one padlock; no keys, no switches; nothing appears or disappears.
- **Voiceover (current):** "The app keeps only the data it needs under Hong Kong's privacy law, and a stop switch turns the AI off while the inventory stays readable."
- *Note: the picture no longer shows a switch. Consider: "...and one tap pauses the AI while the inventory stays readable."*

### Shot 16: Pilot and measures (10 s)
- **Reference:** `ref_kitchen_scene7.jpg`
- **Prompt:** [global style] Top-down view of a hand-drawn watercolour map of the Kwun Tong neighbourhood on a table. Small house-shaped markers light up one by one with a soft cyan-teal glow, while the corner of a paper wall calendar flips through four weeks.
- **Voiceover:** "A four-week pilot with thirty households will measure food wasted, use-first meals and accuracy. If people stop logging, the idea fails."
- **Card:** "Proposed pilot · not yet run / Targets are hypotheses".

### Shot 17: Close (10 s)
- **Reference:** `ref_mei_scene1.jpg`
- **Prompt:** [global style] Golden dusk. Mei smiles at the open window of her small tidy flat holding a cup of tea. The camera slowly pulls back and rises above the housing estate, revealing hundreds of warm lit windows, with soft cyan-teal glints in some kitchens.
- **Voiceover:** "Household Inventory. Good food. Less waste. By design."
- **Card:** "Household Inventory / Team Climbing Cat · Group Cyan · ECOM7121" (held 2.5 s).

---

## 5. Voice and on-screen text

- **Narrator:** warm, friendly, slightly low English voice (in Vids it was "Elio"), calm pace of about 150 words per minute.
- **Subtitles:** narration only, one full sentence per line, small (about 25 px at 1080p), white on a soft dark strip, bottom centre. Timings are in `subtitles.json` (shift them if your shot lengths change).
- **Cards:** top-left, cream card with a teal bar, bold title plus a small teal subtitle, pop in then out after 1.2–1.5 s.
- **Keep the AI-disclosure mark** if your tool adds one, and mention the tool in the report's AI-use declaration.
