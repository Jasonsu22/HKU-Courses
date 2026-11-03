from __future__ import annotations

import dash
from dash import ALL, Dash, Input, Output, State, ctx, dcc, html, no_update

from src.data_loader import EVERY, KIND_CHOICES, grape_choices, origin_choices, reviews
from src.summaries import MAX_COMPARE


data = reviews()

app = Dash(__name__, use_pages=True, title="Wine Selection Assistant", suppress_callback_exceptions=True)
server = app.server

STEPS = [("/", "Explore the market"), ("/find", "Find my wine"), ("/compare", "Compare & decide")]


def step_link(index: int, path: str, label: str) -> dcc.Link:
    extra = [" ", html.Span(id="compare-count", className="count")] if path == "/compare" else []
    return dcc.Link([html.Span(str(index + 1), className="num"), label, *extra], href=path, id=f"step-{index}", className="step")


app.layout = html.Div(
    className="shell",
    children=[
        dcc.Location(id="url"),
        dcc.Store(id="starred", data=[], storage_type="session"),
        html.Header(
            className="topbar",
            children=[
                html.Div(
                    children=[
                        html.P("Wine Selection Assistant", className="kicker"),
                        html.P("From a world of reviews to one bottle you'll enjoy, in three steps.", className="muted tagline"),
                    ]
                ),
                html.Nav([step_link(index, path, label) for index, (path, label) in enumerate(STEPS)], className="steps"),
            ],
        ),
        html.Section(
            className="controls selection",
            children=[
                html.Div(
                    children=[
                        html.Label("Country"),
                        dcc.Dropdown(id="origin-picker", options=origin_choices(data), value=EVERY, clearable=False, searchable=True),
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
                    className="selection-end",
                    children=[
                        html.P("Your selection follows you across all three steps.", className="hint"),
                        html.Button("Reset selection", id="reset-selection", type="button", n_clicks=0, className="linkish"),
                    ],
                ),
            ],
        ),
        dash.page_container,
        html.Footer(
            "Based on about 130,000 historical Wine Enthusiast reviews. Prices are past list prices, not current offers; "
            "review counts describe the dataset, not sales.",
            className="hint footer",
        ),
    ],
)


@app.callback(
    Output("grape-picker", "options"),
    Output("grape-picker", "value"),
    Input("origin-picker", "value"),
    Input("kind-picker", "value"),
    State("grape-picker", "value"),
)
def keep_grape_valid(country, kind, current):
    options = grape_choices(data, kind or EVERY, country or EVERY)
    allowed = {item["value"] for item in options}
    return options, current if current in allowed else EVERY


@app.callback(
    Output("origin-picker", "value", allow_duplicate=True),
    Output("kind-picker", "value", allow_duplicate=True),
    Output("grape-picker", "value", allow_duplicate=True),
    Input("reset-selection", "n_clicks"),
    prevent_initial_call=True,
)
def reset_selection(_clicks):
    return EVERY, EVERY, EVERY


@app.callback(
    [Output(f"step-{index}", "className") for index in range(len(STEPS))],
    Output("compare-count", "children"),
    Input("url", "pathname"),
    Input("starred", "data"),
)
def mark_step(path, starred):
    classes = ["step active" if path == step_path else "step" for step_path, _ in STEPS]
    return *classes, f"({len(starred or [])}/{MAX_COMPARE})"


@app.callback(
    Output("starred", "data"),
    Input({"type": "star", "id": ALL, "where": ALL}, "n_clicks"),
    Input({"type": "unstar", "id": ALL}, "n_clicks"),
    State("starred", "data"),
    prevent_initial_call=True,
)
def toggle_star(_stars, _unstars, starred):
    # Newly drawn buttons also fire this callback, with zero clicks.
    if not ctx.triggered_id or not ctx.triggered[0]["value"]:
        return no_update
    wine_id = ctx.triggered_id["id"]
    starred = list(starred or [])
    if wine_id in starred:
        starred.remove(wine_id)
    elif ctx.triggered_id["type"] == "star":
        # A full list drops the oldest pick so the newest choice always lands.
        starred = (starred + [wine_id])[-MAX_COMPARE:]
    return starred


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, dev_tools_ui=False)
