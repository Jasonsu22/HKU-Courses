# Find a wine

Local Dash app for choosing a wine by country, variety, price, and rating.

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

Open the local address Dash prints.

## What you can do

- Pick a country on the map. Countries with too few reviews stay gray.
- Filter by region, wine type, variety, price, and rating. Region waits until a country is selected.
- Bubbles place each variety by typical price and average rating. Click one to keep it.
- Copper price bars sit inside the budget. Pale bars show the ratings outside it.
- The list beside the map names up to eight matching bottles.
