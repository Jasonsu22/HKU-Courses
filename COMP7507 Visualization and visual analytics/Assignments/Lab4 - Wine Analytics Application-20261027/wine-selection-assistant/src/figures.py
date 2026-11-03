from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from src.data_loader import BUDGET_CAP, EVERY, GREAT_VALUE_GAP, expected_points


NAVY = ["#e7eef6", "#b7cbe4", "#6d93c4", "#2c5f97", "#16345c"]
COPPER = "#c4622d"
PALE = "#d5dbe3"
QUIET = "#8b95a1"
FONT = "Avenir Next, Segoe UI, sans-serif"
KIND_NAMES = {"red": "Red", "white": "White", "rose": "Rosé", "sparkling": "Sparkling", "dessert": "Dessert", "other": "Other"}
COMPARE_COLORS = [COPPER, "#2c5f97", "#3f8f6b"]
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


def world_map(frame: pd.DataFrame, chosen: str, floor: int, measure: str = "rating") -> go.Figure:
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
    if measure == "count":
        # Review counts span 1 to 50,000+, so colour on a log scale.
        shade = dict(
            z=np.log10(ready["wine_count"]),
            zmin=0,
            zmax=np.log10(max(float(rolled["wine_count"].max()), 10)),
            colorbar=dict(title="Reviews", thickness=12, len=0.6, tickvals=[0, 1, 2, 3, 4], ticktext=["1", "10", "100", "1k", "10k"]),
        )
        title = "Number of reviews by country"
    else:
        shade = dict(
            z=ready["avg_points"],
            zmin=80,
            zmax=100,
            colorbar=dict(title="Avg rating", thickness=12, len=0.6, tickvals=[80, 85, 90, 95, 100]),
        )
        title = "Average rating by country"
    if not ready.empty:
        fig.add_trace(
            go.Choropleth(
                locations=ready["iso3"],
                locationmode="ISO-3",
                colorscale=NAVY,
                marker_line_width=0.3,
                marker_line_color="#f4f7fa",
                **shade,
                hovertext=ready["shown_country"],
                customdata=np.column_stack([ready["wine_count"].astype(int), ready["median_price"].map(_dollars), ready["favorite"], ready["avg_points"].round(1)]),
                hovertemplate="<b>%{hovertext}</b><br>Reviews: %{customdata[0]}<br>Average rating: %{customdata[3]}<br>Median price: %{customdata[1]}<br>Common variety: %{customdata[2]}<extra></extra>",
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
    return _dress(fig, title, 460)


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


def category_bars(frame: pd.DataFrame, chosen: str) -> go.Figure:
    if frame.empty:
        return blank("No reviews match this selection.", 360)
    counts = frame["category"].value_counts()
    fig = go.Figure(
        go.Bar(
            x=[KIND_NAMES.get(name, name) for name in counts.index],
            y=counts.values,
            customdata=counts.index,
            marker_color=[COPPER if chosen in (EVERY, name) else PALE for name in counts.index],
            marker_line_width=0,
            hovertemplate="<b>%{x}</b><br>Reviews: %{y:,}<extra></extra>",
        )
    )
    fig.update_yaxes(title="Reviews", gridcolor="#e6ebf0")
    return _dress(fig, "Which wine types are reviewed most?", 360)


def variety_bars(frame: pd.DataFrame, chosen: str, top: int = 12) -> go.Figure:
    if frame.empty:
        return blank("No reviews match this selection.", 360)
    summary = (
        frame.groupby("variety", as_index=False)
        .agg(wine_count=("id", "count"), avg_points=("points", "mean"), median_price=("price", "median"))
        .nlargest(top, "wine_count")
        .iloc[::-1]
    )
    fig = go.Figure(
        go.Bar(
            x=summary["wine_count"],
            y=summary["variety"],
            orientation="h",
            customdata=np.column_stack([summary["variety"], summary["avg_points"].round(1), summary["median_price"].map(_dollars)]),
            marker_color=[COPPER if chosen in (EVERY, name) else PALE for name in summary["variety"]],
            marker_line_width=0,
            hovertemplate="<b>%{customdata[0]}</b><br>Reviews: %{x:,}<br>Average rating: %{customdata[1]}<br>Median price: %{customdata[2]}<extra></extra>",
        )
    )
    fig.update_xaxes(title="Reviews", gridcolor="#e6ebf0")
    return _dress(fig, "Most reviewed varieties", 360)


def value_map(frame: pd.DataFrame, curve: np.ndarray, starred: list[int], sample: int = 2500) -> go.Figure:
    priced = frame.loc[frame["price"].gt(0) & frame["points"].notna()]
    if priced.empty:
        return blank("No priced wines match these filters.", 440)
    great = priced.loc[priced["value_gap"].ge(GREAT_VALUE_GAP)]
    rest = priced.loc[priced["value_gap"].lt(GREAT_VALUE_GAP)]
    # A random sample keeps the cloud readable without favouring any price or rating.
    if len(rest) > sample:
        rest = rest.sample(sample, random_state=7)
    if len(great) > sample:
        great = great.sample(sample, random_state=7)
    # Integer ratings stack into rows, so a little vertical jitter shows density.
    jitter = np.random.default_rng(7)
    fig = go.Figure()
    for part, name, color, size in [(rest, "Other matches", "#9fb3c8", 5), (great, "Great value", COPPER, 7)]:
        if part.empty:
            continue
        fig.add_trace(
            go.Scattergl(
                x=part["price"],
                y=part["points"] + jitter.uniform(-0.3, 0.3, len(part)),
                mode="markers",
                name=name,
                marker=dict(size=size, color=color, opacity=0.55 if name == "Other matches" else 0.8, line_width=0),
                customdata=np.column_stack([part["id"], part["title"], part["points"], part["value_gap"].round(1)]),
                hovertemplate="<b>%{customdata[1]}</b><br>$%{x:,.0f} · %{customdata[2]} pts<br>%{customdata[3]:+} pts vs. typical at this price<extra></extra>",
            )
        )
    low, high = float(priced["price"].min()), float(priced["price"].max())
    line = pd.Series(np.geomspace(max(low, 4), max(high, 5), 60))
    fig.add_trace(
        go.Scatter(
            x=line,
            y=expected_points(line, curve),
            mode="lines",
            name="Typical rating at this price",
            line=dict(color="#1c2430", width=2, dash="dash"),
            hoverinfo="skip",
        )
    )
    pinned = priced.loc[priced["id"].isin(starred)]
    if not pinned.empty:
        fig.add_trace(
            go.Scatter(
                x=pinned["price"],
                y=pinned["points"],
                mode="markers",
                name="In your compare list",
                marker=dict(symbol="star", size=16, color="#f2c14e", line=dict(color="#1c2430", width=1)),
                customdata=np.column_stack([pinned["id"], pinned["title"], pinned["points"], pinned["value_gap"].round(1)]),
                hovertemplate="<b>%{customdata[1]}</b><br>$%{x:,.0f} · %{customdata[2]} pts<extra></extra>",
            )
        )
    fig.update_xaxes(title="Price ($, log scale)", type="log", gridcolor="#e6ebf0")
    fig.update_yaxes(title="Rating (points)", gridcolor="#e6ebf0")
    fig.update_layout(legend=dict(orientation="h", y=-0.2, x=0), uirevision="value")
    return _dress(fig, "Where is the value? Wines above the dashed line beat their price", 440)


def flavor_radar(profiles: dict[str, pd.Series]) -> go.Figure:
    if not profiles:
        return blank("Add wines to compare their flavor profiles.", 420)
    table = pd.DataFrame(profiles).fillna(0)
    axes = table.max(axis=1).nlargest(10).index.tolist()
    fig = go.Figure()
    for index, (name, shares) in enumerate(table.loc[axes].items()):
        values = (shares * 100).round(0).tolist()
        fig.add_trace(
            go.Scatterpolar(
                r=values + values[:1],
                theta=axes + axes[:1],
                name=name,
                fill="toself",
                opacity=0.55,
                line=dict(color=COMPARE_COLORS[index % len(COMPARE_COLORS)], width=2),
                hovertemplate="<b>%{theta}</b><br>%{r:.0f}% of reviews mention it<extra>" + name + "</extra>",
            )
        )
    fig.update_layout(
        polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(ticksuffix="%", nticks=4, angle=90, tickangle=90, tickfont=dict(size=10, color=QUIET), gridcolor="#e6ebf0"), angularaxis=dict(gridcolor="#e6ebf0")),
        legend=dict(orientation="h", y=-0.12, x=0),
    )
    return _dress(fig, "How each variety is usually described", 420)

