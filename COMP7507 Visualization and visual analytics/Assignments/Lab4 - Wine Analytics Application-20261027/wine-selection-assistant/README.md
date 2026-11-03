# Wine Selection Assistant

Three-page Dash app (Lab 4) that helps a beginner go from the whole wine market to one bottle. Built on the Lab 2 `web_visualization` code.

## Setup

From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The review file and variety groups are already in `data/`.

## Run

```bash
python app.py
```

Open http://127.0.0.1:8050/. Start-up takes about 5 seconds while the reviews are tagged.

## Pages

1. **Explore the market** (`/`): world map (review count or average rating), wine types and top varieties. Click any of them to set your selection.
2. **Find my wine** (`/find`): pick an occasion, style and flavor notes. The value map shows wines that beat the typical rating for their price. Read reviews, then star up to three wines.
3. **Compare & decide** (`/compare`): starred wines side by side, a quick verdict, a flavor radar, a word cloud and similar wines.

The country / type / variety bar at the top is shared by all pages. The compare list is kept for the browser session.

## Code

- `app.py`: navigation, shared selection bar, star/unstar
- `pages/`: one file per page
- `src/data_loader.py`: cleaning, flavor tags, value score, filtering, similar wines
- `src/figures.py`: Plotly charts
- `src/text.py`: word cloud and review highlighting
- `src/summaries.py`: summary sentences and wine cards
