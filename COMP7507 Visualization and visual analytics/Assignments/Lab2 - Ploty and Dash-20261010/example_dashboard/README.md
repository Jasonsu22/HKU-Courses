# Wine Discovery Dashboard

Local-only single-page Dash app for exploring wines by country, variety, price, and rating.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Put `wine_category.csv` and `data/winemag-data-with-year.csv` under `data/`

## Run

```bash
python app.py
```

Then open the local URL shown by Dash in your browser.

## What the dashboard does

- Uses a country choropleth map as the primary selector.
- Provides filters for country, wine type, variety, price range, and rating range.
- Shows three linked visuals: country map, top varieties, and price versus rating.
- Displays summary KPIs for the active selection.

## Data notes

- `data/winemag-data-with-year.csv` contains the main wine review records.
- `data/wine_category.csv` maps varieties to broad wine categories.
- Year values outside a plausible range are ignored during cleaning.
