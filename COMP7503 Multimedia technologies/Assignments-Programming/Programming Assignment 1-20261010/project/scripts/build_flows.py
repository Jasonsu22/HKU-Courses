#!/usr/bin/env python3
"""Build nodered/data/flows.json: the course's HKO sample tab + our "Data Collection" tab.

Run from the project folder:  python3 scripts/build_flows.py
Then restart Node-RED:         docker restart comp7503-nodered

NOTE: once flows are edited in the Node-RED editor, export from the editor instead of
re-running this script (it overwrites flows.json).
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SAMPLE = ROOT.parent / "HKO.Flow.json"
OUT = ROOT / "nodered" / "data" / "flows.json"

DB_CFG = "ecc26120.5c01a8"  # mongodb3 config node id from the sample flow (re-used)
TAB = "dc0llect0r0tab01"

_counter = [0]


def nid(prefix):
    _counter[0] += 1
    return f"{prefix}{_counter[0]:04d}dc"


# ---------------------------------------------------------------- shared JS
STORE_RESULT = r"""
// Show how many documents were inserted/updated by the bulkWrite
const r = msg.payload || {};
const ins = r.nUpserted ?? r.upsertedCount ?? 0;
const mod = r.nModified ?? r.modifiedCount ?? 0;
const t = new Date().toLocaleTimeString('en-GB', {timeZone: 'Asia/Hong_Kong'});
node.status({fill: 'green', shape: 'dot', text: `${t}  +${ins} new, ${mod} updated`});
return null;
"""

HTTP_GUARD = r"""
if (msg.statusCode !== 200 || !msg.payload) {
    node.status({fill: 'red', shape: 'ring', text: 'HTTP ' + msg.statusCode});
    return null;
}
"""

# ---------------------------------------------------------------- parsers
PARSE_AQHI = HTTP_GUARD + r"""
// EPD past-24h AQHI XML -> one document per (station, hour), upserted
const xml = String(msg.payload);
const tag = (s, t) => { const m = s.match(new RegExp('<' + t + '>([\\s\\S]*?)</' + t + '>')); return m ? m[1].trim() : null; };
const ops = [];
for (const m of xml.matchAll(/<item>([\s\S]*?)<\/item>/g)) {
    const it = m[1];
    const station = tag(it, 'StationName');
    const time = new Date(tag(it, 'DateTime'));
    const raw = tag(it, 'aqhi');
    if (!station || isNaN(time) || raw === null || raw === '') continue;
    const aqhi = raw.includes('+') ? 11 : Number(raw);       // "10+" stored as 11
    if (isNaN(aqhi)) continue;
    ops.push({updateOne: {
        filter: {station, time},
        update: {$set: {station, time, aqhi, aqhiRaw: raw,
                        stationType: tag(it, 'type'), fetchedAt: new Date()}},
        upsert: true}});
}
if (!ops.length) { node.status({fill: 'yellow', shape: 'ring', text: 'no items'}); return null; }
node.status({fill: 'blue', shape: 'dot', text: ops.length + ' readings'});
msg.payload = [ops, {ordered: false}];
return msg;
"""

PARSE_AE = HTTP_GUARD + r"""
// Hospital Authority A&E waiting time (v2) -> one document per (hospital, updateTime)
const d = msg.payload;
// "18/11/2026 8:15PM" (HK local time) -> Date
const m = String(d.updateTime || '').match(/(\d+)\/(\d+)\/(\d+)\s+(\d+):(\d+)\s*([AP]M)/i);
if (!m) { node.status({fill: 'red', shape: 'ring', text: 'bad updateTime'}); return null; }
let hh = Number(m[4]) % 12; if (m[6].toUpperCase() === 'PM') hh += 12;
const pad = n => String(n).padStart(2, '0');
const updateTime = new Date(`${m[3]}-${pad(m[2])}-${pad(m[1])}T${pad(hh)}:${pad(m[5])}:00+08:00`);

// "0 minute" | "less than 15 minutes" | "20 minutes" | "1.5 hours" | "3 hour" -> minutes
function toMin(s) {
    if (!s) return null;
    const x = String(s).match(/([\d.]+)\s*(minute|hour)/i);
    if (!x) return null;
    return Math.round(Number(x[1]) * (/hour/i.test(x[2]) ? 60 : 1));
}
const ops = (d.waitTime || []).map(h => ({updateOne: {
    filter: {hospital: h.hospName, updateTime},
    update: {$set: {
        hospital: h.hospName, updateTime,
        t1WaitMin: toMin(h.t1wt), t2WaitMin: toMin(h.t2wt),
        t3P50Min: toMin(h.t3p50), t3P95Min: toMin(h.t3p95),
        t45P50Min: toMin(h.t45p50), t45P95Min: toMin(h.t45p95),
        managingT1: h.manageT1case === 'Y', managingT2: h.manageT2case === 'Y',
        raw: h, fetchedAt: new Date()}},
    upsert: true}}));
if (!ops.length) return null;
node.status({fill: 'blue', shape: 'dot', text: ops.length + ' hospitals @ ' + d.updateTime});
msg.payload = [ops, {ordered: false}];
return msg;
"""

PARSE_JT = HTTP_GUARD + r"""
// Transport Dept journey time indicators (XML) -> one document per (route, captureTime)
const xml = String(msg.payload);
const tag = (s, t) => { const m = s.match(new RegExp('<' + t + '>([\\s\\S]*?)</' + t + '>')); return m ? m[1].trim() : null; };
const ops = [];
for (const m of xml.matchAll(/<jtis_journey_time>([\s\S]*?)<\/jtis_journey_time>/g)) {
    const it = m[1];
    const from = tag(it, 'LOCATION_ID'), to = tag(it, 'DESTINATION_ID');
    const cap = tag(it, 'CAPTURE_DATE');
    if (!from || !to || !cap) continue;
    const captureTime = new Date(cap + '+08:00');
    const val = Number(tag(it, 'JOURNEY_DATA'));
    ops.push({updateOne: {
        filter: {from, to, captureTime},
        update: {$set: {from, to, captureTime,
            journeyType: Number(tag(it, 'JOURNEY_TYPE')),   // 1 = journey time (min)
            value: isNaN(val) ? null : val,
            colour: Number(tag(it, 'COLOUR_ID')),            // 1 red / 2 amber / 3 green
            fetchedAt: new Date()}},
        upsert: true}});
}
if (!ops.length) return null;
node.status({fill: 'blue', shape: 'dot', text: ops.length + ' routes'});
msg.payload = [ops, {ordered: false}];
return msg;
"""

PARSE_SPEED = HTTP_GUARD + r"""
// Transport Dept average road-segment speeds (~thousands of segments) -> 1 snapshot document
const xml = String(msg.payload);
const date = (xml.match(/<date>([^<]+)<\/date>/) || [])[1];
const time = (xml.match(/<time>([^<]+)<\/time>/) || [])[1];
if (!date || !time) return null;
const snapshotTime = new Date(`${date}T${time}+08:00`);
const speeds = {};
const valid = [];
for (const m of xml.matchAll(/<segment_id>(\d+)<\/segment_id><speed>([\d.]+)<\/speed><valid>([YN])<\/valid>/g)) {
    if (m[3] !== 'Y') continue;
    const v = Number(m[2]);
    speeds[m[1]] = v;
    valid.push(v);
}
if (!valid.length) return null;
valid.sort((a, b) => a - b);
const mean = valid.reduce((a, b) => a + b, 0) / valid.length;
const doc = {
    snapshotTime,
    validSegments: valid.length,
    meanSpeed: Math.round(mean * 10) / 10,
    medianSpeed: valid[Math.floor(valid.length / 2)],
    pctBelow30: Math.round(valid.filter(v => v < 30).length / valid.length * 1000) / 10,
    pctBelow15: Math.round(valid.filter(v => v < 15).length / valid.length * 1000) / 10,
    speeds,                        // { segmentId: km/h } for hotspot analysis
    fetchedAt: new Date()
};
node.status({fill: 'blue', shape: 'dot', text: `${valid.length} segs, mean ${doc.meanSpeed} km/h`});
msg.payload = [[{updateOne: {filter: {snapshotTime}, update: {$set: doc}, upsert: true}}]];
return msg;
"""

PARSE_CP_VAC = HTTP_GUARD + r"""
// Carpark vacancy (private cars) -> 1 snapshot document every run
const res = (msg.payload && msg.payload.results) || [];
const now = new Date();
const slot = new Date(Math.floor(now.getTime() / 900000) * 900000);   // 15-min slot
const parks = [];
for (const p of res) {
    const pc = (p.privateCar || [])[0];
    if (!pc) continue;
    parks.push({id: p.park_Id, type: pc.vacancy_type, vacancy: pc.vacancy,
                vacancyEV: pc.vacancyEV ?? null, vacancyDIS: pc.vacancyDIS ?? null,
                lastupdate: pc.lastupdate ? new Date(pc.lastupdate.replace(' ', 'T') + '+08:00') : null});
}
if (!parks.length) return null;
// only real counts (type 'A'); -1 means "no data"
const counted = parks.filter(p => p.type === 'A' && p.vacancy >= 0);
const doc = {slotTime: slot, parkCount: parks.length,
             totalVacancy: counted.reduce((a, p) => a + p.vacancy, 0),
             parks, fetchedAt: now};
node.status({fill: 'blue', shape: 'dot', text: `${parks.length} parks, ${doc.totalVacancy} free`});
msg.payload = [[{updateOne: {filter: {slotTime: slot}, update: {$set: doc}, upsert: true}}]];
return msg;
"""

PARSE_CP_INFO = HTTP_GUARD + r"""
// Carpark static info (name, district, lat/long) -> one document per carpark
const res = (msg.payload && msg.payload.results) || [];
const ops = res.map(p => ({updateOne: {
    filter: {park_Id: p.park_Id},
    update: {$set: {park_Id: p.park_Id, name: p.name, district: p.district,
        region: p.address && p.address.region, nature: p.nature, carparkType: p.carpark_Type,
        latitude: p.latitude, longitude: p.longitude, openingStatus: p.opening_status,
        updatedAt: new Date()}},
    upsert: true}}));
if (!ops.length) return null;
node.status({fill: 'blue', shape: 'dot', text: ops.length + ' carparks'});
msg.payload = [ops, {ordered: false}];
return msg;
"""

PARSE_WARN = HTTP_GUARD + r"""
// HKO warning summary -> store a new document only when the active set changes
const d = msg.payload || {};
const active = Object.keys(d).map(k => ({code: d[k].code, name: d[k].name,
    actionCode: d[k].actionCode, issueTime: d[k].issueTime})).sort((a, b) => a.code < b.code ? -1 : 1);
const sig = JSON.stringify(active.map(a => a.code + ':' + a.issueTime));
if (sig === flow.get('lastWarnSig')) { node.status({fill: 'grey', shape: 'dot', text: 'no change'}); return null; }
flow.set('lastWarnSig', sig);
const t = new Date();
node.status({fill: 'blue', shape: 'dot', text: active.length ? active.map(a => a.code).join(',') : 'no warnings'});
msg.payload = [[{insertOne: {document: {observedAt: t, activeCodes: active.map(a => a.code), warnings: active}}}]];
return msg;
"""

def parse_hko_csv(kind):
    """HKO regional-weather CSV -> hko_regional {station, time, fields}; the 3 CSVs merge into one doc."""
    fields = {
        "temperature": "{temperature: num(c[2])}",
        "humidity": "{humidity: num(c[2])}",
        "wind": "{windDir: c[2] || null, windSpeed: num(c[3]), gust: num(c[4])}",
    }[kind]
    return HTTP_GUARD + r"""
// HKO regional weather CSV (""" + kind + r""") -> one document per (station, time)
const num = x => { const v = parseFloat(x); return isNaN(v) ? null : v; };
const ops = [];
for (const line of String(msg.payload).replace(/^﻿/, '').split(/\r?\n/).slice(1)) {
    const c = line.split(',').map(s => s.trim());
    if (c.length < 3 || !/^\d{12}$/.test(c[0])) continue;
    const t = c[0];
    const time = new Date(`${t.slice(0,4)}-${t.slice(4,6)}-${t.slice(6,8)}T${t.slice(8,10)}:${t.slice(10,12)}:00+08:00`);
    const f = """ + fields + r""";
    Object.keys(f).forEach(k => f[k] === null && delete f[k]);
    if (!Object.keys(f).length) continue;
    ops.push({updateOne: {filter: {station: c[1], time},
        update: {$set: Object.assign({station: c[1], time}, f), $setOnInsert: {fetchedAt: new Date(), source: 'live'}},
        upsert: true}});
}
if (!ops.length) return null;
node.status({fill: 'blue', shape: 'dot', text: ops.length + ' stations'});
msg.payload = [ops, {ordered: false}];
return msg;
"""


INDEXES = r"""
// Run once at start-up: indexes that make upserts and time-range queries fast
const idx = [
  ['aqhi',              {station: 1, time: 1}, {unique: true}],
  ['aqhi',              {time: 1}, {}],
  ['ae_waiting',        {hospital: 1, updateTime: 1}, {unique: true}],
  ['ae_waiting',        {updateTime: 1}, {}],
  ['journey_time',      {from: 1, to: 1, captureTime: 1}, {unique: true}],
  ['journey_time',      {captureTime: 1}, {}],
  ['traffic_speed',     {snapshotTime: 1}, {unique: true}],
  ['carpark_vacancy',   {slotTime: 1}, {unique: true}],
  ['carpark_info',      {park_Id: 1}, {unique: true}],
  ['weather_warnings',  {observedAt: 1}, {}],
  ['hko_regional',      {station: 1, time: 1}, {unique: true}],
  ['hko_regional',      {time: 1}, {}],
  ['Weather Report',    {updateTime: 1}, {}]
];
return [idx.map(([c, k, o]) => ({collection: c, operation: 'createIndex', payload: [k, o]}))];
"""

# ---------------------------------------------------------------- node builders
nodes = []


def add(n):
    nodes.append(n)
    return n["id"]


def comment(text, x, y, info=""):
    return add({"id": nid("cm"), "type": "comment", "z": TAB, "name": text, "info": info, "x": x, "y": y, "wires": []})


def collector(title, url, ret, repeat_s, parse_js, collection, y, info, delay=2):
    """inject -> http request -> parse -> mongodb3 bulkWrite -> status"""
    comment(title, 180, y - 40, info)
    status_id, db_id, parse_id, http_id, inj_id = (nid(p) for p in ("st", "db", "fn", "hr", "in"))
    add({"id": inj_id, "type": "inject", "z": TAB, "name": f"every {repeat_s // 60} min",
         "props": [{"p": "payload"}], "repeat": str(repeat_s), "crontab": "", "once": True,
         "onceDelay": str(delay), "topic": "", "payload": "", "payloadType": "date",
         "x": 150, "y": y, "wires": [[http_id]]})
    add({"id": http_id, "type": "http request", "z": TAB, "name": f"GET {collection}",
         "method": "GET", "ret": ret, "paytoqs": "ignore", "url": url, "tls": "", "persist": False,
         "proxy": "", "insecureHTTPParser": False, "authType": "", "senderr": False, "headers": [],
         "x": 360, "y": y, "wires": [[parse_id]]})
    add({"id": parse_id, "type": "function", "z": TAB, "name": f"Parse -> {collection}",
         "func": parse_js.strip(), "outputs": 1, "timeout": 0, "noerr": 0, "initialize": "",
         "finalize": "", "libs": [], "x": 600, "y": y, "wires": [[db_id]]})
    add({"id": db_id, "type": "mongodb3 in", "z": TAB, "service": "_ext_", "configNode": DB_CFG,
         "name": f"bulkWrite {collection}", "collection": collection, "operation": "bulkWrite",
         "x": 860, "y": y, "wires": [[status_id]]})
    add({"id": status_id, "type": "function", "z": TAB, "name": "Stored", "func": STORE_RESULT.strip(),
         "outputs": 1, "timeout": 0, "noerr": 0, "initialize": "", "finalize": "", "libs": [],
         "x": 1060, "y": y, "wires": [[]]})


ATAB = "an4lysis0tab0001"
BUS_IN = "an4lysisbus0in01"      # link-in that receives every analysis result
BUS_OUT = "an4lysisbus0out1"     # link-out each compute node feeds; dashboards add their link-ins here
RUNNER_IN = "an4lysisrun0in01"


def fn(name, code, x, y, wires, z=ATAB, outputs=1):
    return add({"id": nid("fn"), "type": "function", "z": z, "name": name, "func": code.strip(),
                "outputs": outputs, "timeout": 0, "noerr": 0, "initialize": "", "finalize": "", "libs": [],
                "x": x, "y": y, "wires": wires})


def build_analysis_tab():
    from analyses import ANALYSES, COMMON

    add({"id": ATAB, "type": "tab", "label": "Analysis", "disabled": False,
         "info": "Periodic analyses over the collected data (MongoDB aggregation pipelines + JavaScript). "
                 "Every result is stored in the `analytics` collection and broadcast on the analytics bus "
                 "for the dashboards."})

    # ---- shared query runner: runs msg.queries one by one, collects msg.results, returns to caller
    comment_z = lambda text, x, y, info="": add({"id": nid("cm"), "type": "comment", "z": ATAB, "name": text,
                                                "info": info, "x": x, "y": y, "wires": []})
    comment_z("Query runner (called with link call): msg.queries -> msg.results", 230, 40,
              "Each query is {key, collection, pipeline}. The runner sends them one at a time to a generic "
              "mongodb3 node (operation aggregate.toArray) and stores each result under msg.results[key].")
    ret_id, save_id, db_id, next_id = nid("lo"), nid("fn"), nid("db"), nid("fn")
    add({"id": RUNNER_IN, "type": "link in", "z": ATAB, "name": "run-queries", "links": [], "x": 115, "y": 80,
         "wires": [[next_id]]})
    add({"id": next_id, "type": "function", "z": ATAB, "name": "Next query", "outputs": 2, "timeout": 0,
         "noerr": 0, "initialize": "", "finalize": "", "libs": [], "x": 280, "y": 80,
         "func": """if (msg._qi === undefined) { msg._qi = 0; msg.results = {}; }
if (msg._qi < msg.queries.length) {
    const q = msg.queries[msg._qi];
    msg.collection = q.collection;
    msg.operation = 'aggregate.toArray';
    msg.payload = [q.pipeline, {allowDiskUse: true}];
    return [msg, null];
}
delete msg._qi;
return [null, msg];""", "wires": [[db_id], [ret_id]]})
    add({"id": db_id, "type": "mongodb3 in", "z": ATAB, "service": "_ext_", "configNode": DB_CFG,
         "name": "aggregate (msg.collection)", "collection": "", "operation": "", "x": 500, "y": 60,
         "wires": [[save_id]]})
    add({"id": save_id, "type": "function", "z": ATAB, "name": "Save result", "outputs": 1, "timeout": 0,
         "noerr": 0, "initialize": "", "finalize": "", "libs": [], "x": 700, "y": 60,
         "func": "// mongodb3 copies the result array into a plain object ({0:..,1:..}); turn it back into an array\n"
                 "const p = msg.payload;\n"
                 "msg.results[msg.queries[msg._qi].key] = Array.isArray(p) ? p : Object.values(p || {});\n"
                 "msg._qi++;\nreturn msg;",
         "wires": [[next_id]]})
    add({"id": ret_id, "type": "link out", "z": ATAB, "name": "return", "mode": "return", "links": [],
         "x": 480, "y": 110, "wires": []})

    # ---- analytics bus: store every result in `analytics` (one document per analysis, overwritten)
    comment_z("Analytics bus: store latest result of every analysis in `analytics`", 260, 180)
    store_db = nid("db")
    add({"id": BUS_IN, "type": "link in", "z": ATAB, "name": "analytics-bus", "links": [BUS_OUT],
         "x": 115, "y": 220, "wires": [[nid_peek := nid("fn")]]})
    add({"id": nid_peek, "type": "function", "z": ATAB, "name": "Prepare store", "outputs": 1, "timeout": 0,
         "noerr": 0, "initialize": "", "finalize": "", "libs": [], "x": 300, "y": 220,
         "func": """msg.payload = [{_id: msg.topic},
    {$set: {name: msg.topic, title: msg.title, computedAt: new Date(), result: msg.payload}},
    {upsert: true}];
return msg;""", "wires": [[store_db]]})
    add({"id": store_db, "type": "mongodb3 in", "z": ATAB, "service": "_ext_", "configNode": DB_CFG,
         "name": "updateOne analytics", "collection": "analytics", "operation": "updateOne",
         "x": 520, "y": 220, "wires": [[]]})

    # ---- one row per analysis: inject -> define queries -> link call runner -> compute -> bus
    y = 320
    comment_z("Analyses (run on deploy, then periodically)", 200, y - 40)
    for i, (name, title, every, q_js, c_js) in enumerate(ANALYSES):
        q_id, call_id, c_id = nid("fn"), nid("lc"), nid("fn")
        add({"id": nid("in"), "type": "inject", "z": ATAB, "name": f"every {every // 60} min",
             "props": [{"p": "payload"}], "repeat": str(every), "crontab": "", "once": True,
             "onceDelay": str(8 + i * 2), "topic": "", "payload": "", "payloadType": "date",
             "x": 140, "y": y, "wires": [[q_id]]})
        add({"id": q_id, "type": "function", "z": ATAB, "name": f"Queries: {name}", "outputs": 1, "timeout": 0,
             "noerr": 0, "initialize": "", "finalize": "", "libs": [], "x": 340, "y": y,
             "func": (COMMON + q_js).strip(), "wires": [[call_id]]})
        add({"id": call_id, "type": "link call", "z": ATAB, "name": "run-queries", "links": [RUNNER_IN],
             "linkType": "static", "timeout": "60", "x": 560, "y": y, "wires": [[c_id]]})
        compute = (COMMON + "\ntry {\nmsg = (function (msg) {\n" + c_js.strip() + "\n})(msg);\n} catch (e) {\n"
                   "    node.status({fill: 'red', shape: 'ring', text: e.message});\n    node.error(e, msg);\n"
                   "    return null;\n}\nif (!msg) return null;\n"
                   f"msg.topic = '{name}';\nmsg.title = {json.dumps(title)};\n"
                   "delete msg.results; delete msg.queries;\n"
                   "node.status({fill: 'green', shape: 'dot', text: 'updated ' + new Date().toLocaleTimeString('en-GB', {timeZone: 'Asia/Hong_Kong'})});\n"
                   "return msg;")
        add({"id": c_id, "type": "function", "z": ATAB, "name": f"Compute: {title}", "outputs": 1, "timeout": 0,
             "noerr": 0, "initialize": "", "finalize": "", "libs": [], "x": 820, "y": y,
             "func": compute, "wires": [[BUS_OUT]]})
        y += 60
    add({"id": BUS_OUT, "type": "link out", "z": ATAB, "name": "to analytics-bus", "mode": "link",
         "links": [BUS_IN], "x": 1100, "y": 320 + 60 * (len(ANALYSES) - 1) // 2, "wires": []})

    dbg = nid("dg")
    add({"id": nid("ct"), "type": "catch", "z": ATAB, "name": "Errors", "scope": None, "uncaught": False,
         "x": 140, "y": y + 40, "wires": [[dbg]]})
    add({"id": dbg, "type": "debug", "z": ATAB, "name": "Analysis errors", "active": True, "tosidebar": True,
         "console": True, "tostatus": True, "complete": "error", "targetType": "msg",
         "statusVal": "error.message", "statusType": "msg", "x": 360, "y": y + 40, "wires": []})


def build():
    sample = json.loads(SAMPLE.read_text())
    for n in sample:
        if n["type"] == "mongodb3":
            n["uri"] = "mongodb://mongo:27017/smartcity"
            n["name"] = "SmartCityDB"
        if n["type"] == "tab":
            n["label"] = "HKO Weather (sample)"

    add({"id": TAB, "type": "tab", "label": "Data Collection", "disabled": False,
         "info": "Collectors that poll data.gov.hk feeds and store them in MongoDB (database `smartcity`)."})

    collector("EPD Air Quality Health Index (past 24 h, all stations)",
              "https://www.aqhi.gov.hk/epd/ddata/html/out/24aqhi_Eng.xml", "txt", 1800,
              PARSE_AQHI, "aqhi", 100,
              "Hourly AQHI per monitoring station. The feed covers the past 24 h, so polling every "
              "30 min with upserts never misses an hour.")
    collector("Hospital Authority A&E waiting time (updated every 15 min)",
              "https://www.ha.org.hk/opendata/aed/aedwtdata2-en.json", "obj", 600,
              PARSE_AE, "ae_waiting", 200,
              "Waiting time per A&E department; text like '1.5 hours' converted to minutes.")
    collector("Transport Dept journey time indicators",
              "https://resource.data.one.gov.hk/td/jss/Journeytimev2.xml", "txt", 600,
              PARSE_JT, "journey_time", 300,
              "Journey time (min) from major locations to tunnels / destinations, colour-coded.")
    collector("Transport Dept average road speed (strategic road network)",
              "https://resource.data.one.gov.hk/td/traffic-detectors/irnAvgSpeed-all.xml", "txt", 900,
              PARSE_SPEED, "traffic_speed", 400,
              "Stores a city-wide summary (mean/median speed, % congested) plus per-segment speeds.")
    collector("Carpark vacancy (private cars)",
              "https://api.data.gov.hk/v1/carpark-info-vacancy?data=vacancy&vehicleTypes=privateCar",
              "obj", 900, PARSE_CP_VAC, "carpark_vacancy", 500,
              "One snapshot per 15-min slot with vacancy of every carpark.")
    collector("Carpark static info (daily)",
              "https://api.data.gov.hk/v1/carpark-info-vacancy?data=info&vehicleTypes=privateCar&lang=en_US",
              "obj", 86400, PARSE_CP_INFO, "carpark_info", 600,
              "Name, district and coordinates of each carpark, used to group vacancy by district.")
    collector("HKO weather warnings (stored on change)",
              "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=warnsum&lang=en",
              "obj", 600, PARSE_WARN, "weather_warnings", 700,
              "Rainstorm / typhoon / hot-weather warnings in force; a document is written only when "
              "the set of warnings changes.")

    for i, (kind, csvname) in enumerate([("temperature", "latest_1min_temperature"),
                                         ("humidity", "latest_1min_humidity"),
                                         ("wind", "latest_10min_wind")]):
        collector(f"HKO regional weather – {kind} per station",
                  f"https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/{csvname}.csv",
                  "txt", 600, parse_hko_csv(kind), "hko_regional", 800 + i * 100,
                  f"Per-station {kind} every 10 min; temperature, humidity and wind merge into the "
                  "same {station, time} document.", delay=3 + i)

    # index creation at start-up
    comment("Create MongoDB indexes at start-up", 180, 1060)
    db_idx, fn_idx = nid("db"), nid("fn")
    add({"id": nid("in"), "type": "inject", "z": TAB, "name": "on deploy", "props": [{"p": "payload"}],
         "repeat": "", "crontab": "", "once": True, "onceDelay": "1", "topic": "", "payload": "",
         "payloadType": "date", "x": 150, "y": 1100, "wires": [[fn_idx]]})
    add({"id": fn_idx, "type": "function", "z": TAB, "name": "Index definitions", "func": INDEXES.strip(),
         "outputs": 1, "timeout": 0, "noerr": 0, "initialize": "", "finalize": "", "libs": [],
         "x": 360, "y": 1100, "wires": [[db_idx]]})
    add({"id": db_idx, "type": "mongodb3 in", "z": TAB, "service": "_ext_", "configNode": DB_CFG,
         "name": "createIndex (msg.collection)", "collection": "", "operation": "",
         "x": 600, "y": 1100, "wires": [[]]})

    # error catcher
    dbg = nid("dg")
    add({"id": nid("ct"), "type": "catch", "z": TAB, "name": "Errors", "scope": None, "uncaught": False,
         "x": 140, "y": 1160, "wires": [[dbg]]})
    add({"id": dbg, "type": "debug", "z": TAB, "name": "Collector errors", "active": True, "tosidebar": True,
         "console": True, "tostatus": True, "complete": "error", "targetType": "msg",
         "statusVal": "error.message", "statusType": "msg", "x": 360, "y": 1160, "wires": []})

    build_analysis_tab()

    flows = sample + nodes
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(flows, indent=4))
    print(f"wrote {OUT} ({len(flows)} nodes)")


if __name__ == "__main__":
    build()
