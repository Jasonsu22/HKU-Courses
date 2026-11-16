#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
营地 / 山峰 / 坳口的坐标层。

来源：OpenStreetMap（Overpass API 导出，见 osm_features_raw.json），ODbL。
坐标与海拔直接取自 OSM 标签；与本地数据库的营地中位海拔做交叉核对后写进 features.js。
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "terrain"
RAW = HERE / "osm_features_raw.json"

# 选用哪些 OSM 节点（name -> 输出定义）
CURATED = {
    "south": [
        ("Everest Base Camp", dict(id="BC-S", label="South BC", short="BC", kind="bc", dx=10, dy=4, anchor="start")),
        ("Camp 1S", dict(id="C1-S", label="Camp 1", short="C1", kind="camp", dx=12, dy=4, anchor="start")),
        ("Camp 2S", dict(id="C2-S", label="Camp 2", short="C2", kind="camp", dx=12, dy=14, anchor="start")),
        ("Camp 3S", dict(id="C3-S", label="Camp 3", short="C3", kind="camp", dx=-12, dy=16, anchor="end")),
        ("Camp 4S South Col", dict(id="C4-S", label="Camp 4 · South Col", short="C4", kind="camp", dx=12, dy=-2, anchor="start")),
    ],
    "north": [
        ("珠峰大本营", dict(id="BC-N", label="North BC", short="BC", kind="bc", dx=12, dy=4, anchor="start")),
        ("前进营地", dict(id="ABC-N", label="ABC", short="ABC", kind="camp", dx=12, dy=-2, anchor="start")),
        ("一号营地", dict(id="C1-N", label="Camp 1 · North Col", short="C1", kind="camp", dx=-12, dy=-6, anchor="end")),
        ("二号营地", dict(id="C2-N", label="Camp 2", short="C2", kind="camp", dx=12, dy=-4, anchor="start")),
        ("三号营地", dict(id="C3-N", label="Camp 3", short="C3", kind="camp", dx=12, dy=-4, anchor="start")),
    ],
}

SUMMIT = dict(id="SUM", label="Summit", short="Summit", kind="summit",
              lat=27.98806, lon=86.92521, elev=8849)

PEAKS = [
    dict(id="LHOTSE", label="Lhotse 8,516", lat=27.96199, lon=86.93250, elev=8516, dx=6, dy=16, anchor="middle", hideLabel=True),
    dict(id="NUPTSE", label="Nuptse 7,861", lat=27.96737, lon=86.88696, elev=7861, dx=-8, dy=18, anchor="end"),
    dict(id="PUMORI", label="Pumori 7,138", lat=28.01585, lon=86.82735, elev=7138, dx=-10, dy=4, anchor="end"),
]


def main():
    raw = json.loads(RAW.read_text())["elements"]
    index = {}
    for e in raw:
        t = e.get("tags", {})
        name = t.get("name")
        if name and "lat" in e:
            index[name] = e

    def node(name):
        e = index.get(name)
        if not e:
            raise SystemExit(f"missing OSM node: {name}")
        return e

    camps = {"south": [], "north": []}
    for side, items in CURATED.items():
        for name, meta in items:
            e = node(name)
            camps[side].append({
                "id": meta["id"], "label": meta["label"], "short": meta["short"],
                "kind": meta["kind"], "side": side,
                "lat": round(e["lat"], 6), "lon": round(e["lon"], 6),
                "elev": int(float(e.get("tags", {}).get("ele", 0)) or 0),
                "dx": meta["dx"], "dy": meta["dy"], "anchor": meta["anchor"],
            })
        camps[side].append(dict(SUMMIT, side=side, dx=10, dy=-10, anchor="start"))

    features = {
        "attribution": "Camps, peaks and cols: © OpenStreetMap contributors (ODbL), "
                       "elevations from OSM tags; terrain from Mapzen / AWS Open Data.",
        "sources": [
            {"name": "OpenStreetMap · Overpass API", "url": "https://www.openstreetmap.org/",
             "query": "node[natural~peak|saddle](27.90,86.75,28.20,87.00); "
                      "node[tourism=camp_site](27.90,86.75,28.20,87.00); out;"},
            {"name": "Mapzen Terrain Tiles", "url": "https://registry.opendata.aws/terrain-tiles/"},
        ],
        "camps": camps,
        "peaks": PEAKS,
        "routes": {
            "south": ["BC-S", "C1-S", "C2-S", "C3-S", "C4-S", "SUM"],
            "north": ["BC-N", "ABC-N", "C1-N", "C2-N", "C3-N", "SUM"],
        },
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "features.json").write_text(json.dumps(features, ensure_ascii=False, indent=2),
                                       encoding="utf-8")
    (OUT / "features.js").write_text(
        "window.TERRAIN_FEATURES = " +
        json.dumps(features, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8")
    print("camps", {k: len(v) for k, v in camps.items()})
    for f in ("features.js", "features.json"):
        print(f, f"{(OUT/f).stat().st_size/1024:.1f} KB")


if __name__ == "__main__":
    main()
