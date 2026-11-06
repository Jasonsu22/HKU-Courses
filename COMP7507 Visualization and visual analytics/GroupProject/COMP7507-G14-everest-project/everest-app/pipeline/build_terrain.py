#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建离线地形底图（2D hillshade + 3D 贴图 + DEM）。

数据来源
--------
DEM      : Mapzen / AWS Open Data "Terrain Tiles" (terrarium PNG, SRTM 派生)
            https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png
营地/山峰 : OpenStreetMap，Overpass API 导出（见 pipeline/osm_features.json），ODbL

输出到 everest-app/data/terrain/
    dem.png               terrarium 编码高程（浏览器端解码）
    terrain-shade.png     2D 用：hillshade + 高程配色
    terrain-color.png     3D 用：高程配色（无烘焙阴影，交给光照）
    terrain.json          bbox / 尺寸 / 高程范围 / 署名
"""

from __future__ import annotations

import base64
import json
import math
from pathlib import Path

import urllib.request

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "terrain"
CACHE = HERE / ".terrain_cache"
OUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(exist_ok=True)

# 覆盖 summit / 南北 BC / 两侧 C1–C4 / Lhotse / Pumori
BBOX = {"west": 86.785, "east": 86.985, "south": 27.955, "north": 28.155}
Z = 13
TILE = 256
UA = {"User-Agent": "COMP7507-student-project/1.0 (offline course project)"}

SHADE_SIZE = 1000      # 2D 底图长边
DEM_SIZE = 1100        # DEM 长边（3D 采样用）


def lonlat_to_px(lon, lat, z=Z):
    n = (2 ** z) * TILE
    x = (lon + 180.0) / 360.0 * n
    y = (1.0 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2.0 * n
    return x, y


def fetch_tile(x, y):
    path = CACHE / f"{Z}_{x}_{y}.png"
    if path.exists():
        return Image.open(path).convert("RGB")
    url = f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{x}/{y}.png"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    path.write_bytes(data)
    return Image.open(path).convert("RGB")


def build_mosaic():
    x0f, y0f = lonlat_to_px(BBOX["west"], BBOX["north"])
    x1f, y1f = lonlat_to_px(BBOX["east"], BBOX["south"])
    tx0, ty0 = int(x0f // TILE), int(y0f // TILE)
    tx1, ty1 = int(x1f // TILE), int(y1f // TILE)
    cols, rows = tx1 - tx0 + 1, ty1 - ty0 + 1
    print(f"tiles {cols}×{rows} = {cols*rows} at z{Z} (x {tx0}..{tx1}, y {ty0}..{ty1})")
    mosaic = Image.new("RGB", (cols * TILE, rows * TILE))
    for i, x in enumerate(range(tx0, tx1 + 1)):
        for j, y in enumerate(range(ty0, ty1 + 1)):
            mosaic.paste(fetch_tile(x, y), (i * TILE, j * TILE))
    left = int(round(x0f - tx0 * TILE))
    top = int(round(y0f - ty0 * TILE))
    right = int(round(x1f - tx0 * TILE))
    bottom = int(round(y1f - ty0 * TILE))
    crop = mosaic.crop((left, top, right, bottom))
    print(f"crop {crop.width}×{crop.height}")
    return crop


def decode_elev(img: Image.Image) -> np.ndarray:
    a = np.asarray(img).astype(np.float32)
    return a[..., 0] * 256.0 + a[..., 1] + a[..., 2] / 256.0 - 32768.0


def encode_elev(elev: np.ndarray) -> Image.Image:
    v = np.clip(elev + 32768.0, 0, 65535)
    r = np.floor(v / 256.0)
    g = np.floor(v - r * 256.0)
    b = np.floor((v - r * 256.0 - g) * 256.0)
    rgb = np.stack([r, g, b], axis=-1)
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8), "RGB")


def hillshade(elev: np.ndarray, cellsize_m: float, azimuth=315.0, altitude=38.0,
              z_factor=1.3):
    dy, dx = np.gradient(elev * z_factor, cellsize_m, cellsize_m)
    slope = np.arctan(np.hypot(dx, dy))
    aspect = np.arctan2(-dx, dy)
    az = math.radians(360.0 - azimuth)
    alt = math.radians(altitude)
    shade = (np.sin(alt) * np.cos(slope) +
             np.cos(alt) * np.sin(slope) * np.cos(az - aspect))
    return np.clip(shade, 0, 1)


RAMP = [
    (3000, (84, 98, 74)),
    (4400, (120, 132, 96)),
    (5000, (150, 152, 112)),
    (5600, (166, 160, 124)),
    (6200, (172, 163, 134)),
    (6700, (160, 149, 132)),
    (7100, (182, 173, 162)),
    (7500, (214, 209, 201)),
    (7900, (240, 238, 234)),
    (8300, (252, 251, 250)),
    (8900, (255, 255, 255)),
]


def colorize(elev: np.ndarray) -> np.ndarray:
    stops = np.array([s[0] for s in RAMP], dtype=np.float32)
    cols = np.array([s[1] for s in RAMP], dtype=np.float32)
    out = np.zeros(elev.shape + (3,), dtype=np.float32)
    for c in range(3):
        out[..., c] = np.interp(elev, stops, cols[:, c])
    return out


def snow_boost(elev: np.ndarray, rgb: np.ndarray) -> np.ndarray:
    # 高处提亮、低处压暗，增强立体感
    t = np.clip((elev - 6000) / 2000, 0, 1)[..., None]
    return rgb * (0.88 + 0.22 * t)


def erode(mask: np.ndarray, k: int = 1) -> np.ndarray:
    out = mask.copy()
    for dy in range(-k, k + 1):
        for dx in range(-k, k + 1):
            out &= np.roll(np.roll(mask, dy, 0), dx, 1)
    return out


def contour_lines(elev: np.ndarray, levels, alpha=0.18) -> np.ndarray:
    """500 m 等高线近似：每层的边界像素（形态学边缘，1 px）。"""
    lines = np.zeros(elev.shape, dtype=bool)
    for lv in levels:
        m = elev >= lv
        lines |= (m & ~erode(m, 1))
    return lines


def main():
    mosaic = build_mosaic()
    elev = decode_elev(mosaic)
    print(f"elevation {elev.min():.0f}..{elev.max():.0f} m, mean {elev.mean():.0f}")

    # --- 3D 网格（直接给顶点高程，避免 file:// 下的 canvas taint） ----------
    NX, NY = 260, 300
    h, w = elev.shape
    ys = np.linspace(0, h - 1, NY)
    xs = np.linspace(0, w - 1, NX)
    grid = np.empty((NY, NX), dtype=np.int16)
    for j, yy in enumerate(ys):
        row = int(round(yy))
        for i, xx in enumerate(xs):
            grid[j, i] = int(round(elev[row, int(round(xx))]))
    mesh_b64 = base64.b64encode(grid.astype("<i2").tobytes()).decode("ascii")
    width_km = (BBOX["east"] - BBOX["west"]) * 111.32 * math.cos(math.radians(28.05))
    height_km = (BBOX["north"] - BBOX["south"]) * 110.57

    # --- 2D hillshade + 配色 ----------------------------------------------
    width_m = (BBOX["east"] - BBOX["west"]) * 111320 * math.cos(math.radians(28.05))
    cell = width_m / mosaic.width
    shade = hillshade(elev, cell)
    rgb = colorize(elev)
    lit = rgb * (0.58 + 0.62 * shade[..., None])
    lit = np.clip(snow_boost(elev, lit), 0, 255)
    lines = contour_lines(elev, range(5000, 8500, 500))
    lit[lines] = lit[lines] * 0.72 + np.array([40, 36, 30]) * 0.28
    shade_img = Image.fromarray(np.clip(lit, 0, 255).astype(np.uint8), "RGB")
    shade_img.thumbnail((SHADE_SIZE, SHADE_SIZE * 2), Image.LANCZOS)
    shade_img.save(OUT / "terrain-shade.jpg", quality=88, optimize=True)

    # --- 3D 贴图（无烘焙阴影） -------------------------------------------
    flat = snow_boost(elev, rgb)
    color_img = Image.fromarray(np.clip(flat, 0, 255).astype(np.uint8), "RGB")
    color_img.thumbnail((SHADE_SIZE, SHADE_SIZE * 2), Image.LANCZOS)
    color_img.save(OUT / "terrain-color.jpg", quality=86, optimize=True)

    meta = {
        "bbox": BBOX,
        "zoom": Z,
        "shadeSize": shade_img.size,
        "mesh": {"nx": NX, "ny": NY},
        "widthKm": round(width_km, 3),
        "heightKm": round(height_km, 3),
        "elevation": {"min": round(float(elev.min())), "max": round(float(elev.max()))},
        "cellMetres": round(cell, 1),
        "attribution": {
            "dem": "Terrain tiles: Mapzen / AWS Open Data (SRTM-derived), terrarium encoding",
            "features": "Camps and peaks: © OpenStreetMap contributors, ODbL",
        },
        "build": "pipeline/build_terrain.py",
    }
    (OUT / "terrain.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
    bundle = {"meta": meta, "elev": mesh_b64}
    (OUT / "terrain.js").write_text(
        "window.TERRAIN = " + json.dumps(bundle, separators=(",", ":")) + ";\n",
        encoding="utf-8")
    for f in ("terrain-shade.jpg", "terrain-color.jpg", "terrain.js"):
        print(f"{f:20s} { (OUT/f).stat().st_size/1024:7.0f} KB")


if __name__ == "__main__":
    main()
