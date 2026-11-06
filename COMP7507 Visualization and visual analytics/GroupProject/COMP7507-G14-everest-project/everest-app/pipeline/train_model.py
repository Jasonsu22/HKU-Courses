#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模块三模型：正则化 logistic regression + 基线 + 时间切分评估 + bootstrap 不确定性。

两个模型：
  member      —— 队员级：这名有该档案的登山者登顶的概率（主估计）
  expedition  —— expedition 级：这样的队伍"有人登顶 route 1"的概率（背景信息）

输出 data/model.js / data/model.json 供浏览器端做点乘预测。
"""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

import prepare as P

HERE = Path(__file__).resolve().parent
APP = HERE.parent
OUT_JSON = APP / "data" / "model.json"
OUT_JS = APP / "data" / "model.js"

START, END = 1990, 2024
DEPLOY = (2005, 2024)   # 部署模型只用近 20 个赛季：1990s 的成功率完全是另一个量级
SPLITS = {"train": (1990, 2014), "validation": (2015, 2019), "test": (2020, 2024)}
LAMBDAS = [1.0, 3.0, 10.0]
SEED = 20261017


# ---------------------------------------------------------------------------
# 数值工具
# ---------------------------------------------------------------------------
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -35, 35)))


def fit_logistic(X, y, lam):
    p = X.shape[1]
    beta = np.zeros(p)
    pen = np.eye(p) * lam
    pen[0, 0] = 0.0
    for _ in range(80):
        mu = sigmoid(X @ beta)
        w = np.clip(mu * (1 - mu), 1e-8, None)
        H = X.T @ (X * w[:, None]) + pen
        g = X.T @ (y - mu) - pen @ beta
        step = np.linalg.solve(H, g)
        beta = beta + step
        if np.max(np.abs(step)) < 1e-9:
            break
    return beta


def logloss(y, p):
    p = np.clip(p, 1e-9, 1 - 1e-9)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def brier(y, p):
    return float(np.mean((y - p) ** 2))


def auc(y, p):
    n1 = int(y.sum())
    n0 = len(y) - n1
    if n1 == 0 or n0 == 0:
        return None
    order = np.argsort(p, kind="mergesort")
    ranks = np.empty(len(p))
    ranks[order] = np.arange(1, len(p) + 1)
    ps = p[order]
    i = 0
    while i < len(ps):
        j = i
        while j + 1 < len(ps) and ps[j + 1] == ps[i]:
            j += 1
        if j > i:
            ranks[order[i:j + 1]] = (i + 1 + j + 1) / 2.0
        i = j + 1
    return float((ranks[y == 1].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def calibration(y, p, bins=10):
    out = []
    edges = np.linspace(0, 1, bins + 1)
    for i in range(bins):
        lo, hi = edges[i], edges[i + 1]
        mask = (p >= lo) & (p < hi) if i < bins - 1 else (p >= lo) & (p <= hi)
        n = int(mask.sum())
        if n == 0:
            out.append({"bin": [round(float(lo), 3), round(float(hi), 3)],
                        "n": 0, "predicted": None, "observed": None})
            continue
        out.append({"bin": [round(float(lo), 3), round(float(hi), 3)],
                    "n": n, "predicted": round(float(p[mask].mean()), 4),
                    "observed": round(float(y[mask].mean()), 4)})
    return out


def metrics(y, p):
    return {"n": int(len(y)), "events": int(y.sum()),
            "brier": round(brier(y, p), 4), "logloss": round(logloss(y, p), 4),
            "auc": None if auc(y, p) is None else round(auc(y, p), 4)}


# ---------------------------------------------------------------------------
# 设计矩阵
# ---------------------------------------------------------------------------
MEMBER_SPEC = [
    ("age", "30s"), ("age", "40s"), ("age", "50s"), ("age", "60p"),
    ("sex", "F"),
    ("season", "Autumn"), ("season", "Winter"), ("season", "Summer"),
    ("side", "North"),
    ("route", "other"),
    ("team_log", None),
    ("support_log", None),
    ("o2", 1),
]
EXPED_SPEC = [
    ("season", "Autumn"), ("season", "Winter"), ("season", "Summer"),
    ("side", "North"),
    ("route", "other"),
    ("team_log", None),
    ("support_log", None),
    ("o2", 1),
]


def numeric_series(df, key):
    if key == "team_log":
        return np.log(df["totmembers"].clip(lower=1).astype(float))
    if key == "support_log":
        ratio = df["tothired"].fillna(0) / df["totmembers"].clip(lower=1)
        return np.log1p(ratio.astype(float))
    raise KeyError(key)


def build_columns(df, spec, stats=None):
    cols, meta = [], []
    for group, level in spec:
        if level is None:
            raw = numeric_series(df, group)
            if stats is None:
                stats = {}
            if group not in stats:
                stats[group] = {"mean": float(np.mean(raw)), "sd": float(np.std(raw))}
            v = (raw - stats[group]["mean"]) / (stats[group]["sd"] or 1.0)
            cols.append(np.asarray(v, dtype=float))
            meta.append({"kind": "numeric", "group": group, "key": group,
                         "mean": round(stats[group]["mean"], 6),
                         "sd": round(stats[group]["sd"], 6)})
        else:
            v = (df[group] == level).astype(float).values
            cols.append(v)
            meta.append({"kind": "onehot", "group": group, "level": level})
    return cols, meta, stats


def design(df, spec, stats=None):
    cols, meta, stats = build_columns(df, spec, stats)
    X = np.column_stack([np.ones(len(df))] + cols)
    return X, meta, stats


def feature_labels(meta):
    labels = {
        "age": "Age band", "sex": "Sex", "season": "Season", "side": "Side",
        "route": "Route", "team_log": "Team size (log, per SD)",
        "support_log": "Hired support per member (log, per SD)",
        "o2": "Oxygen planned",
    }
    for m in meta:
        m["label"] = labels.get(m["group"], m["group"])
    return meta


# ---------------------------------------------------------------------------
# 数据集
# ---------------------------------------------------------------------------
def member_dataset(clean, include_closure=False):
    m = clean["members"]
    if not include_closure:
        m = m[~m["closure"].fillna(False).astype(bool)]
    m = m[(m["peakid"] == "EVER") & m["year"].between(START, END)]
    m = m[(~m["hired"]) & (m["status_group"] == "climbing")]
    m = m[m["sex"].isin(["M", "F"])]
    m = m[m["yob"].notna() & m["age"].between(15, 80)]
    m = m[m["totmembers"].fillna(0) > 0]
    m = m[m["msuccess"].notna()]
    df = pd.DataFrame({
        "year": m["year"].astype(int),
        "y": m["msuccess"].astype(int),
        "age": m["age_band"],
        "sex": m["sex"],
        "season": m["exp_season"],
        "side": m["side"],
        "route": m["route_group"],
        "o2": np.where(m["o2used"], 1, 0),
        "team": m["totmembers"].fillna(0).astype(float),
        "hired": m["tothired"].fillna(0).astype(float),
        "totmembers": m["totmembers"].fillna(0).astype(float),
        "tothired": m["tothired"].fillna(0).astype(float),
        "closure": m["closure"].fillna(False).astype(bool),
    })
    return df.reset_index(drop=True)


def expedition_dataset(clean):
    e = clean["exped"]
    e = e[(e["peakid"] == "EVER") & e["year"].between(START, END)]
    e = e[e["totmembers"].fillna(0) > 0]
    e = e[e["success1"].notna()]
    e = e[~e["closure"]]
    return pd.DataFrame({
        "year": e["year"].astype(int),
        "y": e["success1"].astype(int),
        "season": e["season"],
        "side": e["side"],
        "route": e["route_group"],
        "o2": np.where(e["o2used"], 1, 0),
        "team": e["totmembers"].astype(float),
        "hired": e["tothired"].fillna(0).astype(float),
        "totmembers": e["totmembers"].astype(float),
        "tothired": e["tothired"].fillna(0).astype(float),
    }).reset_index(drop=True)


def subset(df, lo, hi):
    return df[(df["year"] >= lo) & (df["year"] <= hi)]


# ---------------------------------------------------------------------------
# 训练 + 评估
# ---------------------------------------------------------------------------
def train_and_evaluate(df, spec, label):
    tr = subset(df, *SPLITS["train"])
    va = subset(df, *SPLITS["validation"])
    te = subset(df, *SPLITS["test"])
    Xtr, meta, stats = design(tr, spec)
    ytr = tr["y"].values.astype(float)

    # 固定基线（只用训练集比例）
    base_const = float(ytr.mean())
    rates = tr.groupby(["side", "season"])["y"].mean()
    base_rate = {k: float(v) for k, v in rates.items()}

    def p_side_season(d):
        return np.array([base_rate.get((s, q), base_const)
                         for s, q in zip(d["side"], d["season"])])

    # 用验证集选 lambda
    best = None
    for lam in LAMBDAS:
        beta = fit_logistic(Xtr, ytr, lam)
        Xva, _, _ = design(va, spec, stats)
        ll = logloss(va["y"].values, sigmoid(Xva @ beta))
        if best is None or ll < best[0]:
            best = (ll, lam)
    lam = best[1]
    beta = fit_logistic(Xtr, ytr, lam)

    out = {"lambda": lam, "features": feature_labels(meta),
           "metrics": {"constant": {}, "sideSeason": {}, "model": {}}}
    for name, d in (("train", tr), ("validation", va), ("test", te)):
        X, _, _ = design(d, spec, stats)
        y = d["y"].values.astype(float)
        out["metrics"]["constant"][name] = metrics(y, np.full(len(y), base_const))
        out["metrics"]["sideSeason"][name] = metrics(y, p_side_season(d))
        out["metrics"]["model"][name] = metrics(y, sigmoid(X @ beta))
        if name == "test":
            out["calibration"] = calibration(y, sigmoid(X @ beta))

    # ---- 部署模型：近 20 个赛季重训（评估仍用上面的时间切分） -------------
    dep = df[df["year"].between(*DEPLOY)]
    Xall, meta_all, stats_all = design(dep, spec)
    yall = dep["y"].values.astype(float)
    beta_all = fit_logistic(Xall, yall, lam)

    rng = np.random.default_rng(SEED)
    n = len(dep)
    boots = np.vstack([fit_logistic(Xall[idx], yall[idx], lam)
                       for idx in (rng.integers(0, n, n) for _ in range(300))])

    out.update({
        "features": feature_labels(meta_all),
        "coef": [round(float(b), 6) for b in beta_all],
        "intercept": round(float(beta_all[0]), 6),
        "stats": {k: {"mean": round(v["mean"], 6), "sd": round(v["sd"], 6)}
                  for k, v in stats_all.items()},
        "n": int(len(dep)),
        "deployWindow": list(DEPLOY),
        "evalWindow": [START, END],
        "trainN": int(len(tr)), "validationN": int(len(va)),
        "testN": int(len(te)),
        "events": int(yall.sum()),
        "baseRate": round(float(yall.mean()), 4),
        "trainBaseRate": round(base_const, 4),
        "boot": [[round(float(v), 5) for v in row] for row in boots],
        "calibrationAll": calibration(yall, sigmoid(Xall @ beta_all)),
    })
    return out


# ---------------------------------------------------------------------------
# 可比样本 cells
# ---------------------------------------------------------------------------
def cells(df, keyfunc, name):
    out = []
    for key, g in df.groupby(keyfunc(df)):
        out.append([key, int(len(g)), int(g["y"].sum())])
    out.sort(key=lambda r: (-r[1], r[0]))
    return {name: out}


def run():
    clean = P.prepare()
    mem = member_dataset(clean)
    exp = expedition_dataset(clean)

    print(f"member model rows={len(mem):,} events={int(mem['y'].sum()):,} "
          f"rate={mem['y'].mean():.3f}")
    print(f"expedition model rows={len(exp):,} events={int(exp['y'].sum()):,} "
          f"rate={exp['y'].mean():.3f}")

    m = train_and_evaluate(mem, MEMBER_SPEC, "member")
    x = train_and_evaluate(exp, EXPED_SPEC, "expedition")

    # cells（与部署模型同窗口，供"可比历史样本"显示）
    def cell_table(d: pd.DataFrame, keys: pd.Series) -> list:
        agg = pd.DataFrame({"key": keys.values, "y": d["y"].values}) \
            .groupby("key")["y"].agg(["size", "sum"])
        return [[k, int(r["size"]), int(r["sum"])]
                for k, r in agg.iterrows()]

    def team_key(v: pd.Series) -> pd.Series:
        return pd.Series(np.where(v <= 8, "s", np.where(v <= 20, "m", "l")),
                         index=v.index)

    mem = mem[mem["year"].between(*DEPLOY)].reset_index(drop=True)
    exp = exp[exp["year"].between(*DEPLOY)].reset_index(drop=True)
    mem_band = team_key(mem["totmembers"])
    m["cellExactKey"] = ("age|sex|season|side|route|o2|team")
    m["cellBroadKey"] = ("age|sex|season|side")
    exact_m = (mem["age"] + "|" + mem["sex"] + "|" + mem["season"] + "|" +
               mem["side"] + "|" + mem["route"] + "|" +
               mem["o2"].astype(str) + "|" + mem_band)
    broad_m = (mem["age"] + "|" + mem["sex"] + "|" + mem["season"] + "|" +
               mem["side"])
    mid_m = (mem["age"] + "|" + mem["sex"] + "|" + mem["season"] + "|" +
             mem["side"] + "|" + mem["o2"].astype(str))
    m["cells"] = {"exact": cell_table(mem, exact_m),
                  "mid": cell_table(mem, mid_m),
                  "broad": cell_table(mem, broad_m)}

    exp_band = team_key(exp["totmembers"])
    x["cellExactKey"] = "season|side|route|o2|team"
    x["cellBroadKey"] = "season|side"
    exact_x = (exp["season"] + "|" + exp["side"] + "|" + exp["route"] + "|" +
               exp["o2"].astype(str) + "|" + exp_band)
    broad_x = exp["season"] + "|" + exp["side"]
    mid_x = exp["season"] + "|" + exp["side"] + "|" + exp["o2"].astype(str)
    x["cells"] = {"exact": cell_table(exp, exact_x),
                  "mid": cell_table(exp, mid_x),
                  "broad": cell_table(exp, broad_x)}

    # ---- self-test：把 Python 端算好的期望值写进 JSON，浏览器端可以自检 ----
    def profile_predict(model, prof):
        x = [1.0]
        for f in model["features"]:
            if f["kind"] == "onehot":
                x.append(1.0 if prof.get(f["group"]) == f["level"] else 0.0)
            elif f["group"] == "team_log":
                x.append((np.log(max(prof["team"], 1)) - f["mean"]) / f["sd"])
            else:
                x.append((np.log1p(prof["hired"] / max(prof["team"], 1)) - f["mean"]) / f["sd"])
        z = float(np.dot(model["coef"], x))
        return 1.0 / (1.0 + np.exp(-z))

    def team_key(t):
        return "s" if t <= 8 else "m" if t <= 20 else "l"

    selftest_profiles = [
        ("default", dict(age="30s", sex="M", season="Spring", side="South",
                         route="standard", team=12, hired=20, o2=1)),
        ("older, no oxygen", dict(age="60p", sex="M", season="Spring", side="South",
                                  route="standard", team=12, hired=20, o2=0)),
        ("north autumn", dict(age="40s", sex="F", season="Autumn", side="North",
                              route="standard", team=10, hired=15, o2=1)),
        ("non-standard route", dict(age="30s", sex="M", season="Spring", side="South",
                                    route="other", team=8, hired=10, o2=1)),
    ]
    selftest = {"profiles": [], "cells": {}}
    for name, prof in selftest_profiles:
        mkey = "|".join([prof["age"], prof["sex"], prof["season"], prof["side"],
                         prof["route"], str(prof["o2"]), team_key(prof["team"])])
        xkey = "|".join([prof["season"], prof["side"], prof["route"],
                         str(prof["o2"]), team_key(prof["team"])])
        mcell = dict((k, (n, kk)) for k, n, kk in m["cells"]["exact"]).get(mkey)
        xcell = dict((k, (n, kk)) for k, n, kk in x["cells"]["exact"]).get(xkey)
        selftest["profiles"].append({
            "name": name,
            "profile": prof,
            "member": round(profile_predict(m, prof), 5),
            "expedition": round(profile_predict(x, prof), 5),
            "memberCell": None if not mcell else {"n": mcell[0], "k": mcell[1]},
            "expeditionCell": None if not xcell else {"n": xcell[0], "k": xcell[1]},
        })
    e_all = clean["exped"].query("peakid == 'EVER'")
    m_all = clean["members"].query("peakid == 'EVER'")
    selftest["counts"] = {
        "expeditions": int(len(e_all)),
        "successful": int(e_all["success1"].sum()),
        "deaths": int(e_all["mdeaths"].sum() + e_all["hdeaths"].sum()),
        "memberRows": int(len(m_all)),
    }

    # 记录排除整季中止前后氧气系数的变化，界面和报告都要说明
    def o2_coef(frame):
        dep = frame[frame["year"].between(*DEPLOY)]
        X, meta, _ = design(dep, MEMBER_SPEC)
        beta = fit_logistic(X, dep["y"].values.astype(float), m["lambda"])
        i = [j for j, f in enumerate(meta) if f["group"] == "o2"][0]
        return round(float(beta[i + 1]), 4)
    with_closure = member_dataset(clean, include_closure=True)
    closure_effect = {"o2CoefWith": o2_coef(with_closure),
                      "o2CoefWithout": o2_coef(with_closure[~with_closure["closure"]])}

    models = {
        "selftest": selftest,
        "meta": {
            "deployWindow": list(DEPLOY),
            "built": date.today().isoformat(),
            "window": [START, END],
            "splits": SPLITS,
            "lambdaGrid": LAMBDAS,
            "seed": SEED,
            "bootstrap": 300,
            "targets": {
                "member": "member reached the summit on this expedition (msuccess)",
                "expedition": "at least one climber reached the summit on route 1 (success1)",
            },
            "population": {
                "member": "non-hired climbing members, 1990–2024, age 15–80, recorded sex M/F",
                "expedition": "Everest expeditions 1990–2024 with at least one member",
            },
            "note": "Post-expedition fields (summit date, reached altitude, actual deaths) "
                    "are excluded. Oxygen and hired staff are recorded during the expedition "
                    "and treated as plan attributes. Expeditions abandoned because of the 2014 "
                    "strike/avalanche or the 2015 earthquake (per termnote) are excluded.",
            "closureEffect": closure_effect,
            "closure": {
                "rule": "year in 2014-2015, no summit, termnote mentions earthquake, strike or avalanche",
                "expeditions": int(clean["exped"].query("peakid == 'EVER'")["closure"].sum()),
                "members": int(member_dataset(clean, include_closure=True)["closure"].sum()),
            },
        },
        "member": m,
        "expedition": x,
    }

    OUT_JSON.write_text(json.dumps(models, ensure_ascii=False, separators=(",", ":")),
                        encoding="utf-8")
    OUT_JS.write_text("window.EVEREST_MODEL = " +
                      json.dumps(models, ensure_ascii=False, separators=(",", ":")) +
                      ";\n", encoding="utf-8")

    for name in ("member", "expedition"):
        mm = models[name]
        print(f"\n[{name}] n={mm['n']:,} lambda={mm['lambda']} "
              f"base={mm['baseRate']:.3f}")
        for split in ("train", "validation", "test"):
            row = mm["metrics"]
            print(f"  {split:10s} model brier={row['model'][split]['brier']:.4f} "
                  f"ll={row['model'][split]['logloss']:.4f} "
                  f"auc={row['model'][split]['auc']} | "
                  f"const ll={row['constant'][split]['logloss']:.4f} | "
                  f"sideSeason ll={row['sideSeason'][split]['logloss']:.4f}")
    print(f"\nwrote {OUT_JSON.name} ({OUT_JSON.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    run()
