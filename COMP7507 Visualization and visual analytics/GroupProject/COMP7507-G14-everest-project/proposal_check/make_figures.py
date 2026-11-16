#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用 Proposal 同一份 CSV 画出 4 张核验图（Pillow，无第三方图表库）。

    python3 make_figures.py

输出到 ./figs/
    fig1_everest_yearly.png        珠峰 expedition / 参与记录 逐年规模
    fig2_side_season_success.png  南/北侧 × 季节的 expedition 成功率 + 95% Wilson 区间
    fig3_myear_mismatch.png        成员表 myear 与 expedition 年份不一致的比例（按年代）
    fig4_hired_gap.png             雇佣人员：expedition 字段 vs 成员表实际收录
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import verify_proposal_claims as vp

HERE = Path(__file__).resolve().parent
FIGS = HERE / "figs"
FIGS.mkdir(exist_ok=True)

FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
INK = (32, 38, 46)
MUTED = (110, 118, 128)
GRID = (226, 230, 235)
BLUE = (44, 110, 143)
ORANGE = (208, 126, 61)
RED = (176, 58, 72)
TEAL = (38, 140, 128)
BG = (255, 255, 255)


def F(size: int):
    return ImageFont.truetype(FONT_PATH, size)


def ctext(d, x, y, s, font, fill):
    tw = d.textlength(s, font=font)
    d.text((x - tw / 2, y), s, font=font, fill=fill)


def nice_ticks(vmax: float, n: int = 5):
    if vmax <= 0:
        return 1, [0, 1]
    raw = vmax / n
    mag = 10 ** math.floor(math.log10(raw))
    step = mag * 10
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            step = m * mag
            break
    top = math.ceil(vmax / step) * step
    count = int(round(top / step))
    return top, [step * i for i in range(count + 1)]


def wilson(k: int, n: int, z: float = 1.96):
    if n == 0:
        return 0.0, 0.0
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


class Axes:
    """极简坐标轴：像素映射 + 网格 + 刻度。"""

    def __init__(self, draw: ImageDraw.ImageDraw, box, ylim=(0, 1)):
        self.d = draw
        self.l, self.t, self.r, self.b = box
        self.ymin, self.ymax = ylim

    def X(self, x, xlim):
        x0, x1 = xlim
        return self.l + (x - x0) / (x1 - x0) * (self.r - self.l)

    def Y(self, y):
        return self.b - (y - self.ymin) / (self.ymax - self.ymin) * (self.b - self.t)

    def grid(self, yticks, yfmt="{:.0f}", ylabel="", tick_size=17, label_size=18):
        for y in yticks:
            py = self.Y(y)
            self.d.line([(self.l, py), (self.r, py)], fill=GRID, width=1)
            txt = yfmt.format(y)
            tw = self.d.textlength(txt, font=F(tick_size))
            self.d.text((self.l - 10 - tw, py - tick_size / 2 - 1), txt,
                        font=F(tick_size), fill=MUTED)
        self.d.line([(self.l, self.t), (self.l, self.b)], fill=MUTED, width=2)
        self.d.line([(self.l, self.b), (self.r, self.b)], fill=MUTED, width=2)
        if ylabel:
            self.d.text((self.l, self.t - 46), ylabel, font=F(label_size), fill=MUTED)


def header(d: ImageDraw.ImageDraw, w: int, title: str, subtitle: str):
    d.text((64, 46), title, font=F(33), fill=INK)
    d.text((66, 92), subtitle, font=F(19), fill=MUTED)


def legend(d: ImageDraw.ImageDraw, items, x: int, y: int, size=17):
    for label, color in items:
        d.rectangle([x, y + 4, x + 18, y + 18], fill=color)
        d.text((x + 26, y), label, font=F(size), fill=INK)
        x += 42 + int(d.textlength(label, font=F(size)))


# ---------------------------------------------------------------------------
# 图 1：逐年规模
# ---------------------------------------------------------------------------
def fig1(n: dict, e):
    w, h = 1560, 1000
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img, "RGBA")
    header(d, w, "珠峰 expedition 与参与记录，1921–2024",
           "同一份 exped.csv / members.csv；底色为 Proposal 的训练/验证/测试窗口；2020 年只有 3 次 expedition")
    legend(d, [("train 1990–2014", (44, 110, 143, 90)),
               ("valid 2015–2019", (208, 126, 61, 110)),
               ("test 2020–2024", (176, 58, 72, 110))], 66, 128)

    years = sorted(n["structure"]["expeditions_by_year"])
    counts = [n["structure"]["expeditions_by_year"][y] for y in years]
    mrows = e.groupby("year").size().reindex(years, fill_value=0).tolist()

    xlim = (1920, 2025)
    top_box = (120, 210, w - 60, 560)
    bot_box = (120, 640, w - 60, 920)

    for lo, hi, color in [(1990, 2014, (44, 110, 143, 22)),
                          (2015, 2019, (208, 126, 61, 30)),
                          (2020, 2024, (176, 58, 72, 30))]:
        ax = Axes(d, bot_box)
        x0, x1 = ax.X(lo - 0.5, xlim), ax.X(hi + 0.5, xlim)
        d.rectangle([x0, top_box[1], x1, bot_box[3]], fill=color)

    step = (top_box[2] - top_box[0]) / (xlim[1] - xlim[0])

    ymax, yticks = nice_ticks(max(counts))
    ax = Axes(d, top_box, (0, ymax))
    ax.grid(yticks, ylabel="expeditions per year")
    for y, c in zip(years, counts):
        x = ax.X(y, xlim)
        d.rectangle([x - step * 0.42, ax.Y(c), x + step * 0.42, ax.Y(0)], fill=BLUE)
    for y in (1921, 1953, 1980, 1996, 2005, 2019, 2020, 2024):
        if y in counts:
            i = years.index(y)
            v = counts[i]
            ctext(d, ax.X(y, xlim), ax.Y(v) - 24, str(v), F(14), BLUE)

    ymax2, yticks2 = nice_ticks(max(mrows))
    ax2 = Axes(d, bot_box, (0, ymax2))
    ax2.grid(yticks2, ylabel="member (participation) rows per year")
    for y, c in zip(years, mrows):
        x = ax2.X(y, xlim)
        d.rectangle([x - step * 0.42, ax2.Y(c), x + step * 0.42, ax2.Y(0)], fill=TEAL)
    peak_year = years[mrows.index(max(mrows))]
    d.text((ax2.X(peak_year, xlim) + 8, ax2.Y(max(mrows)) + 6),
           f"peak {max(mrows):,} ({peak_year})", font=F(14), fill=TEAL)

    for y in range(1925, 2026, 25):
        x = ax2.X(y, xlim)
        d.line([(x, bot_box[3]), (x, bot_box[3] + 6)], fill=MUTED, width=1)
        ctext(d, x, bot_box[3] + 12, str(y), F(16), MUTED)
    d.text((w - 150, bot_box[3] + 46), "year", font=F(17), fill=MUTED)

    legend(d, [("expeditions", BLUE), ("member rows", TEAL)], 120, 950)
    out = FIGS / "fig1_everest_yearly.png"
    img.save(out)
    return out


# ---------------------------------------------------------------------------
# 图 2：南/北侧 × 季节成功率
# ---------------------------------------------------------------------------
def fig2(n: dict):
    w, h = 1560, 900
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img, "RGBA")
    header(d, w, "expedition 成功率：南北侧 × 季节（success1，含 95% Wilson 区间）",
           "样本量写在柱子上方；秋/冬/夏样本很小，区间很宽 —— 这正是必须同时显示 n 的原因")

    rows = {(r["side"], r["season"]): r for r in n["structure"]["side_season"]}
    seasons = ["Spring", "Autumn", "Winter", "Summer"]
    box = (110, 230, w - 70, 740)
    ax = Axes(d, box, (0, 1.0))
    ax.grid([0, .2, .4, .6, .8, 1.0], yfmt="{:.1f}",
            ylabel="share of expeditions reaching the summit on route 1")

    group_w = (box[2] - box[0]) / len(seasons)
    bar_w = 78
    colors = {"South": ORANGE, "North": TEAL}
    for i, season in enumerate(seasons):
        centre = box[0] + group_w * (i + 0.5)
        for j, side in enumerate(["South", "North"]):
            r = rows.get((side, season))
            x = centre + (j - 0.5) * (bar_w + 16)
            if not r:
                ctext(d, x, ax.Y(0) - 26, "n=0", F(14), MUTED)
                continue
            k = round(r["success1"] * r["n"])
            lo, hi = wilson(k, r["n"])
            top = ax.Y(r["success1"])
            d.rectangle([x - bar_w / 2, top, x + bar_w / 2, ax.Y(0)], fill=colors[side])
            d.line([(x, ax.Y(lo)), (x, ax.Y(hi))], fill=INK, width=2)
            for yy in (lo, hi):
                d.line([(x - 9, ax.Y(yy)), (x + 9, ax.Y(yy))], fill=INK, width=2)
            label_y = max(box[1] + 4, ax.Y(hi) - 44)
            ctext(d, x, label_y, f"{r['success1']:.0%}", F(18), INK)
            ctext(d, x, label_y + 22, f"n={r['n']:,}", F(14), MUTED)
        ctext(d, centre, box[3] + 30, season, F(22), INK)

    legend(d, [("South side (Nepal)", ORANGE), ("North side (China)", TEAL)], 110, 812)
    d.text((w - 440, 816), "bars: observed rate   whiskers: 95% Wilson CI",
           font=F(15), fill=MUTED)
    out = FIGS / "fig2_side_season_success.png"
    img.save(out)
    return out


# ---------------------------------------------------------------------------
# 图 3：myear 不可用
# ---------------------------------------------------------------------------
def fig3(clean):
    members = clean["members"].copy()
    members["decade"] = (members["year"] // 10 * 10).astype("Int64")
    ever = members["peakid"] == "EVER"
    allg = members.groupby("decade").apply(
        lambda g: (g["myear"] != g["year"]).mean(), include_groups=False)
    evg = members[ever].groupby("decade").apply(
        lambda g: (g["myear"] != g["year"]).mean(), include_groups=False)
    decades = [int(x) for x in allg.index if 1920 <= int(x) <= 2020]

    w, h = 1560, 860
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img, "RGBA")
    header(d, w, "成员表 myear 与所属 expedition 年份：不一致比例",
           "2000 年前几乎全错、2010 年后基本全对；而 mseason 与 expedition 季节 89,000/89,000 一致")

    box = (110, 240, w - 70, 700)
    ax = Axes(d, box, (0, 1.0))
    ax.grid([0, .2, .4, .6, .8, 1.0], yfmt="{:.1f}",
            ylabel="share of member rows where myear ≠ expedition year")

    group_w = (box[2] - box[0]) / len(decades)
    bar_w = 46
    for i, dec in enumerate(decades):
        centre = box[0] + group_w * (i + 0.5)
        for j, (series, color) in enumerate([(allg, BLUE), (evg, RED)]):
            val = series.get(dec, float("nan"))
            if val != val:
                continue
            x = centre + (j - 0.5) * (bar_w + 6)
            d.rectangle([x - bar_w / 2, ax.Y(val), x + bar_w / 2, ax.Y(0)], fill=color)
            if val > 0.55:
                ctext(d, x, ax.Y(val) + 10, f"{val:.0%}", F(14), (255, 255, 255))
            else:
                ctext(d, x, ax.Y(val) - 24, f"{val:.0%}", F(14), color)
        ctext(d, centre, box[3] + 16, f"{dec}s", F(18), MUTED)

    # 2000 年分界
    bx = box[0] + group_w * 8
    for yy in range(box[1], box[3], 12):
        d.line([(bx, yy), (bx, yy + 6)], fill=RED, width=2)
    d.text((bx + 14, box[1] + 6), "2000: myear 开始可用（2000 年前 96% 错）",
           font=F(16), fill=RED)

    legend(d, [("all peaks", BLUE), ("Everest only", RED)], 110, 756)
    d.text((w - 590, 760),
           "overall 34.8% of 89,000 rows  |  Everest 27.5% of 25,274 rows",
           font=F(15), fill=MUTED)
    out = FIGS / "fig3_myear_mismatch.png"
    img.save(out)
    return out


# ---------------------------------------------------------------------------
# 图 4：雇佣人员被漏记
# ---------------------------------------------------------------------------
def fig4(clean):
    e = clean["exped"].query("peakid == 'EVER'").copy()
    m = clean["members"].query("peakid == 'EVER'").copy()
    listed = m[m["hired"]].groupby((m["year"] // 10 * 10)).size()
    field = e.groupby((e["year"] // 10 * 10))["tothired"].sum()
    decades = [int(x) for x in field.index if int(x) >= 1950]

    w, h = 1560, 860
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img, "RGBA")
    header(d, w, "雇佣人员：expedition.tothired vs 成员表实际收录",
           "成员表只列出约一半雇佣人员（珠峰 8,323 / 15,533 = 53.6%），所以 hired 的分母只能用 tothired")

    vmax = max(field.max(), listed.max())
    ymax, yticks = nice_ticks(vmax)
    box = (110, 230, w - 70, 700)
    ax = Axes(d, box, (0, ymax))
    ax.grid(yticks, ylabel="number of hired personnel (Everest, by decade)")
    group_w = (box[2] - box[0]) / len(decades)
    bar_w = 60
    for i, dec in enumerate(decades):
        centre = box[0] + group_w * (i + 0.5)
        for j, (series, color) in enumerate([(field, ORANGE), (listed, TEAL)]):
            val = series.get(dec, 0)
            x = centre + (j - 0.5) * (bar_w + 8)
            d.rectangle([x - bar_w / 2, ax.Y(val), x + bar_w / 2, ax.Y(0)], fill=color)
            ctext(d, x, ax.Y(val) - 24, f"{int(val):,}", F(14), color)
        ctext(d, centre, box[3] + 16, f"{dec}s", F(18), MUTED)

    legend(d, [("tothired (expedition field)", ORANGE), ("hired rows in members.csv", TEAL)], 110, 756)
    d.text((w - 470, 760), "coverage 54% of the recorded hired personnel", font=F(15), fill=MUTED)
    out = FIGS / "fig4_hired_gap.png"
    img.save(out)
    return out


def main() -> None:
    tables = vp.load_all()
    clean = vp.prepare(tables)
    n = vp.compute(clean)
    e = clean["members"].query("peakid == 'EVER'")
    outs = [fig1(n, e), fig2(n), fig3(clean), fig4(clean)]
    for p in outs:
        print("wrote", p)


if __name__ == "__main__":
    main()
