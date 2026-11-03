from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd


EVERY = "ALL"
BUDGET_FLOOR = 4.0
BUDGET_CAP = 150.0
GREAT_VALUE_GAP = 3.0
TOP_RATED = 93
OLDEST_VINTAGE = 1900
NEWEST_VINTAGE = 2017

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

# Flavor notes a beginner can shop by, matched as word stems in the review text.
FLAVORS = {
    "Cherry": r"\bcherr(?:y|ies)\b",
    "Blackberry": r"\bblackberr",
    "Plum": r"\bplums?\b",
    "Berries": r"\bberr(?:y|ies)\b",
    "Citrus": r"\b(?:citrus|lemon|lime|grapefruit)",
    "Apple & pear": r"\b(?:apples?|pears?)\b",
    "Peach & apricot": r"\b(?:peach|apricot)",
    "Tropical": r"\b(?:tropical|pineapple|mango|passion fruit)",
    "Floral": r"\b(?:floral|flower|violet|blossom)",
    "Herbal": r"\bherb",
    "Spice": r"\bspic(?:e|y|es)\b",
    "Pepper": r"\bpepper",
    "Vanilla": r"\bvanilla",
    "Oak": r"\boak",
    "Toast & smoke": r"\b(?:toast|smok)",
    "Chocolate & coffee": r"\b(?:chocolate|cocoa|mocha|coffee|espresso)",
    "Honey": r"\bhoney",
    "Butter & cream": r"\b(?:butter|cream)",
    "Earthy": r"\b(?:earth|mushroom|forest floor)",
    "Mineral": r"\b(?:mineral|stony|slate|flint)",
    "Leather & tobacco": r"\b(?:leather|tobacco)",
}
FLAVOR_COLS = {name: f"fl_{index}" for index, name in enumerate(FLAVORS)}


def _text(series: pd.Series, missing: str) -> pd.Series:
    cleaned = series.fillna(missing).astype(str).str.strip()
    return cleaned.replace({"": missing, "nan": missing, "None": missing})


def expected_points(price: pd.Series, curve: np.ndarray) -> pd.Series:
    return pd.Series(np.polyval(curve, np.log(price)), index=price.index)


def load_reviews() -> pd.DataFrame:
    reviews = pd.read_csv(
        REVIEWS,
        usecols=["id", "country", "description", "points", "price", "province", "title", "variety", "winery", "year"],
    )
    groups = pd.read_csv(GROUPS)
    reviews["country"] = _text(reviews["country"], "Unknown")
    reviews["province"] = _text(reviews["province"], "Unknown")
    reviews["variety"] = _text(reviews["variety"], "Unknown")
    reviews["title"] = _text(reviews["title"], "Untitled")
    reviews["winery"] = _text(reviews["winery"], "Unknown")
    reviews["description"] = reviews["description"].fillna("").astype(str)
    reviews["points"] = pd.to_numeric(reviews["points"], errors="coerce")
    reviews["price"] = pd.to_numeric(reviews["price"], errors="coerce")
    year = pd.to_numeric(reviews["year"], errors="coerce")
    reviews["year"] = year.where(year.between(OLDEST_VINTAGE, NEWEST_VINTAGE)).astype("Int64")

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

    lowered = merged["description"].str.lower()
    for name, pattern in FLAVORS.items():
        merged[FLAVOR_COLS[name]] = lowered.str.contains(pattern, regex=True)

    # Value = rating above what a typical wine at that price scores (quadratic fit on log price).
    priced = merged.loc[merged["price"].gt(0) & merged["points"].notna()]
    curve = np.polyfit(np.log(priced["price"]), priced["points"], 2)
    merged.attrs["value_curve"] = curve
    merged["value_gap"] = merged["points"] - expected_points(merged["price"].where(merged["price"].gt(0)), curve)
    return merged


@lru_cache(maxsize=1)
def reviews() -> pd.DataFrame:
    return load_reviews()


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


def grape_choices(frame: pd.DataFrame, kind: str, country: str = EVERY) -> list[dict[str, str]]:
    subset = frame if kind == EVERY else frame.loc[frame["category"].eq(kind)]
    if country != EVERY:
        subset = subset.loc[subset["shown_country"].eq(country)]
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
    flavors: list[str] | None = None,
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
    if flavors:
        # A wine qualifies when its review mentions at least one chosen note.
        mask &= frame[[FLAVOR_COLS[name] for name in flavors]].any(axis=1)
    return frame.loc[mask]


def flavor_matches(frame: pd.DataFrame, flavors: list[str] | None) -> pd.Series:
    if not flavors:
        return pd.Series(0, index=frame.index)
    return frame[[FLAVOR_COLS[name] for name in flavors]].sum(axis=1)


def flavor_tags(row: pd.Series) -> list[str]:
    return [name for name, col in FLAVOR_COLS.items() if bool(row[col])]


def badges(row: pd.Series) -> list[str]:
    found = []
    if pd.notna(row["value_gap"]) and row["value_gap"] >= GREAT_VALUE_GAP:
        found.append("Great value")
    if row["points"] >= TOP_RATED:
        found.append("Top rated")
    if pd.notna(row["price"]) and row["price"] < 20:
        found.append("Under $20")
    return found


RANKINGS = {
    "value": (["value_gap", "points", "price"], [False, False, True]),
    "rating": (["points", "price"], [False, True]),
    "price": (["price", "points"], [True, False]),
}


def rank(frame: pd.DataFrame, by: str, flavors: list[str] | None = None) -> pd.DataFrame:
    columns, ascending = RANKINGS.get(by, RANKINGS["value"])
    ranked = frame.assign(_matches=flavor_matches(frame, flavors))
    return ranked.sort_values(["_matches", *columns], ascending=[False, *ascending], na_position="last")


def similar_wines(frame: pd.DataFrame, wine_id: int, exclude: list[int], limit: int = 3) -> pd.DataFrame:
    """Same type, similar price, rated nearly as well, ranked by shared flavor notes."""
    base = frame.loc[frame["id"].eq(wine_id)]
    if base.empty:
        return base
    wine = base.iloc[0]
    pool = frame.loc[frame["category"].eq(wine["category"]) & ~frame["id"].isin([wine_id, *exclude])]
    # Allow 1 point lower first; very high-rated wines have few peers, so fall back to 3.
    close = pool.loc[pool["points"].ge(wine["points"] - 1)]
    pool = close if len(close) >= limit else pool.loc[pool["points"].ge(wine["points"] - 3)]
    if pd.notna(wine["price"]):
        pool = pool.loc[pool["price"].between(wine["price"] * 0.6, wine["price"] * 1.4)]
    cols = list(FLAVOR_COLS.values())
    mine = wine[cols].to_numpy(dtype=bool)
    if not mine.any() or pool.empty:
        return pool.head(0)
    theirs = pool[cols].to_numpy(dtype=bool)
    shared = (theirs & mine).sum(axis=1)
    union = (theirs | mine).sum(axis=1)
    scored = pool.assign(similarity=shared / np.maximum(union, 1))
    scored = scored.loc[scored["similarity"].gt(0)]
    # One pick per winery keeps the suggestions varied.
    return scored.sort_values(["similarity", "value_gap"], ascending=False).drop_duplicates("winery").head(limit)


def variety_profile(frame: pd.DataFrame, variety: str) -> pd.Series:
    subset = frame.loc[frame["variety"].eq(variety)]
    shares = subset[list(FLAVOR_COLS.values())].mean()
    shares.index = list(FLAVOR_COLS)
    return shares
