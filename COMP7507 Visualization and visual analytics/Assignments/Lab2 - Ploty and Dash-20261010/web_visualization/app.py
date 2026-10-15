from __future__ import annotations

from functools import lru_cache

import pandas as pd
from dash import Dash, Input, Output, State, ctx, dcc, html

from src.data_loader import (
    EVERY,
    KIND_CHOICES,
    area_choices,
    grape_choices,
    load_reviews,
    names_for_iso,
    narrow,
    origin_choices,
    score_bounds,
)
from src.figures import band_table, budget_bars, grape_bubbles, price_sentence, world_map


@lru_cache(maxsize=1)
def reviews() -> pd.DataFrame:
    return load_reviews()


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
        f"{len(frame):,} wines match, averaging {frame['points'].mean():.1f} points "
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


def map_note(country: str, present: set[str]) -> str:
    if country == EVERY:
        return "Click a country. Gray countries have too few reviews to compare."
    if country not in present:
        return f"{country} is selected, but nothing there matches the other filters."
    return f"{country} is outlined. Click another country to switch."


def cellar(frame: pd.DataFrame):
    if frame.empty:
        return html.P("No bottles match these filters.", className="quiet")
    picks = frame.sort_values(["points", "price"], ascending=[False, True]).head(8)
    cards = []
    for row in picks.itertuples(index=False):
        cards.append(
            html.Article(
                className="bottle",
                children=[
                    html.H3(row.title),
                    html.P(f"{row.shown_country} · {row.variety} · {row.points:.0f} pts · ${row.price:,.0f}"),
                ],
            )
        )
    return html.Div(cards, className="bottle-stack")


def compose(country, region, kind, grape, budget, premium, scores) -> dict:
    data = reviews()
    shared = dict(country=country, region=region, kind=kind, grape=grape, scores=scores, budget=budget, premium=premium)
    map_rows = narrow(data, country_on=False, budget_on=False, grape_on=True, **shared)
    bubble_rows = narrow(data, country_on=True, budget_on=True, grape_on=False, **shared)
    price_rows = narrow(data, country_on=True, budget_on=False, grape_on=True, **shared)
    picked = narrow(data, country_on=True, budget_on=True, grape_on=True, **shared)
    floor = 20 if len(map_rows) > 5000 else 5
    present = set(map_rows.loc[map_rows["iso3"].notna(), "shown_country"])
    bands = band_table(price_rows, budget, premium)
    return {
        "map": world_map(map_rows, country, floor),
        "bubbles": grape_bubbles(bubble_rows, grape),
        "bands": budget_bars(price_rows, budget, premium),
        "counts": count_sentence(picked, country),
        "prices": price_sentence(bands),
        "note": map_note(country, present),
        "cellar": cellar(picked),
    }


def country_from_click(click, iso_names: dict[str, str]) -> str | None:
    points = (click or {}).get("points") or []
    if not points:
        return None
    point = points[0]
    if point.get("location") in iso_names:
        return iso_names[point["location"]]
    hover = point.get("hovertext")
    if hover in iso_names.values():
        return hover
    return None


def grape_from_click(click) -> str | None:
    points = (click or {}).get("points") or []
    if not points:
        return None
    point = points[0]
    custom = point.get("customdata")
    if isinstance(custom, (list, tuple)) and custom:
        return custom[0]
    if isinstance(custom, str):
        return custom
    return point.get("text")


data = reviews()
iso_names = names_for_iso(data)
low_score, high_score = score_bounds(data)
opening = compose(EVERY, EVERY, EVERY, EVERY, [4, 50], False, [low_score, high_score])

app = Dash(__name__, title="Find a wine")
server = app.server

app.layout = html.Div(
    className="shell",
    children=[
        html.Header(
            className="banner",
            children=[
                html.P("Wine finder", className="kicker"),
                html.H1("Which bottle fits the country, the grape, and the budget?"),
                html.P(id="brief-counts", className="brief", children=opening["counts"]),
                html.P(id="brief-prices", className="brief muted", children=opening["prices"]),
            ],
        ),
        html.Section(
            className="controls",
            children=[
                html.Div(
                    children=[
                        html.Label("Country"),
                        dcc.Dropdown(id="origin-picker", options=origin_choices(data), value=EVERY, clearable=False, searchable=True),
                        html.Button("Clear country", id="clear-origin", type="button", n_clicks=0, className="linkish"),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Region"),
                        dcc.Dropdown(id="area-picker", options=area_choices(data, EVERY), value=EVERY, clearable=False, searchable=True, disabled=True),
                        html.P("Available after a country is chosen.", className="hint"),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Wine type"),
                        dcc.Dropdown(id="kind-picker", options=KIND_CHOICES, value=EVERY, clearable=False),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Variety"),
                        dcc.Dropdown(id="grape-picker", options=grape_choices(data, EVERY), value=EVERY, clearable=False, searchable=True),
                    ]
                ),
                html.Div(
                    className="wide",
                    children=[
                        html.Label("Price"),
                        dcc.RangeSlider(
                            id="budget-slider",
                            min=4,
                            max=150,
                            step=1,
                            value=[4, 50],
                            marks={4: "$4", 50: "$50", 100: "$100", 150: "$150"},
                            tooltip={"placement": "bottom", "always_visible": False},
                            updatemode="mouseup",
                            allowCross=False,
                        ),
                        dcc.Checklist(
                            id="cellar-toggle",
                            options=[{"label": "Include wines over $150", "value": "cellar"}],
                            value=[],
                            className="checkline",
                        ),
                        html.P("Wines with no listed price stay hidden. 80–84 good · 85–89 very good · 90–94 excellent · 95–100 classic", className="hint"),
                    ],
                ),
                html.Div(
                    className="wide",
                    children=[
                        html.Label("Rating"),
                        dcc.RangeSlider(
                            id="score-slider",
                            min=low_score,
                            max=high_score,
                            step=1,
                            value=[low_score, high_score],
                            marks={80: "80", 90: "90", 100: "100"},
                            tooltip={"placement": "bottom", "always_visible": False},
                            updatemode="mouseup",
                            allowCross=False,
                        ),
                    ],
                ),
            ],
        ),
        html.Section(
            className="stage",
            children=[
                html.Div(
                    className="panel map-panel",
                    children=[
                        html.P(id="map-note", className="hint", children=opening["note"]),
                        dcc.Graph(id="world-map", figure=opening["map"], config={"displayModeBar": False}, style={"height": "460px"}),
                    ],
                ),
                html.Div(
                    className="panel cellar-panel",
                    children=[
                        html.H2("Bottles to open"),
                        html.P("Highest rating inside the budget. A tie goes to the lower price.", className="hint"),
                        html.Div(id="cellar-list", children=opening["cellar"]),
                    ],
                ),
            ],
        ),
        html.Section(
            className="pair",
            children=[
                html.Div(
                    className="panel",
                    children=[
                        html.P("Click a bubble to keep that variety. The other bubbles stay so you can switch.", className="hint"),
                        dcc.Graph(id="grape-bubbles", figure=opening["bubbles"], config={"displayModeBar": False}, style={"height": "460px"}),
                    ],
                ),
                html.Div(
                    className="panel",
                    children=[
                        html.P("Copper bars are inside the price slider. Pale bars are outside it.", className="hint"),
                        dcc.Graph(id="budget-bands", figure=opening["bands"], config={"displayModeBar": False}, style={"height": "460px"}),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("origin-picker", "value"),
    Input("world-map", "clickData"),
    Input("clear-origin", "n_clicks"),
    State("origin-picker", "value"),
    prevent_initial_call=True,
)
def choose_country(click, _clicks, current):
    if ctx.triggered_id == "clear-origin":
        return EVERY
    if ctx.triggered_id == "world-map":
        found = country_from_click(click, iso_names)
        if found:
            return found
    return current


@app.callback(
    Output("area-picker", "options"),
    Output("area-picker", "value"),
    Output("area-picker", "disabled"),
    Input("origin-picker", "value"),
    prevent_initial_call=True,
)
def choose_area(country):
    if country == EVERY:
        return area_choices(data, EVERY), EVERY, True
    return area_choices(data, country), EVERY, False


@app.callback(
    Output("grape-picker", "options"),
    Output("grape-picker", "value"),
    Input("kind-picker", "value"),
    Input("grape-bubbles", "clickData"),
    State("grape-picker", "value"),
    prevent_initial_call=True,
)
def choose_grape(kind, click, current):
    options = grape_choices(data, kind)
    allowed = {item["value"] for item in options}
    if ctx.triggered_id == "grape-bubbles":
        picked = grape_from_click(click)
        if picked in allowed:
            return options, picked
    if current not in allowed:
        return options, EVERY
    return options, current


@app.callback(
    Output("world-map", "figure"),
    Output("grape-bubbles", "figure"),
    Output("budget-bands", "figure"),
    Output("brief-counts", "children"),
    Output("brief-prices", "children"),
    Output("map-note", "children"),
    Output("cellar-list", "children"),
    Input("origin-picker", "value"),
    Input("area-picker", "value"),
    Input("kind-picker", "value"),
    Input("grape-picker", "value"),
    Input("budget-slider", "value"),
    Input("cellar-toggle", "value"),
    Input("score-slider", "value"),
    prevent_initial_call=True,
)
def refresh(country, region, kind, grape, budget, cellar_flag, scores):
    view = compose(
        country or EVERY,
        region or EVERY,
        kind or EVERY,
        grape or EVERY,
        budget,
        "cellar" in (cellar_flag or []),
        scores,
    )
    return view["map"], view["bubbles"], view["bands"], view["counts"], view["prices"], view["note"], view["cellar"]


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, dev_tools_ui=False)
