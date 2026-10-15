from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from src.data_loader import BUDGET_CAP, EVERY


NAVY = ["#e7eef6", "#b7cbe4", "#6d93c4", "#2c5f97", "#16345c"]
COPPER = "#c4622d"
PALE = "#d5dbe3"
QUIET = "#8b95a1"
FONT = "Avenir Next, Segoe UI, sans-serif"
BANDS = ["Under $15", "$15–25", "$25–40", "$40–60", "$60–100", "$100–150", "$150+"]
BAND_EDGES = {
    "Under $15": (0, 15),
    "$15–25": (15, 25),
    "$25–40": (25, 40),
    "$40–60": (40, 60),
    "$60–100": (60, 100),
    "$100–150": (100, 150.0000001),
    "$150+": (150.0000001, float("inf")),
}


def _dress(fig: go.Figure, title: str, height: int) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0, xanchor="left", font=dict(size=16, color="#1c2430")),
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family=FONT, color="#1c2430", size=13),
        height=height,
        margin=dict(l=8, r=8, t=48, b=8),
        hoverlabel=dict(bgcolor="#f7f9fb", font=dict(family=FONT, color="#1c2430")),
    )
    return fig


def blank(message: str, height: int = 420) -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=15, color=QUIET, family=FONT),
    )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return _dress(fig, "", height)


def _dollars(value: float) -> str:
    if pd.isna(value):
        return "n/a"
    return f"${value:,.0f}"


def country_rollup(frame: pd.DataFrame) -> pd.DataFrame:
    located = frame.loc[frame["iso3"].notna() & frame["shown_country"].ne("Unknown")]
    if located.empty:
        return located
    rolled = located.groupby(["iso3", "shown_country"], as_index=False).agg(
        avg_points=("points", "mean"),
        wine_count=("id", "count"),
        median_price=("price", "median"),
    )
    favorite = (
        located.groupby(["iso3", "variety"], as_index=False)
        .size()
        .sort_values(["iso3", "size"], ascending=[True, False])
        .drop_duplicates("iso3")
        .rename(columns={"variety": "favorite"})
    )
    return rolled.merge(favorite[["iso3", "favorite"]], on="iso3", how="left")


def world_map(frame: pd.DataFrame, chosen: str, floor: int) -> go.Figure:
    rolled = country_rollup(frame)
    if rolled.empty:
        return blank("No countries match these filters.", 460)

    ready = rolled.loc[rolled["wine_count"] >= floor]
    thin = rolled.loc[rolled["wine_count"] < floor]
    fig = go.Figure()

    if not thin.empty:
        fig.add_trace(
            go.Choropleth(
                locations=thin["iso3"],
                z=np.zeros(len(thin)),
                locationmode="ISO-3",
                colorscale=[[0, "#c5ced6"], [1, "#c5ced6"]],
                showscale=False,
                marker_line_width=0.3,
                marker_line_color="#f4f7fa",
                hovertext=thin["shown_country"],
                customdata=np.column_stack([thin["wine_count"].astype(int), thin["median_price"].map(_dollars), thin["favorite"]]),
                hovertemplate="<b>%{hovertext}</b><br>%{customdata[0]} reviews — too few to compare<br>Median price: %{customdata[1]}<br>Common variety: %{customdata[2]}<extra></extra>",
            )
        )
    if not ready.empty:
        fig.add_trace(
            go.Choropleth(
                locations=ready["iso3"],
                z=ready["avg_points"],
                locationmode="ISO-3",
                colorscale=NAVY,
                zmin=80,
                zmax=100,
                marker_line_width=0.3,
                marker_line_color="#f4f7fa",
                colorbar=dict(title="Avg rating", thickness=12, len=0.6, tickvals=[80, 85, 90, 95, 100]),
                hovertext=ready["shown_country"],
                customdata=np.column_stack([ready["wine_count"].astype(int), ready["median_price"].map(_dollars), ready["favorite"]]),
                hovertemplate="<b>%{hovertext}</b><br>Average rating: %{z:.1f}<br>Wines: %{customdata[0]}<br>Median price: %{customdata[1]}<br>Common variety: %{customdata[2]}<extra></extra>",
            )
        )

    chosen_iso = ""
    matched = rolled.loc[rolled["shown_country"].eq(chosen), "iso3"]
    if chosen != EVERY and not matched.empty:
        chosen_iso = matched.iloc[0]
    if chosen_iso:
        fig.add_trace(
            go.Choropleth(
                locations=[chosen_iso],
                z=[0],
                locationmode="ISO-3",
                colorscale=[[0, "rgba(0,0,0,0)"], [1, "rgba(0,0,0,0)"]],
                showscale=False,
                marker_line_width=2.6,
                marker_line_color="#1c2430",
                hoverinfo="skip",
            )
        )

    fig.update_geos(
        showframe=False,
        showcoastlines=False,
        showcountries=False,
        showland=True,
        landcolor="#e6edf3",
        showocean=True,
        oceancolor="#f4f7fa",
        projection_type="natural earth",
        bgcolor="rgba(0,0,0,0)",
    )
    fig.update_layout(uirevision="world")
    return _dress(fig, "Average rating by country", 460)


def grape_bubbles(frame: pd.DataFrame, chosen: str) -> go.Figure:
    priced = frame.loc[frame["price"].notna()]
    if priced.empty:
        return blank("No varieties match these filters.")

    summary = priced.groupby("variety", as_index=False).agg(
        wine_count=("id", "count"),
        avg_points=("points", "mean"),
        median_price=("price", "median"),
    )
    floor = 30 if len(priced) > 4000 else 8
    kept = summary.loc[summary["wine_count"] >= floor]
    if kept.empty:
        kept = summary
    shown = kept.nlargest(12, "wine_count")
    if chosen != EVERY and chosen not in set(shown["variety"]) and chosen in set(summary["variety"]):
        shown = pd.concat([shown, summary.loc[summary["variety"].eq(chosen)]], ignore_index=True)

    largest = float(shown["wine_count"].max())
    fig = go.Figure(
        go.Scatter(
            x=shown["median_price"],
            y=shown["avg_points"],
            mode="markers",
            customdata=np.column_stack([shown["variety"], shown["wine_count"]]),
            marker=dict(
                size=shown["wine_count"],
                sizemode="area",
                sizeref=2.0 * largest / (46 ** 2),
                color=COPPER,
                opacity=0.82,
                line=dict(
                    width=[2.4 if name == chosen else 0 for name in shown["variety"]],
                    color="#1c2430",
                ),
            ),
            hovertemplate="<b>%{customdata[0]}</b><br>Typical price: $%{x:.0f}<br>Average rating: %{y:.1f}<br>Wines: %{customdata[1]}<extra></extra>",
        )
    )
    fig.update_xaxes(title="Typical price ($)", gridcolor="#e6ebf0")
    fig.update_yaxes(title="Average rating", range=[80, 101], dtick=5, gridcolor="#e6ebf0")
    return _dress(fig, "Varieties by typical price and rating", 460)


def tag_bands(prices: pd.Series) -> pd.Series:
    values = prices.to_numpy(dtype=float)
    labels = np.empty(len(values), dtype=object)
    valid = ~np.isnan(values)
    labels[:] = None
    labels[valid & (values < 15)] = "Under $15"
    labels[valid & (values >= 15) & (values < 25)] = "$15–25"
    labels[valid & (values >= 25) & (values < 40)] = "$25–40"
    labels[valid & (values >= 40) & (values < 60)] = "$40–60"
    labels[valid & (values >= 60) & (values < 100)] = "$60–100"
    labels[valid & (values >= 100) & (values <= BUDGET_CAP)] = "$100–150"
    labels[valid & (values > BUDGET_CAP)] = "$150+"
    return pd.Series(labels, index=prices.index)


def inside_budget(label: str, budget: list[float] | tuple[float, float], premium: bool) -> bool:
    if label == "$150+":
        return premium
    low, high = BAND_EDGES[label]
    budget_low, budget_high = budget
    return low <= budget_high and budget_low < high


def band_table(frame: pd.DataFrame, budget: list[float] | tuple[float, float], premium: bool) -> pd.DataFrame:
    priced = frame.loc[frame["price"].notna(), ["price", "points"]].copy()
    empty = pd.DataFrame(columns=["band", "avg_points", "wine_count", "inside"])
    if priced.empty:
        return empty
    priced["band"] = tag_bands(priced["price"])
    order = [label for label in BANDS if premium or label != "$150+"]
    summary = priced.groupby("band", as_index=False).agg(avg_points=("points", "mean"), wine_count=("points", "count"))
    summary = summary.loc[summary["band"].isin(order)].copy()
    summary["band"] = pd.Categorical(summary["band"], categories=order, ordered=True)
    summary = summary.sort_values("band")
    summary["inside"] = summary["band"].astype(str).map(lambda label: inside_budget(label, budget, premium))
    return summary


def budget_bars(frame: pd.DataFrame, budget: list[float] | tuple[float, float], premium: bool) -> go.Figure:
    summary = band_table(frame, budget, premium)
    if summary.empty:
        return blank("No priced wines match these filters.")
    colors = [COPPER if flagged else PALE for flagged in summary["inside"]]
    fig = go.Figure(
        go.Bar(
            x=summary["band"].astype(str),
            y=summary["avg_points"],
            marker_color=colors,
            marker_line_width=0,
            customdata=summary["wine_count"],
            hovertemplate="<b>%{x}</b><br>Average rating: %{y:.1f}<br>Wines: %{customdata:,}<extra></extra>",
        )
    )
    fig.update_yaxes(range=[80, 101], title="Average rating", dtick=5, gridcolor="#e6ebf0")
    fig.update_xaxes(title="")
    return _dress(fig, "Does paying more raise the rating?", 460)


def price_sentence(summary: pd.DataFrame) -> str:
    if summary.empty:
        return "No priced wines are available for this selection."
    first, last = summary.iloc[0], summary.iloc[-1]
    if len(summary) == 1:
        return f"Across all prices here, the only populated band is {first['band']}, averaging {first['avg_points']:.1f} points."
    gap = abs(float(last["avg_points"]) - float(first["avg_points"]))
    return (
        "Across all prices here, average rating moves from "
        f"{first['avg_points']:.1f} ({first['band']}) to {last['avg_points']:.1f} ({last['band']}), "
        f"a difference of {gap:.1f} points."
    )
