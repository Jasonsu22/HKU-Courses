#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为新增视图生成 data/plan_data.js（window.EVEREST_PLAN）：
  tuples     匿名化的队员聚合行（不含姓名），浏览器按任意条件重新汇总
  peakYears  各山峰逐年 expedition / 成功数（山峰对比图）
  expect     Python 端算好的期望值，供 ?selftest=1 对比
同时把 events.json 同步为浏览器直接加载的 events.js。
只读本地 CSV，不联网。
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

import prepare as P
import train_model as T

APP = Path(__file__).resolve().parent.parent
OUT = APP / "data" / "plan_data.js"
EVENTS_FILE = APP / "data" / "events.json"
EVENTS_OUT = APP / "data" / "events.js"
EVENTS = json.loads(EVENTS_FILE.read_text(encoding="utf-8"))

AGE = ["u30", "30s", "40s", "50s", "60p"]
SEX = ["M", "F"]
SEASON = ["Spring", "Autumn", "Winter", "Summer"]
SIDE = ["South", "North"]
ROUTE = ["standard", "other"]
TEAM = ["s", "m", "l"]
SUPPORT = ["lt05", "05to1", "1to2", "gt2"]
N_PEAKS = 8


def support_band(ratio: float) -> int:
    return 0 if ratio < .5 else 1 if ratio < 1 else 2 if ratio <= 2 else 3


def rate(df) -> dict:
    return {"n": int(len(df)), "k": int(df["y"].sum())}


def main() -> None:
    clean = P.prepare()
    d = T.member_dataset(clean, include_closure=True)
    d["team_i"] = np.where(d.totmembers <= 8, 0, np.where(d.totmembers <= 20, 1, 2))
    d["sup_i"] = [support_band(h / max(t, 1)) for h, t in zip(d.tothired, d.totmembers)]
    for col, levels in (("age", AGE), ("sex", SEX), ("season", SEASON), ("side", SIDE), ("route", ROUTE)):
        d[col + "_i"] = d[col].map({v: i for i, v in enumerate(levels)}).astype(int)
    keys = ["year", "age_i", "sex_i", "season_i", "side_i", "route_i", "o2", "team_i", "sup_i", "closure"]
    g = d.groupby(keys)["y"].agg(["size", "sum"]).reset_index()
    flat = []
    for r in g.itertuples(index=False):
        flat += [int(r.year), r.age_i, r.sex_i, r.season_i, r.side_i, r.route_i, int(r.o2), r.team_i,
                 r.sup_i, int(r.closure), int(r.size), int(r.sum)]

    # ---- 山峰对比 -------------------------------------------------------
    ex = clean["exped"]
    top = ex["peakid"].value_counts().head(N_PEAKS).index.tolist()
    names = clean["peaks"].set_index("peakid")["pkname"].to_dict()
    heights = clean["peaks"].set_index("peakid")["heightm"].to_dict()
    peaks = []
    for pid in top:
        v = ex[(ex.peakid == pid) & (ex.year >= 1975)]
        by = v.groupby("year")["success1"].agg(["size", "sum"])
        peaks.append({"id": pid, "name": names[pid], "height": int(heights[pid]),
                      "years": [[int(y), int(r["size"]), int(r["sum"])] for y, r in by.iterrows()]})

    # ---- 期望值（self-test + 故事里的数字） -------------------------------
    e, _ = P.everest(clean)
    era = lambda s, a, b: s[s.year.between(a, b)]
    def peak_rate(pid, a, b):
        v = ex[(ex.peakid == pid) & ex.year.between(a, b)]
        return {"n": int(len(v)), "k": int(v.success1.sum())}
    ee = lambda a, b: era(e, a, b)
    def risk(a, b):
        x = ee(a, b)
        return {"mDeaths": int(x.mdeaths.sum()), "hDeaths": int(x.hdeaths.sum()), "members": int(x.totmembers.sum()),
                "hired": int(x.tothired.sum()), "summits": int(x.smtmembers.sum() + x.smthired.sum())}
    live = d[~d.closure]
    default = live[(live.age == "30s") & (live.sex == "M") & (live.season == "Spring") & (live.side == "South")
                   & (live.route == "standard") & (live.o2 == 1) & live.totmembers.between(9, 20)]
    def reach(side, a, b, alt):
        x = ee(a, b)
        x = x[(x.side == side) & (x.route_group == "standard") & (x.highpoint > 0)]
        return {"n": int(len(x)), "k": int((x.highpoint >= alt).sum())}
    bc = pd.to_datetime(e.bcdate, errors="coerce").dt.day_of_year
    spring = e[(e.year >= 2005) & (e.season == "Spring") & (e.route_group == "standard") & bc.notna()]
    bc_s = bc[spring.index]
    bins = [(0, 95), (96, 105), (106, 115), (116, 366)]
    no2 = d[(d.year.between(2005, 2024)) & (d.o2 == 0)]
    def event_summary(window):
        x = ee(*window["range"])
        return {"n": int(len(x)), "k": int(x.success1.sum()),
                "members": int(x.totmembers.sum()), "hired": int(x.tothired.sum())}
    expect = {
        "tuples": {"rows": int(len(d)), "k": int(d.y.sum()), "closure": int(d.closure.sum())},
        "closureExpeditions": int(e.closure.sum()),
        "peaks": {p: {"early": peak_rate(p, 1900, 1989), "late": peak_rate(p, 2020, 2024)} for p in ["EVER", "LHOT", "BARU", "MANA"]},
        "risk": {"early": risk(1900, 1989), "tens": risk(2010, 2019), "late": risk(2020, 2024)},
        "hiredPerMember": {"nineties": risk(1990, 1999), "late": risk(2020, 2024)},
        "members2024": {s: rate(live[(live.side == s) & live.year.between(2020, 2024)]) for s in SIDE},
        "defaultByPeriod": {str(y): rate(default[default.year.between(y, y + 4)]) for y in range(1990, 2021, 5)},
        "reach": {"southEarly": reach("South", 1900, 1999, 8840), "southLate": reach("South", 2016, 2024, 8840),
                  "northEarly": reach("North", 1900, 1999, 8840), "northLate": reach("North", 2016, 2024, 8840)},
        "bcWindows": [{"lo": a, "hi": b, "n": int(bc_s.between(a, b).sum()), "k": int(spring[bc_s.between(a, b)].success1.sum())} for a, b in bins],
        "noOxygen": {"members": int(len(no2)), "summits": int(no2.y.sum()), "closure": int(no2.closure.sum())},
        "events": {event["id"]: [event_summary(w) for w in event["windows"]] for event in EVENTS},
    }
    out = {"levels": {"age": AGE, "sex": SEX, "season": SEASON, "side": SIDE, "route": ROUTE, "team": TEAM, "support": SUPPORT},
           "columns": keys + ["n", "k"], "tuples": flat, "peaks": peaks, "expect": expect}
    OUT.write_text("window.EVEREST_PLAN = " + json.dumps(out, separators=(",", ":"), ensure_ascii=False) + ";\n", encoding="utf-8")
    EVENTS_OUT.write_text("window.EVEREST_EVENTS = " + json.dumps(EVENTS, separators=(",", ":"), ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"tuples={len(g):,} rows={len(d):,} size={OUT.stat().st_size/1024:.0f} KB")
    print(json.dumps(expect, indent=0)[:3200])


if __name__ == "__main__":
    main()
