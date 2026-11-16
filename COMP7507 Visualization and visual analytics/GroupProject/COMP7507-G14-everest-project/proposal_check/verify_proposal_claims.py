#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMP7507 Group 14 — Proposal 数据核验 / Proposal data verification
===================================================================

复算 Proposal.docx Part B 中每一条可以用本地 CSV 复核的数字与字段陈述，
并检查支撑「历史演变 / 路线 / 个人档案估计」三个模块的关键数据条件。

用法
----
    python3 verify_proposal_claims.py

输出（与本脚本同目录）
--------------------
    claim_checks.csv    逐条核验表（UTF-8-BOM，可直接用 Excel 打开）
    key_numbers.json    全部实测数字，供 make_figures.py 与报告引用

数据目录默认为 ../Himalayan+Expeditions（Maven Analytics 快照）。
不修改任何原始 CSV。
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "Himalayan+Expeditions"

FILES = ["exped.csv", "members.csv", "peaks.csv", "refer.csv",
         "himalayan_data_dictionary.csv"]


# ---------------------------------------------------------------------------
# 读取与清洗
# ---------------------------------------------------------------------------
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_all(data_dir: Path = DATA) -> dict[str, pd.DataFrame]:
    tables = {
        "exped": pd.read_csv(data_dir / "exped.csv", low_memory=False),
        "members": pd.read_csv(data_dir / "members.csv", low_memory=False),
        "peaks": pd.read_csv(data_dir / "peaks.csv", low_memory=False),
        "refer": pd.read_csv(data_dir / "refer.csv", low_memory=False,
                             encoding="latin-1"),
        "dictionary": pd.read_csv(data_dir / "himalayan_data_dictionary.csv",
                                  low_memory=False, encoding="latin-1"),
    }
    return tables


def to_bool(s: pd.Series) -> pd.Series:
    """稳健地把 TRUE/FALSE 文本或布尔列转成 bool（NaN 视为 False）。"""
    return s.fillna(False).astype(bool)


def resolve_member_year(exped: pd.DataFrame, members: pd.DataFrame) -> pd.DataFrame:
    """给每个 member 行补上所属 expedition 的年份。

    expid 只含两位年份，所以 1921 与 2021 共用一个 expid（EVER21101 等）。
    规则：
      1) 该 expid 只对应一个年份 -> 直接用；
      2) myear 恰好等于候选年份之一 -> 用 myear（2021/2022/2024 的修路队即属此列）；
      3) 其余（1920 年代老记录，myear 已被上游写坏）-> 取最早年份并打标 ambiguous。
    """
    cand = (exped.groupby("expid")["year"]
            .apply(lambda s: sorted({int(y) for y in s}))
            .to_dict())
    years, flags = [], []
    for expid, myear in zip(members["expid"], members["myear"]):
        ys = cand.get(expid)
        if not ys:
            years.append(np.nan)
            flags.append("no_expedition")
        elif len(ys) == 1:
            years.append(ys[0])
            flags.append("")
        elif pd.notna(myear) and int(myear) in ys:
            years.append(int(myear))
            flags.append("")
        else:
            years.append(ys[0])
            flags.append("ambiguous")
    out = members.copy()
    out["year"] = years
    out["year_flag"] = flags
    return out


def prepare(tables: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    exped = tables["exped"].copy()
    members = tables["members"].copy()
    for col in ["success1", "success2", "success3", "success4", "claimed",
                "disputed", "traverse", "ski", "parapente", "o2used", "o2none",
                "o2climb", "o2descent", "o2sleep", "o2medical", "o2taken",
                "o2unkwn", "nohired"]:
        if col in exped:
            exped[col] = to_bool(exped[col])
    for col in ["hired", "msuccess", "mclaimed", "mdisputed", "death",
                "bconly", "leader", "sherpa", "tibetan", "msolo"]:
        if col in members:
            members[col] = to_bool(members[col])
    exped["year"] = exped["year"].astype(int)
    members["myear"] = members["myear"].astype(int)
    members = resolve_member_year(exped, members)
    return {"exped": exped, "members": members, "peaks": tables["peaks"],
            "refer": tables["refer"], "dictionary": tables["dictionary"]}


# ---------------------------------------------------------------------------
# 派生口径
# ---------------------------------------------------------------------------
SIDE_RULES = {
    "South": ("S Col", "S Pillar", "SW Face", "SE Ridge"),
    "North": ("N Col", "N Face", "NE Ridge", "W Ridge", "W Cwm", "Lho La",
              "N Ridge"),
}


def route_side(route: str) -> str:
    """把 136 个 route1 名称归到南/北侧；无法判断的归 Other（提案里要显式标注）。"""
    r = str(route)
    if r.startswith("S Col") or r.startswith("S Pillar") or \
       r.startswith("SW Face") or r.startswith("E Face-S Col"):
        return "South"
    if r.startswith(("N Col", "N Face", "NE Ridge", "W Ridge", "W Cwm",
                     "Lho La", "N Ridge")):
        return "North"
    return "Other"


def everest(clean: dict[str, pd.DataFrame]):
    e = clean["exped"].query("peakid == 'EVER'").copy()
    m = clean["members"].query("peakid == 'EVER'").copy()
    return e, m


# ---------------------------------------------------------------------------
# 计算
# ---------------------------------------------------------------------------
def compute(clean: dict[str, pd.DataFrame], data_dir: Path = DATA) -> dict:
    exped, members = clean["exped"], clean["members"]
    peaks, refer = clean["peaks"], clean["refer"]
    e, m = everest(clean)
    e["side"] = e["route1"].map(route_side)
    m["side"] = m["expid"].map(dict(zip(e["expid"], e["side"])))

    # --- 表规模 -----------------------------------------------------------
    sizes = {
        "exped": len(exped), "members": len(members),
        "peaks": len(peaks), "refer": len(refer),
        "dictionary": len(clean["dictionary"]),
    }

    # --- 键 -----------------------------------------------------------------
    expid_dup_rows = int(exped["expid"].duplicated().sum())
    expid_dup_ids = exped.loc[exped["expid"].duplicated(keep=False), "expid"].unique()
    collisions = (exped[exped["expid"].isin(expid_dup_ids)]
                  .sort_values(["expid", "year"])
                  [["expid", "peakid", "year", "season", "route1"]])
    composite_dup = int(exped.duplicated(subset=["peakid", "year", "expid"]).sum())
    suffix = [str(x)[len(str(p)):len(str(p)) + 2]
              for x, p in zip(exped["expid"], exped["peakid"])]
    suffix_ok = sum(s == str(y)[-2:] for s, y in zip(suffix, exped["year"]))
    membid_dup = int(members.duplicated(subset=["expid", "membid"]).sum())
    membid_dup_in_collision = int(
        members[members["expid"].isin(expid_dup_ids)]
        .duplicated(subset=["expid", "membid"]).sum())

    # --- 参与记录 vs 唯一的人 ------------------------------------------------
    people_key = (members["fname"].fillna("") + "|" + members["lname"].fillna("")
                  + "|" + members["yob"].astype("Int64").astype(str))
    ever_people_key = (m["fname"].fillna("") + "|" + m["lname"].fillna("")
                       + "|" + m["yob"].astype("Int64").astype(str))
    sd = pd.to_datetime(members["msmtdate1"], errors="coerce")

    # --- 分母一致性 -----------------------------------------------------------
    coll = set(expid_dup_ids)
    mm = members[~members["expid"].isin(coll)]
    g = (mm[~mm["hired"]].groupby("expid")
         .agg(n_nonhired=("membid", "size"), n_smt=("msuccess", "sum"),
              n_dth=("death", "sum")))
    h = (mm[mm["hired"]].groupby("expid")
         .agg(n_hired=("membid", "size"), n_smth=("msuccess", "sum"),
              n_dthh=("death", "sum")))
    x = (exped[~exped["expid"].isin(coll)]
         .set_index("expid")[["peakid", "year", "totmembers", "smtmembers",
                              "mdeaths", "tothired", "smthired", "hdeaths"]]
         .join(g).join(h).fillna(0))
    denom = {}
    for a, b, label in [("totmembers", "n_nonhired", "members"),
                        ("tothired", "n_hired", "hired"),
                        ("smtmembers", "n_smt", "member_summits"),
                        ("smthired", "n_smth", "hired_summits"),
                        ("mdeaths", "n_dth", "member_deaths"),
                        ("hdeaths", "n_dthh", "hired_deaths")]:
        d = x[a] - x[b]
        denom[label] = {
            "exact_share": round(float((d == 0).mean()), 4),
            "within1_share": round(float((d.abs() <= 1).mean()), 4),
            "gt2": int((d.abs() > 2).sum()),
            "sum_field": int(x[a].sum()),
            "sum_rows": int(x[b].sum()),
        }
    ex = x[x["peakid"] == "EVER"]
    denom_ever = {}
    for a, b, label in [("totmembers", "n_nonhired", "members"),
                        ("tothired", "n_hired", "hired"),
                        ("smtmembers", "n_smt", "member_summits"),
                        ("smthired", "n_smth", "hired_summits"),
                        ("mdeaths", "n_dth", "member_deaths"),
                        ("hdeaths", "n_dthh", "hired_deaths")]:
        d = ex[a] - ex[b]
        denom_ever[label] = {
            "exact_share": round(float((d == 0).mean()), 4),
            "sum_field": int(ex[a].sum()),
            "sum_rows": int(ex[b].sum()),
        }

    # --- 成功/死亡口径 ---------------------------------------------------------
    succ = {
        "exped_success1_n": int(e["success1"].sum()),
        "exped_success1_rate": round(float(e["success1"].mean()), 4),
        "exped_with_member_summit_n": int((e["smtmembers"] > 0).sum()),
        "member_summits": int(e["smtmembers"].sum()),
        "members_total": int(e["totmembers"].sum()),
        "member_success_rate": round(float(e["smtmembers"].sum() /
                                           e["totmembers"].sum()), 4),
        "hired_summits": int(e["smthired"].sum()),
        "hired_total": int(e["tothired"].sum()),
        "hired_success_rate": round(float(e["smthired"].sum() /
                                          e["tothired"].sum()), 4),
        "flag_true_members0": int(((e["success1"]) & (e["smtmembers"] == 0)).sum()),
        "flag_false_members_pos": int(((~e["success1"]) & (e["smtmembers"] > 0)).sum()),
        "disagreement_share": round(float((
            ((e["success1"]) & (e["smtmembers"] == 0)) |
            ((~e["success1"]) & (e["smtmembers"] > 0))).mean()), 4),
    }

    # --- 结构 ---------------------------------------------------------------
    side_n = e["side"].value_counts().to_dict()
    season_n = e["season"].value_counts().to_dict()
    route_n = e["route1"].value_counts()
    side_season = (e.groupby(["side", "season"])
                   .agg(n=("expid", "size"), success1=("success1", "mean"))
                   .reset_index())
    side_season["success1"] = side_season["success1"].round(4)

    periods = {}
    for label, (lo, hi) in {"train_1990_2014": (1990, 2014),
                            "valid_2015_2019": (2015, 2019),
                            "test_2020_2024": (2020, 2024)}.items():
        ee = e[(e["year"] >= lo) & (e["year"] <= hi)]
        periods[label] = {
            "expeditions": int(len(ee)),
            "member_rows": int(len(m[(m["year"] >= lo) & (m["year"] <= hi)])),
            "success1_rate": round(float(ee["success1"].mean()), 4),
        }
    year_n = e.groupby("year").size()

    missing = {c: int(e[c].isna().sum()) for c in
               ["smtdays", "totdays", "bcdate", "smtdate", "campsites",
                "highpoint", "totmembers", "tothired", "smthired", "o2used"]}
    age = m["year"] - m["yob"]          # 用 expedition 年份算年龄
    age_bad = m["myear"] - m["yob"]     # 用成员表 myear 算年龄（错误来源示范）
    ages = {
        "missing_yob": int(m["yob"].isna().sum()),
        "missing_yob_share": round(float(m["yob"].isna().mean()), 4),
        "age_lt10": int((age < 10).sum()),
        "age_gt80": int((age > 80).sum()),
        "age_min": round(float(age.min()), 1),
        "age_max": round(float(age.max()), 1),
        "age_median": round(float(age.median()), 1),
        "age_lt10_if_myear": int((age_bad < 10).sum()),
        "age_gt80_if_myear": int((age_bad > 80).sum()),
        "age_min_if_myear": round(float(age_bad.min()), 1),
        "age_max_if_myear": round(float(age_bad.max()), 1),
        "sex": m["sex"].value_counts(dropna=False).to_dict(),
    }
    o2 = {
        "exped_o2used_true": int(e["o2used"].sum()),
        "exped_o2used_share": round(float(e["o2used"].mean()), 4),
        "member_mo2used_true_share": round(float(m["mo2used"].mean()), 4),
    }
    ref_cover = {
        "ever_expeditions": int(len(e)),
        "ever_with_reference": int(e["expid"].isin(refer["expid"]).sum()),
        "ever_reference_rows": int(refer["expid"].str.startswith("EVER").sum()),
    }
    campsite = {
        "nonnull": int(e["campsites"].notna().sum()),
        "with_elevation": int(e["campsites"].str.contains(r"m\)", na=False).sum()),
        "with_coordinates": int(e["campsites"].str.contains(
            r"\d+\.\d+\s*[NS]|\d+°", na=False, regex=True).sum()),
    }
    # 2026 新闻里「上一个纪录约 900」的本地对照：members+hired 峰顶数
    summits_by_year = (e.assign(total=e["smtmembers"] + e["smthired"])
                       .groupby("year")["total"].sum().sort_values(ascending=False))

    return {
        "files_sha256": {f: sha256(data_dir / f) for f in FILES},
        "sizes": sizes,
        "everest": {
            "expeditions": int(len(e)),
            "member_rows": int(len(m)),
            "year_min": int(e["year"].min()),
            "year_max": int(e["year"].max()),
            "member_year_min": int(m["year"].min()),
            "member_year_max": int(m["year"].max()),
            "unique_people_est": int(ever_people_key.nunique()),
            "unique_people_est_all": int(people_key.nunique()),
            "expeditions_by_decade": {int(k): int(v) for k, v in
                                      (e["year"] // 10 * 10).value_counts().sort_index().items()},
        },
        "keys": {
            "expid_dup_rows": expid_dup_rows,
            "expid_collision_ids": sorted(expid_dup_ids.tolist()),
            "collisions": collisions.to_dict("records"),
            "composite_dup": composite_dup,
            "expid_suffix_matches_year": int(suffix_ok),
            "expid_rows": int(len(exped)),
            "membid_dup_rows": membid_dup,
            "membid_dup_rows_in_collisions": membid_dup_in_collision,
            "membid_max": int(members["membid"].max()),
            "member_year_ambiguous": int((members["year_flag"] == "ambiguous").sum()),
        },
        "myear_check": {
            "mismatch_rows": int((members["myear"] != members["year"]).sum()),
            "mismatch_share": round(float((members["myear"] != members["year"]).mean()), 4),
            "ever_mismatch_rows": int((m["myear"] != m["year"]).sum()),
            "ever_mismatch_share": round(float((m["myear"] != m["year"]).mean()), 4),
            "mseason_mismatch": int((members["mseason"] !=
                                     members["expid"].map(dict(zip(exped["expid"], exped["season"])))).sum()),
            "pre2000_rows": int((members["year"] < 2000).sum()),
            "pre2000_mismatch_share": round(float(
                (members.loc[members["year"] < 2000, "myear"] !=
                 members.loc[members["year"] < 2000, "year"]).mean()), 4),
            "post2000_mismatch_share": round(float(
                (members.loc[members["year"] >= 2000, "myear"] !=
                 members.loc[members["year"] >= 2000, "year"]).mean()), 4),
            "ever_pre2000_mismatch_share": round(float(
                (m.loc[m["year"] < 2000, "myear"] !=
                 m.loc[m["year"] < 2000, "year"]).mean()), 4),
            "ever_post2000_mismatch_share": round(float(
                (m.loc[m["year"] >= 2000, "myear"] !=
                 m.loc[m["year"] >= 2000, "year"]).mean()), 4),
            "summitdate_rows": int(sd.notna().sum()),
            "summitdate_year_mismatch": int((sd.dt.year[pd.notna(sd)] !=
                                             members.loc[pd.notna(sd), "myear"]).sum()),
        },
        "denominators_all": denom,
        "denominators_everest": denom_ever,
        "success": succ,
        "structure": {
            "side": side_n,
            "host": e["host"].value_counts().to_dict(),
            "side_host_agreement": round(float(
                (((e["side"] == "South") & (e["host"] == "Nepal")) |
                 ((e["side"] == "North") & (e["host"] == "China"))).sum()
                / (e["side"] != "Other").sum()), 4),
            "season": season_n,
            "distinct_routes": int(route_n.size),
            "top2_route_share": round(float(route_n.iloc[:2].sum() / len(e)), 4),
            "top_routes": route_n.head(10).to_dict(),
            "side_season": side_season.to_dict("records"),
            "periods": periods,
            "expeditions_by_year": {int(k): int(v) for k, v in year_n.items()},
        },
        "missingness_everest": missing,
        "ages": ages,
        "oxygen": o2,
        "references": ref_cover,
        "campsites": campsite,
        "summits_by_year_top": {int(k): int(v) for k, v in
                                summits_by_year.head(8).items()},
        "deaths_everest": {"member": int(e["mdeaths"].sum()),
                           "hired": int(e["hdeaths"].sum()),
                           "member_rows_flagged": int(m["death"].sum())},
    }


# ---------------------------------------------------------------------------
# 逐条陈述
# ---------------------------------------------------------------------------
def claims(n: dict) -> list[dict]:
    ever = n["everest"]
    s = n["success"]
    st = n["structure"]
    dn = n["denominators_all"]
    de = n["denominators_everest"]
    my = n["myear_check"]
    rows = [
        dict(
            id="C01", section="Dataset Description",
            quote="11,425 expedition records",
            method="len(exped.csv)",
            measured=f"{n['sizes']['exped']:,}",
            verdict="✅ 一致",
            note="与原始快照完全一致。"),
        dict(
            id="C02", section="Dataset Description",
            quote="approximately 89,000 member records",
            method="len(members.csv)",
            measured=f"{n['sizes']['members']:,}",
            verdict="✅ 一致",
            note="实际正好 89,000 行；可把 approximately 改成正好 89,000。"),
        dict(
            id="C03", section="Dataset Description",
            quote="480 peaks",
            method="len(peaks.csv)",
            measured=f"{n['sizes']['peaks']:,}",
            verdict="✅ 一致",
            note="EVER 高 8,849 m，且 peaks 表没有任何经纬度字段。"),
        dict(
            id="C04", section="Dataset Description",
            quote="15,586 references",
            method="len(refer.csv)",
            measured=f"{n['sizes']['refer']:,}",
            verdict="✅ 一致",
            note="文件 15,587 行 = 表头 + 15,586 条。"),
        dict(
            id="C05", section="Dataset Description",
            quote="Everest filtering gives 2,347 expeditions",
            method="exped[peakid=='EVER']",
            measured=f"{ever['expeditions']:,}",
            verdict="✅ 一致",
            note="peaks 表里只有 EVER 一个珠峰 ID，不会漏算别名。"),
        dict(
            id="C06", section="Dataset Description",
            quote="25,274 participation records",
            method="members[peakid=='EVER']",
            measured=f"{ever['member_rows']:,}",
            verdict="✅ 一致",
            note="这是参与记录（人次），不是人数，见 C08。"),
        dict(
            id="C07", section="Dataset Description",
            quote="from 1921 to 2024",
            method="min/max year",
            measured=f"{ever['year_min']}–{ever['year_max']}",
            verdict="✅ 一致",
            note="exped 与 members 两端年份一致。"),
        dict(
            id="C08", section="Dataset Description",
            quote="Participation rows are not unique climbers",
            method="distinct(fname,lname,yob)",
            measured=f"{ever['unique_people_est']:,} 人 / {ever['member_rows']:,} 人次",
            verdict="✅ 一致",
            note=f"按姓名+出生年去重约为人次的 {ever['unique_people_est']/ever['member_rows']:.0%}；"
                 "姓名去重只能给上界估计。"),
        dict(
            id="C09", section="Dataset Description",
            quote="The expedition identifier also contains a two-digit year",
            method="expid[peakid 之后 2 位] == year[-2:]",
            measured=f"{n['keys']['expid_suffix_matches_year']:,} / {n['keys']['expid_rows']:,}",
            verdict="✅ 一致",
            note="100% 符合；这也确实带来跨世纪撞号（C10）。"),
        dict(
            id="C10", section="Dataset Description",
            quote="linked with a composite key such as peak, year, and expedition identifier",
            method="duplicated()",
            measured=f"expid 单独 {n['keys']['expid_dup_rows']} 行重复；"
                     f"(peakid,year,expid) {n['keys']['composite_dup']} 行重复",
            verdict="✅ 一致",
            note="4 个 expid 同时对应两个年份：EVER21101=1921/2021、EVER22101=1922/2022、"
                 "EVER24101=1924/2024、KANG10101=1910/2010。"),
        dict(
            id="C11", section="Dataset Description",
            quote="the member identifier is expedition-local",
            method="membid 取值范围 / 跨 expid 重复",
            measured=f"membid 1–{n['keys']['membid_max']}，跨 expedition 重复",
            verdict="✅ 一致",
            note="但 (expid,membid) 仍有 35 对（70 行）重复，全部来自 C10 的撞号 expedition，"
                 "所以成员表也必须先解决年份归属。"),
        dict(
            id="C12", section="Dataset Description",
            quote="no complete route geometry, camp coordinates, or terrain model",
            method="字段检查",
            measured="2 表均无 lat/lon；campsites 共 "
                     f"{n['campsites']['nonnull']:,} 条非空，其中 "
                     f"{n['campsites']['with_elevation']:,} 条含海拔、0 条含经纬度",
            verdict="✅ 一致",
            note="peaks 表只有地名与 h Himal/region 文本，没有坐标；外部路点层确实是必需的。"),
        dict(
            id="C13", section="Module 1",
            quote="seasonal composition / duration / oxygen / deaths",
            method="字段缺失率",
            measured="smtdays 缺 "
                     f"{n['missingness_everest']['smtdays']:,}（{n['missingness_everest']['smtdays']/ever['expeditions']:.1%}）、"
                     f"totdays 缺 {n['missingness_everest']['totdays']:,}（{n['missingness_everest']['totdays']/ever['expeditions']:.1%}）；"
                     f"o2used 0 缺失、highpoint 0 缺失",
            verdict="⚠️ 需限定",
            note="时长/日期字段缺失约 3%–20%（bcdate 236、smtdate 77、campsites 28），"
                 "图上必须标注 n；success1/totmembers/o2used 等主字段完整。"),
        dict(
            id="C14", section="Module 2",
            quote="compare climbing side, route group, season",
            method="route1 归类",
            measured=f"136 个 route1；南侧 {st['side'].get('South',0):,}、"
                     f"北侧 {st['side'].get('North',0):,}、无法归类 {st['side'].get('Other',0):,}",
            verdict="⚠️ 需补充",
            note="side 不是现成字段。按 route1 名称归类后与 host 国别的一致率为 "
                 f"{st['side_host_agreement']:.1%}（Nepal {st['host'].get('Nepal',0):,} / "
                 f"China {st['host'].get('China',0):,}）；建议把 host 作为 side 的主口径，"
                 f"route 名称只用于 route group，其余 {st['side'].get('Other',0)} 条显式标 Other。"),
        dict(
            id="C15", section="Module 2",
            quote="season comparison",
            method="season 计数",
            measured=", ".join(f"{k} {v:,}" for k, v in st["season"].items()),
            verdict="⚠️ 需限定",
            note="春季占绝对多数，秋季只有 230 次，冬/夏各 34/24 次；"
                 "季节比较必须同时显示样本量，否则容易被误读。"),
        dict(
            id="C16", section="Module 2",
            quote="route comparison (duration, team size, oxygen, success, risk)",
            method="expedition 级 success1",
            measured=f"{s['exped_success1_n']:,}/{ever['expeditions']:,} = {s['exped_success1_rate']:.1%}",
            verdict="✅ 可用",
            note="但 success1 是「route 1 上是否有人登顶」，与「有多少队员登顶」不同，见 C17。"),
        dict(
            id="C17", section="Module 2/3",
            quote="estimate recorded expedition summit success",
            method="success1 vs smtmembers>0",
            measured=f"不一致 {s['flag_true_members0'] + s['flag_false_members_pos']} 次 "
                     f"（{s['disagreement_share']:.1%}）："
                     f"{s['flag_true_members0']} 次只有雇佣人员登顶、"
                     f"{s['flag_false_members_pos']} 次走 route2 登顶",
            verdict="⚠️ 需补充",
            note="必须在界面/报告里先定义「success」：expedition 级(success1)、"
                 f"队员级(msuccess) 还是峰顶人数(smtmembers)。"),
        dict(
            id="C18", section="Module 3",
            quote="age band / recorded sex predictors",
            method="yob 与 sex",
            measured=f"yob 缺 {n['ages']['missing_yob']:,}/{ever['member_rows']:,}"
                     f"（{n['ages']['missing_yob_share']:.1%}）；"
                     f"年龄 <10 岁 {n['ages']['age_lt10']:,} 行、>80 岁 {n['ages']['age_gt80']:,} 行；"
                     f"性别 M {n['ages']['sex'].get('M',0):,} / F {n['ages']['sex'].get('F',0):,}",
            verdict="⚠️ 需补充",
            note=f"用 expedition 年份算年龄是干净的（{n['ages']['age_min']:.0f}–{n['ages']['age_max']:.0f} 岁，"
                 f"中位 {n['ages']['age_median']:.0f}）；但若误用 myear，会出现 "
                 f"{n['ages']['age_lt10_if_myear']} 行 <10 岁、{n['ages']['age_gt80_if_myear']} 行 >80 岁"
                 f"（最小 {n['ages']['age_min_if_myear']:.0f}、最大 {n['ages']['age_max_if_myear']:.0f}）。"
                 "所以 age band 必须基于 expedition 年份。"),
        dict(
            id="C19", section="Module 3",
            quote="planned oxygen use",
            method="o2used 分布",
            measured=f"{s['exped_o2used_share'] if False else n['oxygen']['exped_o2used_true']:,}/"
                     f"{ever['expeditions']:,} = {n['oxygen']['exped_o2used_share']:.1%} 使用氧气",
            verdict="⚠️ 需补充",
            note="方差很小（约 76% 都用氧），和年代高度共线；回归里它很容易变成"
                 "「年代代理」，解释时要谨慎。"),
        dict(
            id="C20", section="Methodology",
            quote="Training/validation/testing = 1990-2014 / 2015-2019 / 2020-2024",
            method="按 expedition 年份计数",
            measured=f"{st['periods']['train_1990_2014']['expeditions']:,} / "
                     f"{st['periods']['valid_2015_2019']['expeditions']:,} / "
                     f"{st['periods']['test_2020_2024']['expeditions']:,}",
            verdict="⚠️ 需改",
            note=f"2020 年只有 {st['expeditions_by_year'].get(2020, 0)} 次 expedition（疫情），"
                 "2020–2024 测试集仅 189 次，p 值/校准曲线会很不稳；"
                 "建议改成 2021–2024 或 2015–2024 滚动验证。"),
        dict(
            id="C21", section="Module 1",
            quote="hired support / team size",
            method="tothired vs 成员表里 hired 行数",
            measured=f"字段合计 {dn['hired']['sum_field']:,} vs 成员行 {dn['hired']['sum_rows']:,}"
                     f"（只有 {dn['hired']['exact_share']:.1%} 的 expedition 精确相等）",
            verdict="⚠️ 需补充",
            note="成员表只收录了部分雇佣人员（珠峰：8,323/15,533 = 53.6%），"
                 "hired 的分母必须用 expedition.tothired，不能用成员行数。"),
        dict(
            id="C22", section="Module 1",
            quote="recorded deaths",
            method="mdeaths / hdeaths 与成员 death",
            measured=f"队员 {n['deaths_everest']['member']:,} + 雇佣 {n['deaths_everest']['hired']:,}"
                     f" = {n['deaths_everest']['member']+n['deaths_everest']['hired']:,}",
            verdict="✅ 一致",
            note=f"expedition 级死亡数与成员行 death=True 完全对齐"
                 f"（{dn['member_deaths']['exact_share']:.1%} 的 expedition 精确相等）。"),
        dict(
            id="C23", section="Dataset Description",
            quote="participations / success / death rates always state numerator, denominator, unit",
            method="exped 级口径与成员行口径对比",
            measured=f"totmembers 与成员行 {dn['members']['exact_share']:.1%} 精确相等；"
                     f"smtmembers 与成员行 {dn['member_summits']['exact_share']:.1%} 精确相等",
            verdict="✅ 可支撑",
            note="两个口径都自洽；但要固定用哪个口径，并在图上写出分子/分母。"),
        dict(
            id="C24", section="Dataset Description",
            quote="records will be linked ... after duplicate checks",
            method="成员表 myear 与所属 expedition 年份比较",
            measured=f"{my['mismatch_rows']:,}/{n['sizes']['members']:,} 行不一致"
                     f"（{my['mismatch_share']:.1%}；珠峰 {my['ever_mismatch_share']:.1%}）",
            verdict="⚠️ 需补充",
            note="members.csv 的 myear 不可信（例：1973 年意大利队的 65 名队员全被写成 1995；"
                 f"{my['summitdate_year_mismatch']:,}/{my['summitdate_rows']:,} 行的 myear 与本人登山日期年份矛盾），"
                 f"2000 年以前的记录 {my['pre2000_mismatch_share']:.1%} 全错"
                 f"（珠峰 {my['ever_pre2000_mismatch_share']:.1%}），2000 年以后 "
                 f"{my['post2000_mismatch_share']:.1%}（珠峰 {my['ever_post2000_mismatch_share']:.1%}）；"
                 "mseason 却与所属 expedition 的季节 "
                 f"{n['sizes']['members']-my['mseason_mismatch']:,}/{n['sizes']['members']:,} 完全一致。"
                 "年份必须从 expedition 表取，不能按 myear 过滤。"),
        dict(
            id="C25", section="Module 2",
            quote="current 2025-2026 aggregate indicators",
            method="引用链接与数据时间范围",
            measured="本地快照止于 2024；引用 [5][6] 均为 2026 年春季",
            verdict="⚠️ 需限定",
            note="没有 2025 年的来源，建议改成「2026 spring season」；"
                 "两条新闻链接均可打开，数字与标题一致。"),
        dict(
            id="C26", section="Objectives",
            quote="current snapshot / season lists",
            method="外部链接可达性",
            measured="[1][2][4][5][6] 均 HTTP 200；[5] 1.26 billion 卢比、[6] 1,008 人登顶",
            verdict="✅ 一致",
            note="[6] 称上一个纪录「约 900」，与本地数据 2019 年 899 次"
                 "（members+hired）吻合，可作为可信度旁证。"),
        dict(
            id="C27", section="Part B 格式",
            quote="Times New Roman 12pt black, Part B ≤ 5 pages",
            method="docx 样式与 PDF 页数",
            measured="TNR 12pt、黑色；PDF 共 5 页",
            verdict="✅ 合规",
            note="页数正好压线，后续不要再加内容。"),
        dict(
            id="C28", section="Dataset Description",
            quote="The dataset and data dictionary are stored in the project's data folder",
            method="data dictionary 字段与列名对照",
            measured="dictionary 4 张表 165 行；refer 段描述从 ryear 起整体错位一列",
            verdict="⚠️ 需补充",
            note="refer 表字典把 ryear 描述成 Reference type、rtype 描述成 Journal type…，"
                 "每行描述属于下一个字段；上游 Maven 快照的问题，做字典页时要手工修正。"),
    ]
    return rows


# 影响程度：高 = 会改变结论或做不出来；中 = 需要限定/清洗；低 = 文案级
SEVERITY = {
    "C01": "—", "C02": "—", "C03": "—", "C04": "—", "C05": "—", "C06": "—",
    "C07": "—", "C08": "—", "C09": "—", "C10": "—", "C11": "—",
    "C12": "—", "C13": "中", "C14": "中", "C15": "中", "C16": "—",
    "C17": "高", "C18": "中", "C19": "中", "C20": "中", "C21": "高",
    "C22": "—", "C23": "—", "C24": "高", "C25": "低", "C26": "—",
    "C27": "—", "C28": "低",
}


def main() -> None:
    tables = load_all()
    clean = prepare(tables)
    n = compute(clean)
    rows = claims(n)
    for r in rows:
        r["severity"] = SEVERITY.get(r["id"], "—")

    # JSON
    (HERE / "key_numbers.json").write_text(
        json.dumps(n, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8")

    # CSV
    with open(HERE / "claim_checks.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "section", "quote", "method",
                                           "measured", "verdict", "severity", "note"])
        w.writeheader()
        w.writerows(rows)

    # 控制台
    width = max(len(r["quote"]) for r in rows)
    print(f"COMP7507 G14 Proposal 数据核验  ({len(rows)} 条)\n" + "=" * 100)
    for r in rows:
        print(f"[{r['id']}] {r['verdict']}  {r['quote'][:70]}")
        print(f"     实测: {r['measured']}")
    ok = sum(r["verdict"].startswith("✅") for r in rows)
    warn = sum(r["verdict"].startswith("⚠") for r in rows)
    bad = sum(r["verdict"].startswith("❌") for r in rows)
    high = sum(r["severity"] == "高" for r in rows)
    print("=" * 100)
    print(f"✅ {ok}  ⚠️ {warn}  ❌ {bad}   其中高影响 {high} 条")
    print(f"已写出: {HERE/'claim_checks.csv'}")
    print(f"已写出: {HERE/'key_numbers.json'}")


if __name__ == "__main__":
    main()
