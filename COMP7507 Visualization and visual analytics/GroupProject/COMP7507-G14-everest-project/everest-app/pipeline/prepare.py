#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
共享数据准备层：读原始 CSV → 清洗 → 派生字段。

关键规则（与 proposal_check/ 的核验结论一致）：
1. expid 只含两位年份，1921/2021 之类的跨世纪撞号必须用 (peakid, year, expid) 区分；
   成员表的 myear 在 2000 年前几乎全错，所以成员年份一律从 expedition 表取。
2. 4 个撞号 expid 里，现代队伍（2021/2022/2024）的 myear 是对的；
   旧队伍（1921/1922/1924）则退回到较早年份，并标记 ambiguous。
3. climbing side 用 host（Nepal = South，China = North）；route1 只用来做
   standard / other 的 route group。
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent.parent / "Himalayan+Expeditions"

AGE_BANDS = ["under 30", "30–39", "40–49", "50–59", "60+"]
AGE_KEYS = ["u30", "30s", "40s", "50s", "60p"]
SEASONS = ["Spring", "Autumn", "Winter", "Summer"]
TEAM_BANDS = ["≤ 8", "9–20", "> 20"]
TEAM_KEYS = ["s", "m", "l"]


def to_bool(s: pd.Series) -> pd.Series:
    return s.fillna(False).astype(bool)


def load_raw(data_dir: Path = DATA) -> dict[str, pd.DataFrame]:
    return {
        "exped": pd.read_csv(data_dir / "exped.csv", low_memory=False),
        "members": pd.read_csv(data_dir / "members.csv", low_memory=False),
        "peaks": pd.read_csv(data_dir / "peaks.csv", low_memory=False),
        "refer": pd.read_csv(data_dir / "refer.csv", low_memory=False,
                             encoding="latin-1"),
    }


def resolve_member_year(exped: pd.DataFrame, members: pd.DataFrame) -> pd.Series:
    cand = (exped.groupby("expid")["year"]
            .apply(lambda s: sorted({int(y) for y in s})).to_dict())
    years = []
    for expid, myear in zip(members["expid"], members["myear"]):
        ys = cand.get(expid, [])
        if not ys:
            years.append(np.nan)
        elif len(ys) == 1:
            years.append(ys[0])
        elif pd.notna(myear) and int(myear) in ys:
            years.append(int(myear))
        else:
            years.append(ys[0])
    return pd.Series(years, index=members.index, name="year")


def side_of_host(host: str) -> str:
    return "North" if str(host).strip().lower() == "china" else "South"


def route_group(route: str, side: str) -> str:
    r = str(route)
    if side == "South" and r.startswith("S Col-SE Ridge"):
        return "standard"
    if side == "North" and r.startswith("N Col-NE Ridge"):
        return "standard"
    return "other"


def route_family(route: str) -> str:
    """按 route1 的起始名称归成可比较的路线族（命名透明，写在界面上）。"""
    s = str(route).strip()
    if s.startswith(("S Col", "S Pillar", "SE Ridge", "S Sol")):
        return "South: S Col–SE Ridge"
    if s.startswith(("N Col", "NE Ridge")):
        return "North: N Col–NE Ridge"
    if s.startswith("SW Face"):
        return "South: SW Face"
    if s.startswith("N Face"):
        return "North: N Face"
    if s.startswith(("Lho La", "W Ridge", "W Cwm")):
        return "West shoulder / Lho La"
    if s.startswith("E Face"):
        return "East Face"
    if s.startswith(("W, N & E", "Khumbu", "W Rongbuk", "E Rongbuk", "E Ridge")):
        return "Early / reconnaissance"
    return "Other"


CLIMBING_HINTS = ("climb", "leader", "guide", "member", "sirdar")


# 2014 年 Sherpa 罢工/雪崩、2015 年地震导致整季中止。这些队伍往往还没到需要用氧的高度，
# 被记录成"未用氧 + 未登顶"，会把氧气系数抬高；规则只依据数据集自带的 termnote 字段。
CLOSURE_RE = re.compile(r"earthquake|strike|avalanche", re.I)


def is_closure(year: int, success: bool, note) -> bool:
    return (year in (2014, 2015) and not success
            and isinstance(note, str) and bool(CLOSURE_RE.search(note)))


def end_category(reason, closure: bool) -> str:
    """把 15 个 termreason 归成 7 类（图上最多 7 个颜色）。"""
    if closure:
        return "Season closure"
    r = str(reason)
    if r.startswith("Success"):
        return "Summit"
    if r.startswith(("Bad weather", "Bad conditions")):
        return "Weather & conditions"
    if r.startswith("Illness"):
        return "Illness & exhaustion"
    if r.startswith("Accident"):
        return "Accident"
    if r.startswith(("Lack", "Route technically", "Did not")):
        return "Logistics & difficulty"
    return "Other / unknown"


def clean_agency(a) -> str | None:
    """'Asian Trekking (Climbalaya pmt)' -> 'Asian Trekking'；多家时取第一家。"""
    if not isinstance(a, str) or not a.strip():
        return None
    s = re.sub(r"\(.*?\)", "", a).split("/")[0].strip()
    return s or None


def is_climbing_status(status: str) -> bool:
    s = str(status).lower()
    return any(h in s for h in CLIMBING_HINTS)


def age_band(age: float) -> str:
    if age != age:
        return ""
    if age < 30:
        return "u30"
    if age < 40:
        return "30s"
    if age < 50:
        return "40s"
    if age < 60:
        return "50s"
    return "60p"


def team_band(n: float) -> str:
    if n != n:
        return ""
    if n <= 8:
        return "s"
    if n <= 20:
        return "m"
    return "l"


def prepare(data_dir: Path = DATA) -> dict[str, pd.DataFrame]:
    raw = load_raw(data_dir)
    exped = raw["exped"].copy()
    members = raw["members"].copy()

    for col in ["success1", "o2used"]:
        if col in exped:
            exped[col] = to_bool(exped[col])
    for col in ["hired", "msuccess", "death", "bconly"]:
        if col in members:
            members[col] = to_bool(members[col])

    exped["year"] = exped["year"].astype(int)
    for c in ["totmembers", "tothired", "smtmembers", "smthired", "mdeaths",
              "hdeaths", "smtdays", "totdays", "highpoint"]:
        exped[c] = pd.to_numeric(exped[c], errors="coerce")

    exped["side"] = exped["host"].map(side_of_host)
    exped["route"] = exped["route1"].fillna("Unknown route").astype(str)
    exped["route_group"] = [route_group(r, s)
                            for r, s in zip(exped["route"], exped["side"])]
    exped["route_family"] = exped["route"].map(route_family)
    exped["uid"] = exped["expid"] + "-" + exped["year"].astype(str)
    exped["closure"] = [is_closure(y, s, n) for y, s, n in
                        zip(exped["year"], exped["success1"], exped["termnote"])]
    exped["end_cat"] = [end_category(r, c) for r, c in
                        zip(exped["termreason"], exped["closure"])]
    exped["agency_clean"] = exped["agency"].map(clean_agency)

    members["year"] = resolve_member_year(exped, members)
    members["myear_ok"] = members["myear"] == members["year"]

    # 把 expedition 级上下文并到成员行（复合键，一年一行，many_to_one）
    ctx = exped[["peakid", "year", "expid", "season", "side", "route_group",
                 "totmembers", "tothired", "o2used", "success1", "closure"]] \
        .rename(columns={"season": "exp_season"})
    members = members.merge(ctx, on=["peakid", "year", "expid"],
                            how="left", validate="many_to_one")
    members["status_group"] = np.where(
        members["status"].map(is_climbing_status), "climbing", "other")
    members["age"] = members["year"] - members["yob"]
    members["age_band"] = members["age"].map(age_band)
    members["team_band"] = members["totmembers"].map(team_band)

    return {"exped": exped, "members": members,
            "peaks": raw["peaks"], "refer": raw["refer"]}


def everest(clean: dict[str, pd.DataFrame]):
    e = clean["exped"].query("peakid == 'EVER'").copy()
    m = clean["members"].query("peakid == 'EVER'").copy()
    return e, m


# ---------------------------------------------------------------------------
# campsites 解析："BC(04/04,5350m),C1(11/04,6100m),C2(08/05)…"
# ---------------------------------------------------------------------------
CAMP_ORDER_SOUTH = ["BC", "IC", "C1", "C2", "C3", "C4", "C5", "Smt"]
CAMP_ORDER_NORTH = ["BC", "ABC", "C1", "C2", "C3", "C4", "C5", "C6", "Smt"]
CAMP_LABELS = {"BC", "ABC", "IC", "C1", "C2", "C3", "C4", "C5", "C6", "C7",
               "Smt", "CBC"}
ELEV_RE = re.compile(r"(\d{4,5})\s*m")


def parse_campsites(row) -> list[dict]:
    """返回 [{label, elev, date}]；只保留已知营地标签与合法海拔。"""
    s = row["campsites"] if isinstance(row, dict) else row["campsites"]
    if not isinstance(s, str) or not s.strip():
        return []
    out = []
    for m in re.finditer(r"([A-Za-z]{1,4}\d?)\s*(?:\(([^)]*)\))?", s):
        label = m.group(1)
        if label not in CAMP_LABELS:
            continue
        inner = m.group(2) or ""
        elev = None
        em = ELEV_RE.search(inner)
        if em:
            v = int(em.group(1))
            if 4000 <= v <= 8900:
                elev = v
        date = None
        dm = re.search(r"(\d{1,2})-(\d{1,2})/(\d{1,2})|(\d{1,2})/(\d{1,2})", inner)
        if dm:
            day = int(dm.group(1) or dm.group(4))
            month = int(dm.group(3) or dm.group(5))
            if 1 <= day <= 31 and 1 <= month <= 12:
                date = f"{month:02d}-{day:02d}"
        out.append({"label": label, "elev": elev, "date": date})
    return out
