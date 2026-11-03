from __future__ import annotations

import dash
from dash import Input, Output, State, callback, dcc, html, no_update

from src.data_loader import EVERY, names_for_iso, narrow, reviews, score_bounds
from src.figures import KIND_NAMES, category_bars, variety_bars, world_map
from src.summaries import count_sentence


dash.register_page(__name__, path="/", name="Explore the market", title="Explore the market · Wine Selection Assistant", order=0)

data = reviews()
iso_names = names_for_iso(data)
low_score, high_score = score_bounds(data)
EVERYTHING = dict(region=EVERY, scores=[low_score, high_score], budget=[0, 0], premium=False, budget_on=False)


def layout(**_):
    return html.Div(
        children=[
            html.Section(
                className="banner",
                children=[
                    html.P("Step 1 · Explore the market", className="kicker"),
                    html.H1("Where should a new wine buyer start looking?"),
                    html.P(id="explore-brief", className="brief"),
                ],
            ),
            html.Div(
                className="panel",
                children=[
                    html.Div(
                        className="panel-head",
                        children=[
                            html.P(id="explore-note", className="hint"),
                            dcc.RadioItems(
                                id="map-measure",
                                options=[{"label": "Number of reviews", "value": "count"}, {"label": "Average rating", "value": "rating"}],
                                value="count",
                                inline=True,
                                className="toggle",
                            ),
                        ],
                    ),
                    dcc.Graph(id="explore-map", config={"displayModeBar": False}, style={"height": "460px"}),
                ],
            ),
            html.Section(
                className="pair",
                children=[
                    html.Div(
                        className="panel",
                        children=[
                            html.P("Click a bar to choose that wine type. Click it again to show all types.", className="hint"),
                            dcc.Graph(id="explore-kinds", config={"displayModeBar": False}, style={"height": "360px"}),
                        ],
                    ),
                    html.Div(
                        className="panel",
                        children=[
                            html.P("Click a bar to choose that variety. Hover for its average rating and price.", className="hint"),
                            dcc.Graph(id="explore-grapes", config={"displayModeBar": False}, style={"height": "360px"}),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="next-step",
                children=[
                    html.P(id="explore-next"),
                    dcc.Link("Find wines in this selection →", href="/find", className="button"),
                ],
            ),
        ]
    )


def selection_label(country: str, kind: str, grape: str) -> str:
    if grape != EVERY:
        what = grape
    elif kind != EVERY:
        what = KIND_NAMES.get(kind, kind) + " wines"
    else:
        what = "All wines"
    return what + (f" from {country}" if country != EVERY else " from every country")


@callback(
    Output("explore-map", "figure"),
    Output("explore-kinds", "figure"),
    Output("explore-grapes", "figure"),
    Output("explore-brief", "children"),
    Output("explore-note", "children"),
    Output("explore-next", "children"),
    Input("origin-picker", "value"),
    Input("kind-picker", "value"),
    Input("grape-picker", "value"),
    Input("map-measure", "value"),
)
def refresh(country, kind, grape, measure):
    shared = dict(country=country, kind=kind, grape=grape, **EVERYTHING)
    map_rows = narrow(data, country_on=False, **shared)
    kind_rows = narrow(data, **{**shared, "kind": EVERY, "grape": EVERY})
    grape_rows = narrow(data, grape_on=False, **shared)
    picked = narrow(data, **shared)
    floor = 1 if measure == "count" else (20 if len(map_rows) > 5000 else 5)
    if country == EVERY:
        note = "Click a country to focus on it." + (" Gray countries have too few reviews to compare ratings." if measure == "rating" else "")
    else:
        note = f"{country} is outlined. Click it again to see every country, or click another one."
    return (
        world_map(map_rows, country, floor, measure),
        category_bars(kind_rows, kind),
        variety_bars(grape_rows, grape),
        count_sentence(picked, country),
        note,
        f"Your selection: {selection_label(country, kind, grape)} — {len(picked):,} reviews.",
    )


def _clicked(click, key: str):
    points = (click or {}).get("points") or []
    if not points:
        return None
    custom = points[0].get("customdata")
    if key == "location":
        return iso_names.get(points[0].get("location"))
    if isinstance(custom, (list, tuple)):
        return custom[0]
    return custom


@callback(
    Output("origin-picker", "value", allow_duplicate=True),
    Output("explore-map", "clickData"),
    Input("explore-map", "clickData"),
    State("origin-picker", "value"),
    prevent_initial_call=True,
)
def pick_country(click, current):
    found = _clicked(click, "location")
    if not found:
        return no_update, None
    # Clearing clickData lets the same country be clicked again to toggle it off.
    return (EVERY if found == current else found), None


@callback(
    Output("kind-picker", "value", allow_duplicate=True),
    Output("explore-kinds", "clickData"),
    Input("explore-kinds", "clickData"),
    State("kind-picker", "value"),
    prevent_initial_call=True,
)
def pick_kind(click, current):
    found = _clicked(click, "custom")
    if not found:
        return no_update, None
    return (EVERY if found == current else found), None


@callback(
    Output("grape-picker", "value", allow_duplicate=True),
    Output("explore-grapes", "clickData"),
    Input("explore-grapes", "clickData"),
    State("grape-picker", "value"),
    prevent_initial_call=True,
)
def pick_grape(click, current):
    found = _clicked(click, "custom")
    if not found:
        return no_update, None
    return (EVERY if found == current else found), None
