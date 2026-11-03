from __future__ import annotations

import pandas as pd
from dash import dcc, html

from src.data_loader import EVERY, badges, flavor_tags
from src.figures import KIND_NAMES
from src.text import highlight


MAX_COMPARE = 3


def _join(names: list[str]) -> str:
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


def featured_grape(frame: pd.DataFrame) -> str:
    if frame.empty:
        return ""
    grouped = frame.groupby("variety").agg(wine_count=("id", "count"), avg_points=("points", "mean"))
    eligible = grouped.loc[grouped["wine_count"] >= 20]
    pool = eligible if not eligible.empty else grouped
    sort_cols = ["avg_points", "wine_count"] if not eligible.empty else ["wine_count"]
    name = pool.sort_values(sort_cols, ascending=False).index[0]
    label = "Standout variety" if not eligible.empty else "Most listed variety"
    return f"{label}: {name}."


def count_sentence(frame: pd.DataFrame, country: str) -> str:
    if frame.empty:
        return "No wines match these filters."
    sentence = (
        f"{len(frame):,} reviews match, averaging {frame['points'].mean():.1f} points "
        f"at a typical price of ${frame['price'].median():,.0f}. {featured_grape(frame)}"
    )
    if country != EVERY:
        return f"In {country}, {sentence[0].lower()}{sentence[1:]}"
    leaders = frame["shown_country"].value_counts().head(3)
    if leaders.empty:
        return sentence
    names = _join(leaders.index.tolist())
    if names.startswith("United States"):
        names = f"The {names}"
    share = float(leaders.sum()) / len(frame)
    if share >= 0.5:
        verb = "accounts" if len(leaders) == 1 else "account"
        return sentence + f" {names} {verb} for most reviews in this slice."
    verb = "leads" if len(leaders) == 1 else "lead"
    return sentence + f" {names} {verb} this slice."


def star_button(wine_id: int, starred: list[int], where: str) -> html.Button:
    """`where` keeps ids unique when one wine shows in several places (card, review panel, similar list)."""
    picked = wine_id in starred
    return html.Button(
        "★ In compare list" if picked else "☆ Add to compare",
        id={"type": "star", "id": wine_id, "where": where},
        n_clicks=0,
        className="star on" if picked else "star",
        title="Click again to remove" if picked else f"Keep up to {MAX_COMPARE} wines to compare",
    )


def price_text(price: float) -> str:
    return "price n/a" if pd.isna(price) else f"${price:,.0f}"


def meta_line(row: pd.Series) -> str:
    vintage = "" if pd.isna(row["year"]) else f" · {row['year']}"
    return f"{row['shown_country']} · {row['province']} · {row['variety']}{vintage}"


def badge_row(row: pd.Series) -> html.Div:
    return html.Div([html.Span(name, className=f"badge {name.split()[0].lower()}") for name in badges(row)], className="badges")


def tag_row(row: pd.Series, limit: int = 6) -> html.Div:
    return html.Div([html.Span(name, className="tag") for name in flavor_tags(row)[:limit]], className="tags")


def wine_card(row: pd.Series, starred: list[int], where: str, peek: bool = True) -> html.Article:
    actions = [star_button(int(row["id"]), starred, where)]
    if peek:
        actions.insert(0, html.Button("Read review", id={"type": "peek", "id": int(row["id"])}, n_clicks=0, className="linkish"))
    return html.Article(
        className="wine-card",
        children=[
            html.H3(row["title"]),
            html.P(meta_line(row), className="quiet"),
            html.P([html.Strong(f"{row['points']:.0f} pts"), f" · {price_text(row['price'])}"], className="stats"),
            badge_row(row),
            tag_row(row),
            html.Div(actions, className="card-actions"),
        ],
    )


def review_block(row: pd.Series, flavors: list[str] | None = None) -> list:
    text = row["description"].strip() or "No review text is available for this wine."
    return [
        html.H3(row["title"]),
        html.P(meta_line(row), className="quiet"),
        html.P([html.Strong(f"{row['points']:.0f} pts"), f" · {price_text(row['price'])} · {KIND_NAMES.get(row['category'], row['category'])}"], className="stats"),
        badge_row(row),
        dcc.Markdown(highlight(text, flavors), className="review"),
        html.P(f"Winery: {row['winery']} · flavor words in bold", className="hint"),
    ]
