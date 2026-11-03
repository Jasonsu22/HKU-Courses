from __future__ import annotations

import math

import dash
import pandas as pd
from dash import ALL, Input, Output, State, callback, ctx, dash_table, dcc, html, no_update

from src.data_loader import (
    BUDGET_CAP,
    EVERY,
    FLAVORS,
    GREAT_VALUE_GAP,
    area_choices,
    narrow,
    rank,
    reviews,
    score_bounds,
)
from src.figures import value_map
from src.summaries import review_block, star_button, wine_card


dash.register_page(__name__, path="/find", name="Find my wine", title="Find my wine · Wine Selection Assistant", order=1)

data = reviews()
curve = data.attrs["value_curve"]
low_score, high_score = score_bounds(data)
FULL_BUDGET = [4, BUDGET_CAP]
PAGE_SIZE = 10
SHORTLIST = 6
VALUE_SAMPLE = 2500

OCCASIONS = {
    "any": ("Any occasion", FULL_BUDGET),
    "everyday": ("Everyday · under $20", [4, 20]),
    "dinner": ("Dinner with friends · $15–40", [15, 40]),
    "gift": ("Special gift · $40–150", [40, BUDGET_CAP]),
}
# Each style picks a wine type and the notes reviewers use for it.
STYLES = {
    "any": ("Any style", EVERY, []),
    "crisp": ("Light & crisp", "white", ["Citrus", "Apple & pear", "Mineral"]),
    "fruity": ("Fruity & smooth", "red", ["Cherry", "Berries", "Plum"]),
    "bold": ("Rich & bold", "red", ["Blackberry", "Chocolate & coffee", "Leather & tobacco", "Oak"]),
    "sweet": ("Sweet", "dessert", ["Honey", "Peach & apricot"]),
    "bubbly": ("Bubbly", "sparkling", ["Apple & pear", "Citrus", "Toast & smoke"]),
}
RANK_CHOICES = [
    {"label": "Best value", "value": "value"},
    {"label": "Highest rated", "value": "rating"},
    {"label": "Lowest price", "value": "price"},
]
COLUMNS = [
    {"name": "Wine", "id": "title"},
    {"name": "Country", "id": "shown_country"},
    {"name": "Variety", "id": "variety"},
    {"name": "Vintage", "id": "year", "type": "numeric"},
    {"name": "Price ($)", "id": "price", "type": "numeric"},
    {"name": "Rating", "id": "points", "type": "numeric"},
    {"name": "vs. typical", "id": "value_gap", "type": "numeric"},
]
FILTERS = [
    Input("origin-picker", "value"),
    Input("area-picker", "value"),
    Input("kind-picker", "value"),
    Input("grape-picker", "value"),
    Input("budget-slider", "value"),
    Input("cellar-toggle", "value"),
    Input("score-slider", "value"),
    Input("flavor-picker", "value"),
    Input("rank-picker", "value"),
]


def chips(component_id: str, choices: dict, value: str) -> dcc.RadioItems:
    return dcc.RadioItems(
        id=component_id,
        options=[{"label": label, "value": key} for key, (label, *_rest) in choices.items()],
        value=value,
        inline=True,
        className="chips",
    )


def layout(**_):
    return html.Div(
        children=[
            dcc.Store(id="spot"),
            html.Section(
                className="banner",
                children=[
                    html.P("Step 2 · Find my wine", className="kicker"),
                    html.H1("What fits your taste and your budget?"),
                    html.P(id="find-brief", className="brief"),
                ],
            ),
            html.Section(
                className="panel taste",
                children=[
                    html.H2("Start with what you like"),
                    html.Div(className="taste-row", children=[html.Label("Occasion"), chips("occasion-picker", OCCASIONS, "any")]),
                    html.Div(className="taste-row", children=[html.Label("Style"), chips("style-picker", STYLES, "any")]),
                    html.Div(
                        className="taste-row",
                        children=[
                            html.Label("Notes you enjoy"),
                            dcc.Checklist(id="flavor-picker", options=list(FLAVORS), value=[], inline=True, className="chips"),
                        ],
                    ),
                    html.P("A wine qualifies when its review mentions at least one chosen note; wines matching more notes rank first.", className="hint"),
                    html.Details(
                        className="more",
                        children=[
                            html.Summary("More filters: region, exact price, rating"),
                            html.Div(
                                className="controls inner",
                                children=[
                                    html.Div(
                                        children=[
                                            html.Label("Region"),
                                            dcc.Dropdown(id="area-picker", options=area_choices(data, EVERY), value=EVERY, clearable=False, searchable=True),
                                            html.P(id="area-hint", className="hint"),
                                        ]
                                    ),
                                    html.Div(
                                        className="span3",
                                        children=[
                                            html.Label("Price"),
                                            dcc.RangeSlider(
                                                id="budget-slider",
                                                min=4,
                                                max=BUDGET_CAP,
                                                step=1,
                                                value=FULL_BUDGET,
                                                marks={4: "$4", 20: "$20", 40: "$40", 100: "$100", 150: "$150"},
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
                                                marks={80: "80", 85: "85", 90: "90", 95: "95", 100: "100"},
                                                tooltip={"placement": "bottom", "always_visible": False},
                                                updatemode="mouseup",
                                                allowCross=False,
                                            ),
                                            html.P(
                                                "80–84 good · 85–89 very good · 90–94 excellent · 95–100 classic. Wines with no listed price stay hidden.",
                                                className="hint",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Button("Reset taste & filters", id="reset-find", type="button", n_clicks=0, className="linkish"),
                ],
            ),
            html.Section(
                className="stage",
                children=[
                    html.Div(
                        className="panel",
                        children=[
                            html.P(id="value-note", className="hint"),
                            dcc.Graph(id="value-map", config={"displayModeBar": False}, style={"height": "440px"}),
                        ],
                    ),
                    html.Div(
                        id="spotlight",
                        className="panel spotlight",
                    ),
                ],
            ),
            html.Section(
                className="panel",
                children=[
                    html.Div(
                        className="panel-head",
                        children=[
                            html.H2("Top picks for you"),
                            dcc.RadioItems(id="rank-picker", options=RANK_CHOICES, value="value", inline=True, className="toggle"),
                        ],
                    ),
                    html.Div(id="shortlist", className="card-grid"),
                ],
            ),
            html.Section(
                className="panel",
                children=[
                    html.H2("Every match"),
                    html.P(
                        "All matching wines, in the order chosen above. Click a column header to sort, and pick a row to read its review. "
                        "“vs. typical” is how many points a wine scores above a typical wine at its price.",
                        className="hint",
                    ),
                    dash_table.DataTable(
                        id="match-table",
                        columns=COLUMNS,
                        page_action="custom",
                        page_current=0,
                        page_size=PAGE_SIZE,
                        sort_action="custom",
                        sort_mode="single",
                        sort_by=[],
                        row_selectable="single",
                        selected_rows=[],
                        style_table={"overflowX": "auto"},
                        style_cell={"textAlign": "left", "padding": "8px 10px", "fontFamily": "Avenir Next, Segoe UI, sans-serif", "fontSize": 14, "whiteSpace": "normal", "height": "auto"},
                        style_header={"fontWeight": 700, "backgroundColor": "#e7eef6", "border": "none"},
                        style_data={"borderLeft": "none", "borderRight": "none"},
                        style_cell_conditional=[{"if": {"column_id": "title"}, "minWidth": "280px"}],
                    ),
                ],
            ),
            html.Div(
                className="next-step",
                children=[
                    html.P("Starred a few? Put them side by side, see how they differ, and find similar bottles."),
                    dcc.Link("Compare & decide →", href="/compare", className="button"),
                ],
            ),
        ]
    )


def matches(country, region, kind, grape, budget, cellar, scores, flavors):
    return narrow(
        data,
        country=country or EVERY,
        region=region or EVERY,
        kind=kind or EVERY,
        grape=grape or EVERY,
        scores=scores,
        budget=budget,
        premium="cellar" in (cellar or []),
        flavors=flavors or [],
    )


@callback(
    Output("area-picker", "options"),
    Output("area-picker", "value"),
    Output("area-picker", "disabled"),
    Output("area-hint", "children"),
    Input("origin-picker", "value"),
)
def choose_area(country):
    if country == EVERY:
        return area_choices(data, EVERY), EVERY, True, "Choose a country first."
    return area_choices(data, country), EVERY, False, f"Regions in {country}."


@callback(
    Output("kind-picker", "value", allow_duplicate=True),
    Output("flavor-picker", "value"),
    Input("style-picker", "value"),
    prevent_initial_call=True,
)
def apply_style(style):
    _label, kind, notes = STYLES.get(style, STYLES["any"])
    # "Any style" also fires when the page opens, so it must not overwrite the type chosen in step 1.
    return (no_update if kind == EVERY else kind), notes


@callback(
    Output("budget-slider", "value"),
    Output("cellar-toggle", "value"),
    Input("occasion-picker", "value"),
    prevent_initial_call=True,
)
def apply_occasion(occasion):
    return OCCASIONS.get(occasion, OCCASIONS["any"])[1], []


@callback(
    Output("occasion-picker", "value"),
    Output("style-picker", "value"),
    Output("flavor-picker", "value", allow_duplicate=True),
    Output("area-picker", "value", allow_duplicate=True),
    Output("budget-slider", "value", allow_duplicate=True),
    Output("cellar-toggle", "value", allow_duplicate=True),
    Output("score-slider", "value"),
    Output("rank-picker", "value"),
    Input("reset-find", "n_clicks"),
    prevent_initial_call=True,
)
def reset_find(clicks):
    if not clicks:
        return (no_update,) * 8
    return "any", "any", [], EVERY, FULL_BUDGET, [], [low_score, high_score], "value"


@callback(
    Output("find-brief", "children"),
    Output("value-note", "children"),
    Output("value-map", "figure"),
    Output("shortlist", "children"),
    *FILTERS,
    Input("starred", "data"),
)
def refresh(country, region, kind, grape, budget, cellar, scores, flavors, order, starred):
    frame = matches(country, region, kind, grape, budget, cellar, scores, flavors)
    starred = starred or []
    if frame.empty:
        empty = html.P("No wines match. Try another style, fewer notes, or a wider price range.", className="quiet")
        return "No wines match these choices yet.", "", value_map(frame, curve, starred), empty

    great = int(frame["value_gap"].ge(GREAT_VALUE_GAP).sum())
    brief = (
        f"{len(frame):,} wines match. {great:,} of them are great value: they score at least {GREAT_VALUE_GAP:.0f} points "
        f"above a typical wine at the same price. Median price ${frame['price'].median():,.0f}, average rating {frame['points'].mean():.1f}."
    )
    shown = min(great, VALUE_SAMPLE) + min(len(frame) - great, VALUE_SAMPLE)
    note = (
        "Each dot is a wine; copper dots are great value. Click a dot to read its review."
        + (f" A random sample of {shown:,} of {len(frame):,} wines is drawn so the chart stays readable." if len(frame) > shown else "")
    )
    picks = rank(frame, order, flavors).head(SHORTLIST)
    cards = [wine_card(row, starred, "pick") for _, row in picks.iterrows()]
    return brief, note, value_map(frame, curve, starred, VALUE_SAMPLE), cards


@callback(
    Output("match-table", "data"),
    Output("match-table", "page_count"),
    Output("match-table", "page_current"),
    Output("match-table", "selected_rows"),
    *FILTERS,
    Input("match-table", "page_current"),
    Input("match-table", "sort_by"),
)
def fill_table(country, region, kind, grape, budget, cellar, scores, flavors, order, page, sort_by):
    frame = matches(country, region, kind, grape, budget, cellar, scores, flavors)
    if ctx.triggered_id not in ("match-table", None):
        page = 0
    if sort_by:
        column, direction = sort_by[0]["column_id"], sort_by[0]["direction"]
        frame = frame.sort_values(column, ascending=direction == "asc", na_position="last")
    else:
        frame = rank(frame, order, flavors)
    pages = max(1, math.ceil(len(frame) / PAGE_SIZE))
    page = min(page or 0, pages - 1)
    rows = frame.iloc[page * PAGE_SIZE : (page + 1) * PAGE_SIZE][[column["id"] for column in COLUMNS] + ["id"]].copy()
    rows["value_gap"] = rows["value_gap"].round(1)
    rows["year"] = rows["year"].astype(object)
    records = rows.astype(object).where(pd.notna(rows), None).to_dict("records")
    return records, pages, page, []


@callback(
    Output("spot", "data"),
    Input("value-map", "clickData"),
    Input("match-table", "selected_rows"),
    Input({"type": "peek", "id": ALL}, "n_clicks"),
    State("match-table", "data"),
    prevent_initial_call=True,
)
def choose_spot(click, selected, _peeks, rows):
    trigger = ctx.triggered_id
    if trigger == "value-map":
        points = (click or {}).get("points") or []
        custom = points[0].get("customdata") if points else None
        return int(custom[0]) if custom else no_update
    if trigger == "match-table":
        return int(rows[selected[0]]["id"]) if selected and rows else no_update
    if isinstance(trigger, dict) and ctx.triggered[0]["value"]:
        return trigger["id"]
    return no_update


@callback(
    Output("spotlight", "children"),
    Input("spot", "data"),
    Input("starred", "data"),
    Input("flavor-picker", "value"),
)
def show_spot(wine_id, starred, flavors):
    found = data.loc[data["id"].eq(wine_id)] if wine_id is not None else data.head(0)
    if found.empty:
        return [
            html.H2("Read before you choose"),
            html.P("Click a dot on the chart, a “Read review” link, or a table row to read that wine's full review here.", className="quiet"),
            html.P("Then star up to three wines to compare them in step 3.", className="quiet"),
        ]
    row = found.iloc[0]
    return [*review_block(row, flavors or None), star_button(int(row["id"]), starred or [], "spot")]
