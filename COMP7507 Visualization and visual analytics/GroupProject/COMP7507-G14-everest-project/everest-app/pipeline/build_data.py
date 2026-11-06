#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成前端数据包：
    data/everest_data.js   window.EVEREST_DATA = {...}
    data/everest_data.json 同内容，便于调试/校验

只使用本地 Maven Analytics 快照；不联网、不改原始 CSV。
"""

from __future__ import annotations

import hashlib
import json
import statistics
from datetime import date
from pathlib import Path

import pandas as pd

import prepare as P

HERE = Path(__file__).resolve().parent
APP = HERE.parent
OUT_JSON = APP / "data" / "everest_data.json"
OUT_JS = APP / "data" / "everest_data.js"
DATA_DIR = P.DATA

PEAK_HEIGHT = 8849
MODEL_START, MODEL_END = 1990, 2024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def q(vals, p):
    vals = sorted(v for v in vals if v == v)
    if not vals:
        return None
    k = (len(vals) - 1) * p
    lo, hi = int(k), min(int(k) + 1, len(vals) - 1)
    return round(vals[lo] + (vals[hi] - vals[lo]) * (k - lo), 1)


def doy(v):
    """日期字符串 -> 一年中的第几天；无法解析返回 None。"""
    t = pd.to_datetime(v, errors="coerce")
    return None if pd.isna(t) else int(t.day_of_year)


def main() -> None:
    clean = P.prepare()
    e, m = P.everest(clean)
    e = e.sort_values(["year", "expid"]).reset_index(drop=True)

    # ---- 逐 expedition 记录（模块二在浏览器里自行筛选/聚合） ----------------
    expeditions = []
    for r in e.itertuples():
        expeditions.append({
            "id": r.uid,
            "year": int(r.year),
            "season": r.season,
            "side": r.side,
            "route": r.route,
            "standard": r.route_group == "standard",
            "family": r.route_family,
            "members": int(r.totmembers) if r.totmembers == r.totmembers else 0,
            "hired": int(r.tothired) if r.tothired == r.tothired else 0,
            "summits": int(r.smtmembers) if r.smtmembers == r.smtmembers else 0,
            "summitsHired": int(r.smthired) if r.smthired == r.smthired else 0,
            "mDeaths": int(r.mdeaths) if r.mdeaths == r.mdeaths else 0,
            "hDeaths": int(r.hdeaths) if r.hdeaths == r.hdeaths else 0,
            "o2": bool(r.o2used),
            "success": bool(r.success1),
            "daysSummit": None if r.smtdays != r.smtdays else float(r.smtdays),
            "daysTotal": None if r.totdays != r.totdays else float(r.totdays),
            "hp": int(r.highpoint) if r.highpoint == r.highpoint and r.highpoint > 0 else None,
            "end": r.end_cat,
            "closure": bool(r.closure),
            "smt": doy(r.smtdate),
            "bc": doy(r.bcdate),
            "agency": r.agency_clean if isinstance(r.agency_clean, str) else None,
            "nation": r.nation if isinstance(r.nation, str) else None,
        })

    # ---- 年度聚合 -----------------------------------------------------------
    yearly = []
    for y, g in e.groupby("year"):
        days = [v for v in g["smtdays"].tolist() if v == v and 5 <= v <= 130]
        yearly.append({
            "year": int(y),
            "n": int(len(g)),
            "k": int(g["success1"].sum()),
            "members": int(g["totmembers"].sum()),
            "hired": int(g["tothired"].sum()),
            "summits": int(g["smtmembers"].sum()),
            "summitsHired": int(g["smthired"].sum()),
            "mDeaths": int(g["mdeaths"].sum()),
            "hDeaths": int(g["hdeaths"].sum()),
            "o2": int(g["o2used"].sum()),
            "daysMedian": q(days, .5),
        })

    decades = []
    for dec, g in e.groupby(e["year"] // 10 * 10):
        days = [v for v in g["smtdays"].tolist() if v == v and 5 <= v <= 130]
        decades.append({
            "decade": int(dec),
            "n": int(len(g)),
            "k": int(g["success1"].sum()),
            "members": int(g["totmembers"].sum()),
            "hired": int(g["tothired"].sum()),
            "summits": int(g["smtmembers"].sum()),
            "summitsHired": int(g["smthired"].sum()),
            "mDeaths": int(g["mdeaths"].sum()),
            "hDeaths": int(g["hdeaths"].sum()),
            "o2": int(g["o2used"].sum()),
            "daysMedian": q(days, .5),
        })

    # ---- 季节 × 年代 -------------------------------------------------------
    season_decade = []
    for (dec, season), g in e.groupby([e["year"] // 10 * 10, "season"]):
        season_decade.append({
            "decade": int(dec), "season": season,
            "n": int(len(g)), "k": int(g["success1"].sum()),
        })

    # ---- 时长分布 ----------------------------------------------------------
    durations = []
    for dec, g in e.groupby(e["year"] // 10 * 10):
        vals = [v for v in g["smtdays"].tolist() if v == v and 5 <= v <= 130]
        if len(vals) < 8:
            continue
        durations.append({
            "decade": int(dec), "n": len(vals),
            "p10": q(vals, .10), "p25": q(vals, .25), "p50": q(vals, .50),
            "p75": q(vals, .75), "p90": q(vals, .90),
        })
    total_days = []
    for dec, g in e.groupby(e["year"] // 10 * 10):
        vals = [v for v in g["totdays"].tolist() if v == v and 5 <= v <= 200]
        if len(vals) < 8:
            continue
        total_days.append({
            "decade": int(dec), "n": len(vals),
            "p10": q(vals, .10), "p25": q(vals, .25), "p50": q(vals, .50),
            "p75": q(vals, .75), "p90": q(vals, .90),
        })

    # ---- 营地剖面 ----------------------------------------------------------
    camp_order = {
        "South": ["BC", "C1", "C2", "C3", "C4", "Smt"],
        "North": ["BC", "ABC", "C1", "C2", "C3", "Smt"],
    }
    camp_names = {
        "BC": "Base Camp", "ABC": "Advanced BC", "C1": "Camp 1", "C2": "Camp 2",
        "C3": "Camp 3", "C4": "Camp 4", "Smt": "Summit",
    }
    camps = {}
    for side in ("South", "North"):
        rows = e[e["side"] == side]
        total = len(rows)
        parsed = [(r.year, P.parse_campsites({"campsites": r.campsites}))
                  for r in rows.itertuples()]
        series = []
        for label in camp_order[side]:
            elevs, dates, cnt = [], [], 0
            for _, cs in parsed:
                hit = [c for c in cs if c["label"] == label]
                if not hit:
                    continue
                cnt += 1
                for c in hit:
                    if c["elev"]:
                        elevs.append(c["elev"])
                    if c["date"]:
                        dates.append(c["date"])
            elev = PEAK_HEIGHT if label == "Smt" else (
                statistics.median(elevs) if elevs else None)
            series.append({
                "label": label,
                "name": camp_names[label],
                "elev": elev,
                "n": cnt,
                "share": round(cnt / total, 4) if total else None,
                "medianDate": sorted(dates)[len(dates) // 2] if dates else None,
            })
        camps[side.lower()] = series

    # ---- 头部卡片 ----------------------------------------------------------
    headline = {
        "expeditions": int(len(e)),
        "members": int(len(m)),
        "successfulExpeditions": int(e["success1"].sum()),
        "summitMembers": int(e["smtmembers"].sum()),
        "deaths": int(e["mdeaths"].sum() + e["hdeaths"].sum()),
        "years": [int(e["year"].min()), int(e["year"].max())],
    }

    data = {
        "meta": {
            "title": "Everest climbing decision support",
            "built": date.today().isoformat(),
            "source": {
                "name": "Maven Analytics · Himalayan Expeditions",
                "basedOn": "The Himalayan Database (Elizabeth Hawley)",
                "snapshot": "exped.csv dated 2025-04-29",
                "url": "https://mavenanalytics.io/data-playground/himalayan-expeditions",
            },
            "counts": {"expeditions": len(expeditions),
                       "expedition_rows": int(len(e)),
                       "member_rows": int(len(m))},
            "modelWindow": [MODEL_START, MODEL_END],
            "splits": {"train": [1990, 2014], "validation": [2015, 2019],
                       "test": [2020, 2024]},
            "checksums": {f.name: sha256(f) for f in
                          sorted(DATA_DIR.glob("*.csv"))},
            "caveats": [
                "The snapshot ends in 2024; the 2026 spring figures are a separate, "
                "clearly labelled layer and are not merged into any modelling data.",
                "The source has no camp coordinates or route geometry. The camp altitude "
                "profile is built from the campsite text field; the terrain view uses "
                "SRTM elevation and OpenStreetMap camp positions.",
                "Member-level year is taken from the expedition record because the "
                "member table's own year field disagrees with its expedition in 34.8% "
                "of rows (96% before 2000).",
            ],
        },
        "headline": headline,
        "expeditions": expeditions,
        "yearly": sorted(yearly, key=lambda d: d["year"]),
        "decades": sorted(decades, key=lambda d: d["decade"]),
        "seasonDecade": sorted(season_decade, key=lambda d: (d["decade"], d["season"])),
        "durations": durations,
        "totalDays": total_days,
        "camps": camps,
        "current": {
            "label": "2026 spring season (not in the historical dataset)",
            "items": [
                {"value": "1,008", "label": "successful Everest summits",
                 "note": "Nepal Department of Tourism, via Kathmandu Post, 29 May 2026"},
                {"value": "495", "label": "Everest permits issued",
                 "note": "390 men, 105 women, 56 countries (Radio Nepal, 10 June 2026)"},
                {"value": "899", "label": "previous season record in this dataset (2019)",
                 "note": "smtmembers + smthired, computed from exped.csv"},
                {"value": "Rs 1.26 bn", "label": "spring mountaineering royalties",
                 "note": "all peaks; Everest contributed the largest share (Radio Nepal)"},
            ],
            "sources": [
                {"title": "Everest spring climbing season sets new record with 1,008 successful summits",
                 "publisher": "The Kathmandu Post", "date": "2026-05-29",
                 "url": "https://kathmandupost.com/national/2026/05/29/everest-spring-climbing-season-sets-new-record-with-1-008-successful-summits"},
                {"title": "Spring climbing season concludes; Nepal earns Rs 1.26 billion in revenue",
                 "publisher": "Radio Nepal", "date": "2026-06-10",
                 "url": "https://radionepalonline.com/en/2026/06/10/431063.html"},
            ],
        },
    }

    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")),
                        encoding="utf-8")
    OUT_JS.write_text("window.EVEREST_DATA = " +
                      json.dumps(data, ensure_ascii=False, separators=(",", ":")) +
                      ";\n", encoding="utf-8")
    print(f"expeditions={len(expeditions)} yearly={len(yearly)} "
          f"decades={len(decades)} camps={len(camps['south'])+len(camps['north'])}")
    print(f"wrote {OUT_JSON.name} ({OUT_JSON.stat().st_size/1024:.0f} KB), "
          f"{OUT_JS.name} ({OUT_JS.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
