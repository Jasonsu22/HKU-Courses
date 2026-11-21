# Cyan (Climbing Cat · Group Cyan): Lab 2 redesign plan

Sources checked: the slide deck (16 slides), report draft A (`Cyan_ClimbingCat_ECOM7121_Lab2_Report.docx`, 1,484 words), report draft B (Sara's "Household Inventory Management (Cyan)", about 3,400 words), and the `cyan-household` repo (README plus `server/domain.js`, `server/ai.js` and `src/main.jsx`).
The earlier FoodBridge KT work (food rescue) is replaced in full.

## 1. One story everyone tells the same way

The **slides and draft A agree**, so they are the base. Draft B adds stronger evidence and tests, but it uses different agent names and a feature the app doesn't have.

| Topic | Slides / draft A | Draft B | Use in all deliverables |
|---|---|---|---|
| Persona | Mei, 29, Kwun Tong, lives with her partner | Mei in a shared flat with a flatmate | **Mei, 29, Kwun Tong, with her partner** |
| Agents | Sense, Steward, Kitchen Concierge, plus Guardrail (deterministic) | Register, Plan, Coordinate, plus D1/D2 | **Sense / Steward / Concierge / Guardrail**, mapped to the course labels (a)–(e) |
| Shared reminders to flatmates (B's Agent C) | — | Yes | **Drop.** The repo README says there are no scheduled reminders or shared accounts. |
| Failure case | Dairy allergy added; chicken left out overnight; Concierge proposes the chicken and the Guardrail vetoes it | Agent B tries to extend a use-by date | **Draft A's case**, plus B's "never extend a date" as a one-line refusal |
| Pilot | 20–30 households, 4 weeks (A); 30 households (slides) | 10 households | **30 households, 4 weeks** (slides) |
| Waste target | 15% (A); 20% or more (slides) | 25% | **20% or more versus baseline** (slides' success gate) |
| Who pays | HK$28/month tier plus NGO/estate licence | Free core, grants | **HK$28 tier + NGO/estate licence**, grants as seed |
| Evidence | 3,001 t/day food waste, 0.27 kg per person per day | **67% (1,996 t/day) from households**; honest evidence gap | Merge both |
| Alternatives | Four groups, in prose | Table: Nosh, Sidekick, OLIO, Too Good To Go, Food Wise HK | B's table, trimmed |
| Rules | PDPO, CFS food-recovery guide, CFS allergens | PCPD agentic-AI guidance (Aug 2026), Cap. 132W date labels | Merge both |
| Testing | Functional tests of the prototype | Synthetic test: 200 labels, 50 rogue attempts blocked | Both, **if the team confirms the synthetic test was really run** |

**Claims to soften unless the team can show them in the app:** photos deleted after extraction; data export and delete; a stop control that turns off AI suggestions; "founder is alerted"; saved plans invalidated the moment an allergy is added. The code checks again at cooking time, so word these as "proposed" where the code doesn't already do it.

## 2. Team report (Word, ≤ 1,500 words)

- Draft A's structure and wording, with B's evidence, alternatives table, PCPD agentic-AI guidance, date labels (Cap. 132W) and test results merged in. Word count checked.
- **Figure 1, new flowchart** (A4 portrait, matches the chosen style's palette):
  - inputs → Sense → Steward → Concierge → Guardrail → user approval;
  - each agent's inputs, what it may and may not do, and its handoffs;
  - (a) sensing, (b) seizing, (c) reconfiguring, (d) approval/stop, (e) feedback;
  - fallback route ("no safe meal" → inspect, discard or add food; AI off → manual entry);
  - stop control;
  - the rogue move (Concierge proposes the overnight chicken → veto → logged);
  - shared state in Neon.
- **Figure 2, six-frame storyboard:** stills taken from the video, in the same style, with captions from slide 9 (problem → signal → coordinate → surprise → stop → outcome and learning).
- References and AI-use declaration: one merged list. The declaration also mentions Google Vids and its AI-generated clips.

## 3. Video (about 2:50, 17 shots of 10 seconds, Google Vids)

Narrator: a warm Vids voice (tested first). Character descriptions stay word-for-word the same in every prompt, so Mei and her partner keep the same look.
Real app moments: screenshots of the live demo (scan review, inventory statuses, meal idea, veto/"Review required"), labelled *"Prototype – fictional household data"*.

| # | Picture | Voiceover (short) | Course point |
|---|---|---|---|
| 1 | 6:40 pm, the MTR: Mei weighs takeaway against cooking | "On the MTR home to Kwun Tong, Mei has no idea what's in her fridge, so takeaway wins again." | Local problem |
| 2 | Her fridge: yoghurt hidden behind leftovers, a second bag of spinach | "Yoghurt hidden at the back. A second bag of spinach she didn't need." | Problem |
| 3 | Food scraped into the bin; on-screen statistic | "Hong Kong landfills about three thousand tonnes of food a day, two-thirds of it from homes." | Evidence |
| 4 | Shopping list, recipe app, food-bank van: none of them sees her fridge | "Lists remember what to buy. Food banks rescue surplus. None knows what's in Mei's kitchen." | Alternatives / gap |
| 5 | Mei photographs her groceries and receipt | "Meet Cyan. The Sense Agent turns a photo into items, and flags what it isn't sure of." | (a) Sensing |
| 6 | App screen: draft with "Review required" | "Nothing is saved until Mei checks it, and Cyan never guesses a date." | D1 approval |
| 7 | Fridge items light up in "use first" order | "The Steward Agent ranks what to use first." | (b) Seizing |
| 8 | App screen: a 15-minute spinach-and-egg skillet | "The Concierge drafts dinner from what she already has." | (b) Seizing |
| 9 | Her partner: "I'm avoiding dairy now"; the chicken left out overnight | "Then things change: a new dairy allergy, and chicken left out overnight." | Surprise |
| 10 | The Guardrail stamps a veto on the yoghurt bowl and the chicken | "The Guardrail blocks both, and no chat message can argue past it." | (d) Stop |
| 11 | Concierge proposes the chicken again → "no safe meal"; Mei inspects and discards it | "Even when an agent tries, the decision goes back to Mei." | Rogue move / fallback |
| 12 | Mei approves the skillet and cooks; inventory updates | "Only after she approves does Cyan update the stock." | Human authority |
| 13 | Dinner on the table; one tap logs "cooked"; a weekly review card | "Two use-first items eaten, one takeaway avoided, and every outcome feeds next week's review." | (c) Reconfigure / (e) feedback |
| 14 | Households, a community centre / NGO, a housing estate | "Households save money; NGOs and estates get a low-cost education tool; a small subscription and licences pay for it." | Value / who pays |
| 15 | A padlocked data folder, a stop switch | "Minimal data under Hong Kong's privacy law, and a switch that stops the AI." | Rules / safeguards |
| 16 | Pilot calendar: 30 households, 4 weeks | "A four-week pilot measures waste, use-first meals and accuracy, and fails if people stop logging." | Measures / test |
| 17 | Kwun Tong at dusk; logo card | "Cyan. Good food. Less waste. By design." | Close |

On-screen notes (added as Vids Text, not drawn by the AI):
- "Illustrative scenario – Mei is fictional"
- "No organisation has endorsed this proposal"
- "Proposed pilot – not yet run"

## 4. Order of work

1. **You pick a style** (`style_options/style_options_overview.png`).
2. Report merge plus new flowchart. You review.
3. Two test clips in the chosen style, plus one voice sample. You approve.
4. All 17 clips, app screenshots, voiceover, text notes. Download as MP4.
5. Storyboard stills taken from the video, put into the report. Final check against the course brief and marking criteria.
6. Old FoodBridge files and the FoodBridge Vids project: delete only if you say so.
