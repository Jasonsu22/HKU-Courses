from __future__ import annotations

from functools import lru_cache

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, State, callback_context, dcc, html

from src.data_loader import (
    get_country_options,
    get_points_bounds,
    get_price_bounds,
    get_variety_options,
    load_wine_data,
)


ALL_VALUE = "__all__"


@lru_cache(maxsize=1)
def get_data() -> pd.DataFrame:
    return load_wine_data()


def build_price_marks(min_price: float, max_price: float) -> dict[float, str]:
    if max_price <= min_price:
        return {round(min_price, 0): f"${min_price:,.0f}"}

    anchors = [
        min_price,
        min_price + (max_price - min_price) * 0.25,
        min_price + (max_price - min_price) * 0.5,
        min_price + (max_price - min_price) * 0.75,
        max_price,
    ]
    marks: dict[float, str] = {}
    for value in anchors:
        rounded = float(round(value, 0))
        if min_price <= rounded <= max_price:
            marks[rounded] = f"${rounded:,.0f}"
    return marks


def build_point_marks(min_points: int, max_points: int) -> dict[int, str]:
    anchors = sorted({min_points, max_points, 82, 85, 88, 90, 92, 95, 98, 100})
    marks: dict[int, str] = {}
    for value in anchors:
        if min_points <= value <= max_points:
            marks[int(value)] = str(value)
    return marks


def apply_filters(
    dataframe: pd.DataFrame,
    country: str,
    category: str,
    variety: str,
    price_range: list[float],
    point_range: list[int],
    include_country: bool = True,
) -> pd.DataFrame:
    filtered = dataframe.copy()

    if category != ALL_VALUE:
        filtered = filtered.loc[filtered["category"] == category]
    if variety != ALL_VALUE:
        filtered = filtered.loc[filtered["variety"] == variety]
    if include_country and country != ALL_VALUE:
        filtered = filtered.loc[filtered["country_display"] == country]

    filtered = filtered.loc[filtered["price"].between(price_range[0], price_range[1], inclusive="both")]
    filtered = filtered.loc[filtered["points"].between(point_range[0], point_range[1], inclusive="both")]
    return filtered


def empty_figure(message: str):
    fig = px.scatter(title=message)
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=24, r=24, t=60, b=24),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        annotations=[
            dict(
                text=message,
                x=0.5,
                y=0.5,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=16, color="#495057"),
            )
        ],
    )
    return fig


def make_map_figure(dataframe: pd.DataFrame):
    country_summary = (
        dataframe.loc[dataframe["country_display"] != "Unknown"]
        .groupby("country_display", as_index=False)
        .agg(avg_points=("points", "mean"), wine_count=("id", "count"))
    )
    if country_summary.empty:
        return empty_figure("No country data for the current filters.")

    fig = px.choropleth(
        country_summary,
        locations="country_display",
        locationmode="country names",
        color="avg_points",
        hover_name="country_display",
        hover_data={"avg_points": ":.1f", "wine_count": True, "country_display": False},
        color_continuous_scale="YlOrBr",
        title="Country map",
    )
    fig.update_layout(
        template="plotly_white",
        height=470,
        margin=dict(l=0, r=0, t=60, b=0),
        coloraxis_colorbar=dict(title="Avg rating"),
    )
    fig.update_geos(showframe=False, showcoastlines=False, projection_type="natural earth")
    return fig


def make_variety_figure(dataframe: pd.DataFrame):
    variety_summary = dataframe.groupby("variety", as_index=False).agg(wine_count=("id", "count"), avg_points=("points", "mean"))
    variety_summary = variety_summary.sort_values(["wine_count", "avg_points"], ascending=[False, False]).head(12)
    if variety_summary.empty:
        return empty_figure("No variety data for the current filters.")

    fig = px.bar(
        variety_summary.sort_values("wine_count"),
        x="wine_count",
        y="variety",
        orientation="h",
        color="avg_points",
        color_continuous_scale="Tealgrn",
        title="Top varieties in the current slice",
        hover_data={"avg_points": ":.1f"},
    )
    fig.update_layout(template="plotly_white", height=430, margin=dict(l=20, r=20, t=60, b=20), coloraxis_colorbar=dict(title="Avg rating"))
    fig.update_xaxes(title="Wine count")
    fig.update_yaxes(title="")
    return fig


def make_scatter_figure(dataframe: pd.DataFrame):
    if dataframe.empty:
        return empty_figure("No price and rating data for the current filters.")

    fig = px.scatter(
        dataframe,
        x="price",
        y="points",
        color="category",
        hover_data={"country_display": True, "variety": True, "winery": True, "price": ":.0f", "points": True},
        opacity=0.65,
        title="Price versus rating",
        labels={"price": "Price ($)", "points": "Rating"},
    )
    fig.update_traces(marker=dict(size=8))
    fig.update_layout(template="plotly_white", height=430, margin=dict(l=20, r=20, t=60, b=20), legend_title_text="Category")
    return fig


def make_dashboard_title(dataframe: pd.DataFrame, country: str) -> str:
    if dataframe.empty:
        return "Wine Discovery Dashboard"
    if country != ALL_VALUE:
        return f"Wine Discovery Dashboard - {country}"
    return "Wine Discovery Dashboard"


data = get_data()
country_options = get_country_options(data)
variety_options = get_variety_options(data)
price_min, price_max = get_price_bounds(data)
points_min, points_max = get_points_bounds(data)

app = Dash(__name__, title="Wine Discovery Dashboard")
server = app.server

app.layout = html.Div(
    className="page-shell",
    children=[
        html.Div(
            className="hero",
            children=[
                html.Div(
                    children=[
                        html.P("Local-only Plotly Dash dashboard", className="eyebrow"),
                        html.H1("Discover wine by country, variety, price, and rating"),
                        html.P(
                            "Use the map to pick a country, then narrow the catalog with price, rating, and variety filters.",
                            className="hero-copy",
                        ),
                    ]
                ),
                html.Div(
                    className="hero-badge",
                    children=[
                        html.Span("Data rows"),
                        html.Strong(f"{len(data):,}"),
                    ],
                ),
            ],
        ),
        html.Div(
            className="layout-grid",
            children=[
                html.Aside(
                    className="control-panel",
                    children=[
                        html.Div(
                            className="panel-header",
                            children=[html.H2("Filters"), html.P("Click the map or use the dropdowns to refine the slice.")],
                        ),
                        html.Label("Country"),
                        dcc.Dropdown(
                            id="country-dropdown",
                            options=country_options,
                            value=ALL_VALUE,
                            clearable=False,
                            searchable=True,
                            placeholder="Select a country",
                        ),
                        html.Button("Reset country", id="reset-country", className="reset-button"),
                        html.Label("Wine type"),
                        dcc.RadioItems(
                            id="category-filter",
                            options=[
                                {"label": "All types", "value": ALL_VALUE},
                                {"label": "Red", "value": "red"},
                                {"label": "White", "value": "white"},
                                {"label": "Other", "value": "other"},
                            ],
                            value=ALL_VALUE,
                            className="radio-row",
                        ),
                        html.Label("Variety"),
                        dcc.Dropdown(
                            id="variety-dropdown",
                            options=variety_options,
                            value=ALL_VALUE,
                            clearable=False,
                            searchable=True,
                            placeholder="Select a variety",
                        ),
                        html.Label("Price range"),
                        dcc.RangeSlider(
                            id="price-slider",
                            min=price_min,
                            max=price_max,
                            step=max((price_max - price_min) / 200, 1),
                            value=[price_min, min(price_max, 150)],
                            marks=build_price_marks(price_min, price_max),
                            tooltip={"placement": "bottom", "always_visible": False},
                            updatemode="mouseup",
                            allowCross=False,
                        ),
                        html.Label("Rating range"),
                        dcc.RangeSlider(
                            id="points-slider",
                            min=points_min,
                            max=points_max,
                            step=1,
                            value=[points_min, points_max],
                            marks=build_point_marks(points_min, points_max),
                            tooltip={"placement": "bottom", "always_visible": False},
                            allowCross=False,
                        ),
                    ],
                ),
                html.Main(
                    className="content-panel",
                    children=[
                        html.Div(
                            className="kpi-row",
                            children=[
                                html.Div([html.Span("Wines"), html.Strong(id="kpi-wines")], className="kpi-card"),
                                html.Div([html.Span("Average rating"), html.Strong(id="kpi-rating")], className="kpi-card"),
                                html.Div([html.Span("Median price"), html.Strong(id="kpi-price")], className="kpi-card"),
                                html.Div([html.Span("Top variety"), html.Strong(id="kpi-variety")], className="kpi-card"),
                            ],
                        ),
                        html.Div(
                            className="graph-card graph-card-map",
                            children=[
                                html.Div(className="card-title", children=[html.H2(id="dashboard-title"), html.P("Click a country to update the rest of the dashboard.")]),
                                dcc.Graph(id="country-map", config={"displayModeBar": False}),
                            ],
                        ),
                        html.Div(
                            className="graph-grid",
                            children=[
                                html.Div(className="graph-card", children=[dcc.Graph(id="variety-bar", config={"displayModeBar": False})]),
                                html.Div(className="graph-card", children=[dcc.Graph(id="price-points-scatter", config={"displayModeBar": False})]),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("country-dropdown", "value"),
    Input("country-map", "clickData"),
    Input("reset-country", "n_clicks"),
    State("country-dropdown", "value"),
    prevent_initial_call=True,
)
def sync_country_selection(click_data, reset_clicks, current_value):
    triggered = callback_context.triggered_id
    if triggered == "reset-country":
        return ALL_VALUE
    if triggered == "country-map" and click_data:
        points = click_data.get("points", [])
        if points:
            hovered_country = points[0].get("location") or points[0].get("hovertext")
            if hovered_country:
                return hovered_country
    return current_value


@app.callback(
    Output("country-map", "figure"),
    Output("variety-bar", "figure"),
    Output("price-points-scatter", "figure"),
    Output("kpi-wines", "children"),
    Output("kpi-rating", "children"),
    Output("kpi-price", "children"),
    Output("kpi-variety", "children"),
    Output("dashboard-title", "children"),
    Input("country-dropdown", "value"),
    Input("category-filter", "value"),
    Input("variety-dropdown", "value"),
    Input("price-slider", "value"),
    Input("points-slider", "value"),
)
def update_dashboard(country, category, variety, price_range, point_range):
    map_slice = apply_filters(data, ALL_VALUE, category, variety, price_range, point_range, include_country=False)
    filtered = apply_filters(data, country, category, variety, price_range, point_range)

    if filtered.empty:
        kpi_wines = "0"
        kpi_rating = "-"
        kpi_price = "-"
        kpi_variety = "-"
    else:
        top_variety = filtered["variety"].value_counts().idxmax()
        kpi_wines = f"{len(filtered):,}"
        kpi_rating = f"{filtered['points'].mean():.1f}"
        kpi_price = f"${filtered['price'].median():.0f}" if filtered["price"].notna().any() else "-"
        kpi_variety = top_variety

    return (
        make_map_figure(map_slice),
        make_variety_figure(filtered),
        make_scatter_figure(filtered),
        kpi_wines,
        kpi_rating,
        kpi_price,
        kpi_variety,
        make_dashboard_title(filtered, country),
    )


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
