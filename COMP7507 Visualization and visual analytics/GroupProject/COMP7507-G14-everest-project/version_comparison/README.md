# Before and after comparison

**Open `compare.html`** (double-click; no server or internet needed).

- **Left list:** every difference on the current page. Click one to jump to it in both versions.
- **Page:** switch between History, Routes and Your plan.
- **Show:** side by side, before only, or after only.
- **Differences:** turn the highlights on or off.

| Label | Meaning |
|---|---|
| **NEW** (green) | Not in the old version |
| **UPGRADED** (blue) | Same purpose, now does more |
| **FIXED** (orange) | Corrected a problem |
| **CHANGED** / **ISSUE** (old version only) | What was limited or wrong before |

## Contents

| Path | What it is |
|---|---|
| `compare.html` | Side-by-side viewer with highlights |
| `v1_before/index.html` | The app at baseline commit `8e6b16f`, runs alone |
| `v2_after/index.html` | The upgraded app, runs alone |
| `screens/` | Full-page screenshots of both versions, with highlights |
| `changes_data.js` | The list of differences and changed numbers |
| `client.js` | Draws the highlights inside each version |
| `build_snapshots.sh` | Rebuilds `v1_before` and `v2_after` after further edits |

The highlights exist only in these snapshot copies. The real app in `../everest-app/` has none, so it's safe to submit and demo.

To see every code change:

```bash
git diff 8e6b16f -- everest-app
```
