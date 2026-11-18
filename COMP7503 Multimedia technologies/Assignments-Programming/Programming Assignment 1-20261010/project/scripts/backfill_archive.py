# /// script
# requires-python = ">=3.10"
# dependencies = ["pymongo>=4.6", "requests>=2.31"]
# ///
"""Backfill MongoDB with past versions of the live feeds from the data.gov.hk Historical Archive.

The archive (https://api.data.gov.hk/v1/historical-archive) stores every version of a
registered data file. We list the versions, pick one per time slot, download it from the
archive's S3 bucket and store it with the SAME document schema the Node-RED collectors use
(plus `source: "archive"`), so live and historical data can be queried together.

Usage (from the project folder, stack running):
    uv run scripts/backfill_archive.py --start 20261020 --end 20261117
    uv run scripts/backfill_archive.py --only aqhi,ae_waiting      # subset
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import requests
from pymongo import MongoClient, UpdateOne

HKT = timezone(timedelta(hours=8))
API = "https://api.data.gov.hk/v1/historical-archive/list-file-versions"
S3 = "https://s3-ap-southeast-1.amazonaws.com/historical-resource-archive"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "comp7503-smartcity-backfill/1.0"

HKO_CSV = "https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/{}.csv"


# ------------------------------------------------------------------ archive access
def list_versions(url: str, start: str, end: str) -> list[str]:
    r = SESSION.get(API, params={"url": url, "start": start, "end": end}, timeout=120)
    r.raise_for_status()
    return r.json().get("timestamps", [])


def s3_url(url: str, ts: str) -> str:
    day, hhmm = ts.split("-")
    enc = urllib.parse.quote(urllib.parse.quote(url, safe=""), safe="")
    return f"{S3}/{day[:4]}/{day[4:6]}/{day[6:]}/{enc}/{hhmm}"


def fetch(url: str, ts: str) -> str | None:
    for _ in range(3):
        try:
            r = SESSION.get(s3_url(url, ts), timeout=60)
            if r.status_code == 200:
                r.encoding = "utf-8"
                return r.text
        except requests.RequestException:
            pass
    return None


def ts_to_dt(ts: str) -> datetime:
    return datetime.strptime(ts, "%Y%m%d-%H%M").replace(tzinfo=HKT)


def pick_per_slot(stamps: list[str], minutes: int) -> list[str]:
    """Keep the first version in every `minutes`-long slot."""
    seen, out = set(), []
    for ts in stamps:
        dt = ts_to_dt(ts)
        slot = (dt - datetime(2000, 1, 1, tzinfo=HKT)) // timedelta(minutes=minutes)
        if slot not in seen:
            seen.add(slot)
            out.append(ts)
    return out


# ------------------------------------------------------------------ parsers (mirror the Node-RED functions)
def tag(s: str, t: str) -> str | None:
    m = re.search(rf"<{t}>([\s\S]*?)</{t}>", s)
    return m.group(1).strip() if m else None


def parse_aqhi(text: str, now: datetime):
    for it in re.findall(r"<item>([\s\S]*?)</item>", text):
        station, dt, raw = tag(it, "StationName"), tag(it, "DateTime"), tag(it, "aqhi")
        if not station or not dt or not raw:
            continue
        try:
            time = parsedate_to_datetime(dt)
            aqhi = 11 if "+" in raw else float(raw)
        except (TypeError, ValueError):
            continue
        yield UpdateOne({"station": station, "time": time},
                        {"$set": {"station": station, "time": time, "aqhi": aqhi, "aqhiRaw": raw,
                                  "stationType": tag(it, "type")},
                         "$setOnInsert": {"fetchedAt": now, "source": "archive"}}, upsert=True)


def to_min(s):
    m = re.search(r"([\d.]+)\s*(minute|hour)", str(s or ""), re.I)
    if not m:
        return None
    return round(float(m.group(1)) * (60 if m.group(2).lower().startswith("hour") else 1))


def parse_ae(text: str, now: datetime):
    import json
    d = json.loads(text)
    m = re.match(r"(\d+)/(\d+)/(\d+)\s+(\d+):(\d+)\s*([AP]M)", d.get("updateTime", ""), re.I)
    if not m:
        return
    hh = int(m.group(4)) % 12 + (12 if m.group(6).upper() == "PM" else 0)
    upd = datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)), hh, int(m.group(5)), tzinfo=HKT)
    for h in d.get("waitTime", []):
        yield UpdateOne({"hospital": h["hospName"], "updateTime": upd},
                        {"$set": {"hospital": h["hospName"], "updateTime": upd,
                                  "t1WaitMin": to_min(h.get("t1wt")), "t2WaitMin": to_min(h.get("t2wt")),
                                  "t3P50Min": to_min(h.get("t3p50")), "t3P95Min": to_min(h.get("t3p95")),
                                  "t45P50Min": to_min(h.get("t45p50")), "t45P95Min": to_min(h.get("t45p95")),
                                  "managingT1": h.get("manageT1case") == "Y",
                                  "managingT2": h.get("manageT2case") == "Y", "raw": h},
                         "$setOnInsert": {"fetchedAt": now, "source": "archive"}}, upsert=True)


def parse_jt(text: str, now: datetime):
    for it in re.findall(r"<jtis_journey_time>([\s\S]*?)</jtis_journey_time>", text):
        frm, to, cap = tag(it, "LOCATION_ID"), tag(it, "DESTINATION_ID"), tag(it, "CAPTURE_DATE")
        if not (frm and to and cap):
            continue
        ct = datetime.fromisoformat(cap).replace(tzinfo=HKT)
        try:
            val = float(tag(it, "JOURNEY_DATA"))
        except (TypeError, ValueError):
            val = None
        yield UpdateOne({"from": frm, "to": to, "captureTime": ct},
                        {"$set": {"from": frm, "to": to, "captureTime": ct,
                                  "journeyType": int(tag(it, "JOURNEY_TYPE") or 0), "value": val,
                                  "colour": int(tag(it, "COLOUR_ID") or 0)},
                         "$setOnInsert": {"fetchedAt": now, "source": "archive"}}, upsert=True)


def parse_speed(text: str, now: datetime):
    if "</segment_speed_list>" not in text[-200:]:
        raise ValueError("truncated file")  # the archive's S3 sometimes cuts slow downloads short
    d, t = tag(text, "date"), tag(text, "time")
    if not d or not t:
        return
    snap = datetime.fromisoformat(f"{d}T{t}").replace(tzinfo=HKT)
    speeds = {sid: float(v) for sid, v, ok in
              re.findall(r"<segment_id>(\d+)</segment_id><speed>([\d.]+)</speed><valid>([YN])</valid>", text)
              if ok == "Y"}
    vals = sorted(speeds.values())
    if not vals:
        return
    n = len(vals)
    doc = {"snapshotTime": snap, "validSegments": n,
           "meanSpeed": round(sum(vals) / n, 1), "medianSpeed": vals[n // 2],
           "pctBelow30": round(sum(v < 30 for v in vals) / n * 100, 1),
           "pctBelow15": round(sum(v < 15 for v in vals) / n * 100, 1),
           "speeds": speeds}
    yield UpdateOne({"snapshotTime": snap}, {"$set": doc,
                    "$setOnInsert": {"fetchedAt": now, "source": "archive"}}, upsert=True)


def hko_csv_parser(kind: str):
    """HKO regional CSVs -> hko_regional {station, time, <fields>} (fields merged across CSVs)."""
    def parse(text: str, now: datetime):
        rows = list(csv.reader(io.StringIO(text.lstrip("﻿"))))
        for r in rows[1:]:
            if len(r) < 3 or not r[0].strip().isdigit():
                continue
            time = datetime.strptime(r[0].strip(), "%Y%m%d%H%M").replace(tzinfo=HKT)
            station = r[1].strip()

            def num(x):
                try:
                    return float(x)
                except ValueError:
                    return None
            if kind == "temperature":
                fields = {"temperature": num(r[2])}
            elif kind == "humidity":
                fields = {"humidity": num(r[2])}
            else:
                fields = {"windDir": r[2].strip() or None, "windSpeed": num(r[3]) if len(r) > 3 else None,
                          "gust": num(r[4]) if len(r) > 4 else None}
            fields = {k: v for k, v in fields.items() if v is not None}
            if not fields:
                continue
            yield UpdateOne({"station": station, "time": time},
                            {"$set": {"station": station, "time": time, **fields},
                             "$setOnInsert": {"fetchedAt": now, "source": "archive"}}, upsert=True)
    return parse


# name -> (archived url, collection, slot minutes, parser)
SOURCES = {
    "aqhi": ("https://www.aqhi.gov.hk/epd/ddata/html/out/24aqhi_Eng.xml", "aqhi", 12 * 60, parse_aqhi),
    "ae_waiting": ("https://www.ha.org.hk/opendata/aed/aedwtdata2-en.json", "ae_waiting", 15, parse_ae),
    "journey_time": ("https://resource.data.one.gov.hk/td/jss/Journeytimev2.xml", "journey_time", 10, parse_jt),
    "traffic_speed": ("https://resource.data.one.gov.hk/td/traffic-detectors/irnAvgSpeed-all.xml",
                      "traffic_speed", 60, parse_speed),   # hourly: archive S3 serves ~5 KB/s per file
    "hko_temperature": (HKO_CSV.format("latest_1min_temperature"), "hko_regional", 10,
                        hko_csv_parser("temperature")),
    "hko_humidity": (HKO_CSV.format("latest_1min_humidity"), "hko_regional", 10, hko_csv_parser("humidity")),
    "hko_wind": (HKO_CSV.format("latest_10min_wind"), "hko_regional", 10, hko_csv_parser("wind")),
}


def run_source(db, name: str, start: str, end: str, workers: int):
    url, coll, slot, parser = SOURCES[name]
    stamps = pick_per_slot(list_versions(url, start, end), slot)
    print(f"[{name}] {len(stamps)} versions to fetch -> {coll}", flush=True)
    now = datetime.now(timezone.utc)
    done = failed = written = 0
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fetch, url, ts): ts for ts in stamps}
        batch = []
        for fut in as_completed(futs):
            text = fut.result()
            done += 1
            if text is None:
                failed += 1
            else:
                try:
                    batch.extend(parser(text, now))
                except Exception as e:  # malformed version: skip it, keep going
                    failed += 1
                    print(f"  parse error {futs[fut]}: {e}", file=sys.stderr)
            if len(batch) >= 2000 or (batch and (done == len(stamps) or done % 25 == 0)):
                res = db[coll].bulk_write(batch, ordered=False)
                written += res.upserted_count + res.modified_count
                batch = []
            if done % 50 == 0:
                print(f"  {done}/{len(stamps)}", flush=True)
    print(f"[{name}] done: {done - failed} files ok, {failed} failed, {written} docs written", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="20261020")
    ap.add_argument("--end", default=(datetime.now(HKT) - timedelta(days=1)).strftime("%Y%m%d"))
    ap.add_argument("--only", default=",".join(SOURCES))
    ap.add_argument("--mongo", default="mongodb://localhost:27017")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    db = MongoClient(a.mongo, tz_aware=True)["smartcity"]
    db["hko_regional"].create_index([("station", 1), ("time", 1)], unique=True)
    db["hko_regional"].create_index([("time", 1)])
    for name in a.only.split(","):
        run_source(db, name.strip(), a.start, a.end, a.workers)


if __name__ == "__main__":
    main()
