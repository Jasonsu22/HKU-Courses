from __future__ import annotations

from pathlib import Path

import pandas as pd


EVERY = "ALL"
BUDGET_FLOOR = 4.0
BUDGET_CAP = 150.0

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "data" / "winemag-data-with-year.csv"
GROUPS = ROOT / "data" / "wine_category.csv"

ISO3 = {
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Australia": "AUS",
    "Austria": "AUT",
    "Bosnia and Herzegovina": "BIH",
    "Brazil": "BRA",
    "Bulgaria": "BGR",
    "Canada": "CAN",
    "Chile": "CHL",
    "China": "CHN",
    "Croatia": "HRV",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Egypt": "EGY",
    "England": "GBR",
    "France": "FRA",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Greece": "GRC",
    "Hungary": "HUN",
    "India": "IND",
    "Israel": "ISR",
    "Italy": "ITA",
    "Lebanon": "LBN",
    "Luxembourg": "LUX",
    "Macedonia": "MKD",
    "Mexico": "MEX",
    "Moldova": "MDA",
    "Morocco": "MAR",
    "New Zealand": "NZL",
    "Peru": "PER",
    "Portugal": "PRT",
    "Romania": "ROU",
    "Serbia": "SRB",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "South Africa": "ZAF",
    "Spain": "ESP",
    "Switzerland": "CHE",
    "Turkey": "TUR",
    "US": "USA",
    "Ukraine": "UKR",
    "Uruguay": "URY",
}

SHOWN_AS = {"US": "United States"}

KIND_CHOICES = [
    {"label": "All types", "value": EVERY},
    {"label": "Red", "value": "red"},
    {"label": "White", "value": "white"},
    {"label": "Rosé", "value": "rose"},
    {"label": "Sparkling", "value": "sparkling"},
    {"label": "Dessert", "value": "dessert"},
    {"label": "Other", "value": "other"},
]


def _text(series: pd.Series, missing: str) -> pd.Series:
    cleaned = series.fillna(missing).astype(str).str.strip()
    return cleaned.replace({"": missing, "nan": missing, "None": missing})


def load_reviews() -> pd.DataFrame:
    reviews = pd.read_csv(REVIEWS, usecols=["id", "country", "points", "price", "province", "title", "variety"])
    groups = pd.read_csv(GROUPS)
    reviews["country"] = _text(reviews["country"], "Unknown")
    reviews["province"] = _text(reviews["province"], "Unknown")
    reviews["variety"] = _text(reviews["variety"], "Unknown")
    reviews["title"] = _text(reviews["title"], "Untitled")
    reviews["points"] = pd.to_numeric(reviews["points"], errors="coerce")
    reviews["price"] = pd.to_numeric(reviews["price"], errors="coerce")

    groups["variety"] = groups["variety"].astype(str).str.strip()
    groups["category"] = groups["category"].astype(str).str.strip().str.lower()
    groups = groups.drop_duplicates("variety")

    merged = reviews.merge(groups, on="variety", how="left")
    merged["category"] = merged["category"].fillna("other")
    merged["shown_country"] = merged["country"].map(SHOWN_AS).fillna(merged["country"])
    merged["iso3"] = merged["country"].map(ISO3)

    known = set(merged.loc[merged["country"] != "Unknown", "country"].unique())
    missing = known - set(ISO3)
    if missing:
        raise ValueError(f"Countries without an ISO-3 code: {sorted(missing)}")
    return merged


def names_for_iso(frame: pd.DataFrame) -> dict[str, str]:
    pairs = frame.loc[frame["iso3"].notna(), ["iso3", "shown_country"]].drop_duplicates()
    return dict(zip(pairs["iso3"], pairs["shown_country"]))


def origin_choices(frame: pd.DataFrame) -> list[dict[str, str]]:
    names = frame.loc[frame["shown_country"] != "Unknown", "shown_country"].value_counts().index.tolist()
    return [{"label": "All countries", "value": EVERY}] + [{"label": name, "value": name} for name in names]


def area_choices(frame: pd.DataFrame, country: str) -> list[dict[str, str]]:
    if country == EVERY:
        return [{"label": "All regions", "value": EVERY}]
    counts = frame.loc[frame["shown_country"].eq(country), "province"].value_counts()
    names = [name for name in counts.index.tolist() if name != "Unknown"]
    if "Unknown" in counts.index:
        names.append("Unknown")
    return [{"label": "All regions", "value": EVERY}] + [{"label": name, "value": name} for name in names]


def grape_choices(frame: pd.DataFrame, kind: str) -> list[dict[str, str]]:
    subset = frame if kind == EVERY else frame.loc[frame["category"].eq(kind)]
    names = [name for name in subset["variety"].value_counts().index.tolist() if name != "Unknown"]
    return [{"label": "All varieties", "value": EVERY}] + [{"label": name, "value": name} for name in names]


def score_bounds(frame: pd.DataFrame) -> tuple[int, int]:
    scores = frame["points"].dropna()
    return int(scores.min()), int(scores.max())


def usable_region(frame: pd.DataFrame, country: str, region: str) -> str:
    if country == EVERY or region == EVERY:
        return EVERY
    found = (frame["shown_country"].eq(country) & frame["province"].eq(region)).any()
    return region if found else EVERY


def narrow(
    frame: pd.DataFrame,
    *,
    country: str,
    region: str,
    kind: str,
    grape: str,
    scores: list[float] | tuple[float, float],
    budget: list[float] | tuple[float, float],
    premium: bool,
    country_on: bool = True,
    budget_on: bool = True,
    grape_on: bool = True,
) -> pd.DataFrame:
    region = usable_region(frame, country, region)
    mask = frame["points"].between(scores[0], scores[1], inclusive="both")
    if kind != EVERY:
        mask &= frame["category"].eq(kind)
    if grape_on and grape != EVERY:
        mask &= frame["variety"].eq(grape)
    if country_on and country != EVERY:
        mask &= frame["shown_country"].eq(country)
    if region != EVERY:
        mask &= frame["province"].eq(region)
    if budget_on:
        low, high = budget
        priced = frame["price"].between(low, high, inclusive="both")
        if premium:
            priced = priced | frame["price"].gt(BUDGET_CAP)
        mask &= priced
    return frame.loc[mask]
