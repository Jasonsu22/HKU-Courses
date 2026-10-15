from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
WINE_DATA_PATH = DATA_DIR / "winemag-data-with-year.csv"
CATEGORY_DATA_PATH = DATA_DIR / "wine_category.csv"


def load_wine_data() -> pd.DataFrame:
    wine_df = pd.read_csv(WINE_DATA_PATH)
    category_df = pd.read_csv(CATEGORY_DATA_PATH)

    wine_df = wine_df.copy()
    category_df = category_df.copy()

    wine_df["country"] = wine_df["country"].fillna("Unknown").astype(str).str.strip()
    wine_df["variety"] = wine_df["variety"].fillna("Unknown").astype(str).str.strip()
    wine_df["description"] = wine_df["description"].fillna("").astype(str).str.strip()
    wine_df["designation"] = wine_df["designation"].fillna("").astype(str).str.strip()
    wine_df["province"] = wine_df["province"].fillna("Unknown").astype(str).str.strip()
    wine_df["region_1"] = wine_df["region_1"].fillna("Unknown").astype(str).str.strip()
    wine_df["region_2"] = wine_df["region_2"].fillna("Unknown").astype(str).str.strip()
    wine_df["winery"] = wine_df["winery"].fillna("Unknown").astype(str).str.strip()

    wine_df["points"] = pd.to_numeric(wine_df["points"], errors="coerce")
    wine_df["price"] = pd.to_numeric(wine_df["price"], errors="coerce")
    wine_df["year"] = pd.to_numeric(wine_df["year"], errors="coerce")
    wine_df.loc[(wine_df["year"] < 1900) | (wine_df["year"] > 2026), "year"] = pd.NA

    category_df["variety"] = category_df["variety"].astype(str).str.strip()
    category_df["category"] = category_df["category"].astype(str).str.strip().str.lower()

    merged = wine_df.merge(category_df, on="variety", how="left")
    merged["category"] = merged["category"].fillna("other")
    merged["country_display"] = merged["country"].replace({"US": "United States"})
    merged["country_display"] = merged["country_display"].astype(str).str.strip()
    merged.loc[merged["country_display"].isin(["", "nan", "None"]), "country_display"] = "Unknown"

    return merged


def get_country_options(dataframe: pd.DataFrame) -> list[dict[str, str]]:
    countries = (
        dataframe.loc[dataframe["country_display"] != "Unknown", "country_display"]
        .dropna()
        .value_counts()
        .index
        .tolist()
    )
    return [{"label": "All countries", "value": "__all__"}] + [
        {"label": country, "value": country} for country in countries
    ]


def get_variety_options(dataframe: pd.DataFrame, limit: int = 100) -> list[dict[str, str]]:
    varieties = dataframe["variety"].dropna().value_counts().head(limit).index.tolist()
    return [{"label": "All varieties", "value": "__all__"}] + [
        {"label": variety, "value": variety} for variety in varieties
    ]


def get_price_bounds(dataframe: pd.DataFrame) -> tuple[float, float]:
    prices = dataframe["price"].dropna()
    return float(prices.min()), float(prices.max())


def get_points_bounds(dataframe: pd.DataFrame) -> tuple[int, int]:
    points = dataframe["points"].dropna()
    return int(points.min()), int(points.max())
