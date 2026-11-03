from __future__ import annotations

import dash
import pandas as pd
from dash import Input, Output, State, callback, dcc, html, no_update

from src.data_loader import BUDGET_CAP, EVERY, narrow, rank, reviews, score_bounds, similar_wines, variety_profile
from src.figures import COMPARE_COLORS, flavor_radar
from src.summaries import MAX_COMPARE, price_text, review_block, wine_card
from src.text import variety_words, word_cloud_image, word_counts


dash.register_page(__name__, path="/compare", name="Compare & decide", title="Compare & decide · Wine Selection Assistant", order=2)

data = reviews()
low_score, high_score = score_bounds(data)
grape_words = variety_words(data)


def layout(**_):
    return html.Div(
        children=[
            html.Section(
                className="banner",
                children=[
                    html.P("Step 3 · Compare & decide", className="kicker"),
                    html.H1("Which one will you buy?"),
                    html.P(id="compare-brief", className="brief"),
                ],
            ),
            html.Div(
                id="compare-empty",
                className="panel empty",
                children=[
                    html.H2("Your compare list is empty"),
                    html.P(f"Star up to {MAX_COMPARE} wines in step 2, or load three great-value examples from your current selection.", className="quiet"),
                    html.Div(
                        className="card-actions",
                        children=[
                            dcc.Link("← Find my wine", href="/find", className="button ghost"),
                            html.Button("Load 3 example picks", id="load-examples", type="button", n_clicks=0, className="button"),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="compare-body",
                children=[
                    html.Section(id="compare-cards", className="compare-grid"),
                    html.Section(
                        className="pair",
                        children=[
                            html.Div(
                                className="panel",
                                children=[
                                    html.P("Share of all reviews of each variety that mention a note. Bigger shape = described that way more often.", className="hint"),
                                    dcc.Graph(id="compare-radar", config={"displayModeBar": False}, style={"height": "420px"}),
                                ],
                            ),
                            html.Div(
                                className="panel",
                                children=[
                                    html.H2(id="cloud-title", className="panel-title"),
                                    html.Img(id="compare-cloud", className="cloud", alt="Word cloud of review language"),
                                    html.P(id="cloud-note", className="hint"),
                                ],
                            ),
                        ],
                    ),
                    html.Section(
                        className="panel",
                        children=[
                            html.H2("You might also like"),
                            html.P(
                                "Same wine type, within 40% of the price, rated at most 1 point lower (3 for top-rated wines), "
                                "and sharing the most flavor notes in the review. One wine per winery.",
                                className="hint",
                            ),
                            html.Div(id="compare-similar"),
                        ],
                    ),
                ],
            ),
        ]
    )


def verdict(wines) -> list:
    if len(wines) < 2:
        return ["Add another wine to see how they differ. ", dcc.Link("Find more wines →", href="/find")]
    cheapest = wines.loc[wines["price"].idxmin()] if wines["price"].notna().any() else None
    best = wines.sort_values(["points", "price"], ascending=[False, True]).iloc[0]
    value = wines.sort_values("value_gap", ascending=False).iloc[0]
    parts = [html.Strong("Quick verdict: "), f"highest rated is {best['title']} ({best['points']:.0f} pts). "]
    if cheapest is not None:
        parts.append(f"Cheapest is {cheapest['title']} ({price_text(cheapest['price'])}). ")
    if pd.notna(value["value_gap"]):
        parts.append(f"Best value is {value['title']}, {value['value_gap']:+.1f} points above a typical wine at its price.")
    return parts


def compare_card(row, index: int) -> html.Article:
    return html.Article(
        className="panel compare-card",
        style={"borderTop": f"5px solid {COMPARE_COLORS[index % len(COMPARE_COLORS)]}"},
        children=[
            *review_block(row),
            html.Div(className="tags", children=[html.Span(f"vs. typical at this price: {row['value_gap']:+.1f} pts", className="tag plain")] if pd.notna(row["value_gap"]) else []),
            html.Button("Remove", id={"type": "unstar", "id": int(row["id"])}, n_clicks=0, className="linkish"),
        ],
    )


@callback(
    Output("compare-empty", "style"),
    Output("compare-body", "style"),
    Output("compare-brief", "children"),
    Output("compare-cards", "children"),
    Output("compare-radar", "figure"),
    Output("compare-cloud", "src"),
    Output("cloud-title", "children"),
    Output("cloud-note", "children"),
    Output("compare-similar", "children"),
    Input("starred", "data"),
)
def refresh(starred):
    starred = starred or []
    wines = data.set_index("id").reindex(starred).dropna(subset=["title"]).reset_index()
    if wines.empty:
        hidden = {"display": "none"}
        return {}, hidden, "Pick the wines you are deciding between, then compare them here.", [], flavor_radar({}), "", "", "", []

    cards = [compare_card(row, index) for index, (_, row) in enumerate(wines.iterrows())]
    varieties = list(dict.fromkeys(wines["variety"]))
    radar = flavor_radar({name: variety_profile(data, name) for name in varieties})

    counts, used = word_counts(data.loc[data["variety"].isin(varieties), "description"], skip=grape_words)
    cloud = word_cloud_image(counts) if counts else ""
    cloud_title = f"How reviewers describe {' & '.join(varieties)}"
    cloud_note = f"Most frequent words in a random sample of {used:,} reviews of these varieties. Common words and grape names (which blends mention a lot) are left out."

    groups = []
    for _, row in wines.iterrows():
        found = similar_wines(data, int(row["id"]), starred)
        children = [wine_card(other, starred, f"like-{int(row['id'])}", peek=False) for _, other in found.iterrows()]
        groups.append(
            html.Div(
                className="similar-group",
                children=[
                    html.H3(f"Like {row['title']}"),
                    html.Div(children or [html.P("No close matches: few wines of this type are rated this high at a similar price.", className="quiet")], className="card-grid"),
                ],
            )
        )
    return {"display": "none"}, {}, verdict(wines), cards, radar, cloud, cloud_title, cloud_note, groups


@callback(
    Output("starred", "data", allow_duplicate=True),
    Input("load-examples", "n_clicks"),
    State("origin-picker", "value"),
    State("kind-picker", "value"),
    State("grape-picker", "value"),
    prevent_initial_call=True,
)
def load_examples(clicks, country, kind, grape):
    if not clicks:
        return no_update
    frame = narrow(
        data,
        country=country or EVERY,
        region=EVERY,
        kind=kind or EVERY,
        grape=grape or EVERY,
        scores=[low_score, high_score],
        budget=[4, BUDGET_CAP],
        premium=False,
    )
    # Different varieties make the comparison more interesting.
    picks = rank(frame, "value").drop_duplicates("variety").head(MAX_COMPARE)
    if len(picks) < MAX_COMPARE:
        picks = rank(frame, "value").head(MAX_COMPARE)
    return [int(value) for value in picks["id"]]
