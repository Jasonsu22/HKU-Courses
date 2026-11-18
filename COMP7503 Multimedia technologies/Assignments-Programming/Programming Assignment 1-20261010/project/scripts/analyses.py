"""Analysis definitions for the "Analysis" tab (imported by build_flows.py).

Each analysis = (name, title, every_s, QUERIES_JS, COMPUTE_JS)
  QUERIES_JS : function body; must set msg.queries = [{key, collection, pipeline}]
  COMPUTE_JS : function body; msg.results[key] holds each query's rows. Must set msg.payload
               (the result object, incl. chart-ready data under .charts) and return msg.
All times are grouped in Hong Kong time (+08:00).
"""

COMMON = r"""
const TZ = '+08:00';
const DAY = 864e5;
const now = new Date();
const hkHour = d => Number(new Intl.DateTimeFormat('en-GB', {timeZone: 'Asia/Hong_Kong', hour: '2-digit', hour12: false}).format(d)) % 24;
const hkDow = d => new Date(d.getTime() + 8 * 36e5).getUTCDay();   // 0 = Sunday
const r1 = v => v == null ? null : Math.round(v * 10) / 10;
const HOURS = [...Array(24).keys()].map(h => String(h).padStart(2, '0') + ':00');
"""

# ------------------------------------------------------------------ UC1 air quality
AQHI_LATEST_Q = r"""
msg.queries = [{key: 'latest', collection: 'aqhi', pipeline: [
    {$match: {time: {$gte: new Date(Date.now() - 2 * DAY)}}},
    {$sort: {time: -1}},
    {$group: {_id: '$station', time: {$first: '$time'}, aqhi: {$first: '$aqhi'},
              raw: {$first: '$aqhiRaw'}, type: {$first: '$stationType'}}},
    {$sort: {aqhi: -1, _id: 1}}]}];
return msg;
"""

AQHI_LATEST_C = r"""
// EPD health-risk bands
const band = a => a <= 3 ? 'Low' : a <= 6 ? 'Moderate' : a === 7 ? 'High' : a <= 10 ? 'Very High' : 'Serious';
const advice = {
  'Low': 'Normal activities.',
  'Moderate': 'Heart/respiratory patients: watch for symptoms.',
  'High': 'Sensitive groups: reduce outdoor exertion.',
  'Very High': 'Sensitive groups: avoid outdoor activity; others reduce exertion.',
  'Serious': 'Everyone: reduce or avoid outdoor activity.'};
const rows = msg.results.latest.map(s => ({station: s._id, type: s.type === 'Roadside Stations' ? 'Roadside' : 'General',
    aqhi: s.aqhi, display: s.raw, band: band(s.aqhi), time: s.time}));
const counts = {};
rows.forEach(r => counts[r.band] = (counts[r.band] || 0) + 1);
const worst = rows[0] || {};
const alerts = rows.filter(r => r.aqhi >= 7);
msg.payload = {
    asOf: rows.reduce((m, r) => r.time > m ? r.time : m, new Date(0)),
    stations: rows, bandCounts: counts, worst,
    worstAdvice: advice[worst.band],
    alert: alerts.length ? `${alerts.length} station(s) at High risk or above: ` + alerts.map(a => a.station).join(', ')
                         : 'No station at High health risk',
    generalMean: r1(rows.filter(r => r.type === 'General').reduce((a, r, _, A) => a + r.aqhi / A.length, 0)),
    roadsideMean: r1(rows.filter(r => r.type === 'Roadside').reduce((a, r, _, A) => a + r.aqhi / A.length, 0)),
    charts: {
        byStation: [{series: ['AQHI'], data: [rows.map(r => r.aqhi)], labels: rows.map(r => r.station)}]
    }
};
return msg;
"""

AQHI_PATTERN_Q = r"""
const typeExpr = {$cond: [{$eq: ['$stationType', 'Roadside Stations']}, 'Roadside', 'General']};
msg.queries = [
  {key: 'trend', collection: 'aqhi', pipeline: [
    {$match: {time: {$gte: new Date(Date.now() - 7 * DAY)}}},
    {$group: {_id: {t: '$time', type: typeExpr}, v: {$avg: '$aqhi'}}},
    {$sort: {'_id.t': 1}}]},
  {key: 'diurnal', collection: 'aqhi', pipeline: [
    {$match: {time: {$gte: new Date(Date.now() - 28 * DAY)}}},
    {$group: {_id: {h: {$hour: {date: '$time', timezone: TZ}}, type: typeExpr}, v: {$avg: '$aqhi'}}}]},
  {key: 'daily', collection: 'aqhi', pipeline: [
    {$group: {_id: {$dateToString: {format: '%Y-%m-%d', date: '$time', timezone: TZ}},
              mean: {$avg: '$aqhi'}, max: {$max: '$aqhi'}}},
    {$sort: {_id: 1}}]}
];
return msg;
"""

AQHI_PATTERN_C = r"""
const series = ['General', 'Roadside'];
const trend = series.map(s => msg.results.trend.filter(d => d._id.type === s).map(d => ({x: new Date(d._id.t).getTime(), y: r1(d.v)})));
const diurnal = series.map(s => { const a = Array(24).fill(null);
    msg.results.diurnal.filter(d => d._id.type === s).forEach(d => a[d._id.h] = r1(d.v)); return a; });
const peakHour = diurnal[1].indexOf(Math.max(...diurnal[1].filter(v => v != null)));
const lowHour = diurnal[1].indexOf(Math.min(...diurnal[1].filter(v => v != null)));
const daily = msg.results.daily;
const worstDay = daily.reduce((m, d) => (!m || d.mean > m.mean) ? d : m, null);
msg.payload = {
    diurnal: {general: diurnal[0], roadside: diurnal[1]},
    insight: `Roadside AQHI peaks around ${HOURS[peakHour]} (${diurnal[1][peakHour]}) and is lowest around ${HOURS[lowHour]} (${diurnal[1][lowHour]}); ` +
             `the roadside-general gap reflects vehicle emissions.`,
    worstDay: worstDay && {date: worstDay._id, mean: r1(worstDay.mean), max: worstDay.max},
    days: daily.length,
    charts: {
        trend: [{series, data: trend, labels: ['']}],
        diurnal: [{series, data: diurnal, labels: HOURS}],
        daily: [{series: ['Daily mean AQHI', 'Daily max AQHI'],
                 data: [daily.map(d => ({x: new Date(d._id + 'T12:00:00+08:00').getTime(), y: r1(d.mean)})),
                        daily.map(d => ({x: new Date(d._id + 'T12:00:00+08:00').getTime(), y: d.max}))], labels: ['']}]
    }
};
return msg;
"""

# ------------------------------------------------------------------ UC2 A&E
AE_STATUS_Q = r"""
msg.queries = [
  {key: 'latest', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - DAY)}}},
    {$sort: {updateTime: -1}},
    {$group: {_id: '$hospital', t: {$first: '$updateTime'}, t3: {$first: '$t3P50Min'}, t3p95: {$first: '$t3P95Min'},
              t45: {$first: '$t45P50Min'}, t45p95: {$first: '$t45P95Min'},
              m1: {$first: '$managingT1'}, m2: {$first: '$managingT2'}}}]},
  {key: 'typical', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - 28 * DAY)}}},
    {$group: {_id: {hosp: '$hospital', h: {$hour: {date: '$updateTime', timezone: TZ}}},
              t45: {$avg: '$t45P50Min'}, t3: {$avg: '$t3P50Min'}}}]}
];
return msg;
"""

AE_STATUS_C = r"""
const h = hkHour(now);
const typ = {};
msg.results.typical.filter(d => d._id.h === h).forEach(d => typ[d._id.hosp] = d);
const rows = msg.results.latest.map(d => {
    const t = typ[d._id] || {};
    const ratio = t.t45 ? d.t45 / t.t45 : null;
    return {hospital: d._id, updateTime: d.t,
            t3: d.t3, t45: d.t45, t45p95: d.t45p95,
            typicalT45: r1(t.t45), vsTypicalPct: ratio == null ? null : Math.round((ratio - 1) * 100),
            // flag only when both relatively (±30%) and absolutely (±20 min) different from the norm
            status: ratio == null ? 'n/a' : (ratio >= 1.3 && d.t45 - t.t45 >= 20) ? 'Busier than usual'
                  : (ratio <= 0.7 && t.t45 - d.t45 >= 20) ? 'Quieter than usual' : 'Normal',
            managingCritical: d.m1 || d.m2};
}).sort((a, b) => a.t45 - b.t45);
const mean = rows.reduce((a, r) => a + r.t45, 0) / (rows.length || 1);
const meanTyp = rows.filter(r => r.typicalT45).reduce((a, r, _, A) => a + r.typicalT45 / A.length, 0);
const busy = rows.filter(r => r.status === 'Busier than usual');
msg.payload = {
    asOf: rows[0] && rows[0].updateTime, hour: h,
    hospitals: rows,
    shortest: rows[0], longest: rows[rows.length - 1],
    territoryMeanT45: r1(mean), territoryTypicalT45: r1(meanTyp),
    alert: busy.length ? `${busy.length} A&E department(s) busier than usual for ${HOURS[h]}: ` + busy.map(b => b.hospital).join(', ')
                       : `All A&E departments within normal range for ${HOURS[h]}`,
    charts: {
        byHospital: [{series: ['Now (median, semi/non-urgent)', 'Typical at this hour'],
                      data: [rows.map(r => r.t45), rows.map(r => r.typicalT45)],
                      labels: rows.map(r => r.hospital.replace(/ Hospital| Medical Centre| Nethersole/g, ''))}]
    }
};
return msg;
"""

AE_PATTERN_Q = r"""
msg.queries = [
  {key: 'trend', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - 7 * DAY)}}},
    {$group: {_id: {$dateTrunc: {date: '$updateTime', unit: 'hour'}}, t45: {$avg: '$t45P50Min'}, t3: {$avg: '$t3P50Min'}}},
    {$sort: {_id: 1}}]},
  {key: 'diurnal', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - 28 * DAY)}}},
    {$group: {_id: {$hour: {date: '$updateTime', timezone: TZ}}, t45: {$avg: '$t45P50Min'}, t3: {$avg: '$t3P50Min'}}}]},
  {key: 'weekday', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - 28 * DAY)}}},
    {$group: {_id: {$dayOfWeek: {date: '$updateTime', timezone: TZ}}, t45: {$avg: '$t45P50Min'}}}]},
  {key: 'hospitals', collection: 'ae_waiting', pipeline: [
    {$match: {updateTime: {$gte: new Date(Date.now() - 28 * DAY)}}},
    {$group: {_id: '$hospital', t45: {$avg: '$t45P50Min'}, p95: {$avg: '$t45P95Min'}}},
    {$sort: {t45: -1}}]}
];
return msg;
"""

AE_PATTERN_C = r"""
const R = msg.results;
const d45 = Array(24).fill(null), d3 = Array(24).fill(null);
R.diurnal.forEach(d => { d45[d._id] = r1(d.t45); d3[d._id] = r1(d.t3); });
const DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const wk = Array(7).fill(null);
R.weekday.forEach(d => wk[d._id - 1] = r1(d.t45));
const vals = d45.filter(v => v != null);
const peak = d45.indexOf(Math.max(...vals)), low = d45.indexOf(Math.min(...vals));
const best = DOW[wk.indexOf(Math.min(...wk.filter(v => v != null)))];
const worst = DOW[wk.indexOf(Math.max(...wk.filter(v => v != null)))];
msg.payload = {
    diurnal: {t45: d45, t3: d3}, weekday: wk,
    hospitalRanking: R.hospitals.map(h => ({hospital: h._id, avgT45: r1(h.t45), avgP95: r1(h.p95)})),
    insight: `Semi/non-urgent waits are shortest around ${HOURS[low]} (${d45[low]} min) and longest around ${HOURS[peak]} (${d45[peak]} min). ` +
             `${best} is the quietest day and ${worst} the busiest.`,
    charts: {
        trend: [{series: ['Semi/non-urgent (P50)', 'Urgent (P50)'],
                 data: [R.trend.map(d => ({x: new Date(d._id).getTime(), y: r1(d.t45)})),
                        R.trend.map(d => ({x: new Date(d._id).getTime(), y: r1(d.t3)}))], labels: ['']}],
        diurnal: [{series: ['Semi/non-urgent (P50)', 'Urgent (P50)'], data: [d45, d3], labels: HOURS}],
        weekday: [{series: ['Semi/non-urgent (P50)'], data: [wk], labels: DOW}],
        ranking: [{series: ['28-day average wait (min)'], data: [R.hospitals.map(h => r1(h.t45))],
                   labels: R.hospitals.map(h => h._id.replace(/ Hospital| Medical Centre| Nethersole/g, ''))}]
    }
};
return msg;
"""

# ------------------------------------------------------------------ UC3 mobility
TRAFFIC_STATUS_Q = r"""
const dayType = {$cond: [{$in: [{$dayOfWeek: {date: '$snapshotTime', timezone: TZ}}, [1, 7]]}, 'weekend', 'weekday']};
msg.queries = [
  {key: 'latest', collection: 'traffic_speed', pipeline: [
    {$sort: {snapshotTime: -1}}, {$limit: 1}, {$project: {speeds: 0}}]},
  {key: 'typical', collection: 'traffic_speed', pipeline: [
    {$group: {_id: {h: {$hour: {date: '$snapshotTime', timezone: TZ}}, dt: dayType},
              speed: {$avg: '$meanSpeed'}, cong: {$avg: '$pctBelow30'}}}]},
  {key: 'jtLatest', collection: 'journey_time', pipeline: [
    {$match: {captureTime: {$gte: new Date(Date.now() - 3 * 36e5)}, journeyType: 1}},
    {$sort: {captureTime: -1}},
    {$group: {_id: {from: '$from', to: '$to'}, t: {$first: '$captureTime'}, v: {$first: '$value'}, c: {$first: '$colour'}}}]},
  {key: 'jtTypical', collection: 'journey_time', pipeline: [
    {$match: {journeyType: 1}},
    {$group: {_id: {from: '$from', to: '$to', h: {$hour: {date: '$captureTime', timezone: TZ}}}, v: {$avg: '$value'}}}]}
];
return msg;
"""

TRAFFIC_STATUS_C = r"""
const R = msg.results;
const L = R.latest[0] || {};
const t = L.snapshotTime ? new Date(L.snapshotTime) : now;
const h = hkHour(t), dt = [0, 6].includes(hkDow(t)) ? 'weekend' : 'weekday';
const typ = R.typical.find(d => d._id.h === h && d._id.dt === dt) || {};
const jtTyp = {};
R.jtTypical.filter(d => d._id.h === hkHour(now)).forEach(d => jtTyp[d._id.from + '>' + d._id.to] = d.v);
const routes = R.jtLatest.map(d => {
    const k = d._id.from + '>' + d._id.to, ty = jtTyp[k];
    return {route: d._id.from + ' → ' + d._id.to, minutes: d.v, colour: ['', 'Red', 'Amber', 'Green'][d.c] || '?',
            typical: r1(ty), delayMin: ty == null || d.v == null ? null : r1(d.v - ty)};
}).sort((a, b) => (b.delayMin ?? -99) - (a.delayMin ?? -99));
const red = routes.filter(r => r.colour === 'Red');
const delta = typ.speed ? r1(L.meanSpeed - typ.speed) : null;
msg.payload = {
    asOf: L.snapshotTime, meanSpeed: L.meanSpeed, pctBelow30: L.pctBelow30, pctBelow15: L.pctBelow15,
    validSegments: L.validSegments, typicalSpeed: r1(typ.speed), typicalPctBelow30: r1(typ.cong), speedDelta: delta,
    status: delta == null ? 'n/a' : delta <= -3 ? 'Slower than usual' : delta >= 3 ? 'Faster than usual' : 'Normal',
    routes, redRoutes: red.length,
    alert: red.length ? `Congested (red) routes: ` + red.map(r => r.route).join(', ') : 'No route currently red',
    charts: {
        routeDelay: [{series: ['Now (min)', 'Typical at this hour (min)'],
                      data: [routes.slice(0, 12).map(r => r.minutes), routes.slice(0, 12).map(r => r.typical)],
                      labels: routes.slice(0, 12).map(r => r.route)}]
    }
};
return msg;
"""

TRAFFIC_PATTERN_Q = r"""
const dayType = {$cond: [{$in: [{$dayOfWeek: {date: '$snapshotTime', timezone: TZ}}, [1, 7]]}, 'weekend', 'weekday']};
msg.queries = [
  {key: 'diurnal', collection: 'traffic_speed', pipeline: [
    {$group: {_id: {h: {$hour: {date: '$snapshotTime', timezone: TZ}}, dt: dayType},
              speed: {$avg: '$meanSpeed'}, cong: {$avg: '$pctBelow30'}}}]},
  {key: 'trend', collection: 'traffic_speed', pipeline: [
    {$match: {snapshotTime: {$gte: new Date(Date.now() - 7 * DAY)}}},
    {$sort: {snapshotTime: 1}}, {$project: {snapshotTime: 1, meanSpeed: 1, pctBelow30: 1}}]}
];
return msg;
"""

TRAFFIC_PATTERN_C = r"""
const R = msg.results;
const prof = (dt, f) => { const a = Array(24).fill(null); R.diurnal.filter(d => d._id.dt === dt).forEach(d => a[d._id.h] = r1(d[f])); return a; };
const wd = prof('weekday', 'speed'), we = prof('weekend', 'speed');
const wdc = prof('weekday', 'cong'), wec = prof('weekend', 'cong');
const minIdx = a => a.indexOf(Math.min(...a.filter(v => v != null)));
const am = wd.slice(6, 11), pm = wd.slice(16, 21);
const amH = 6 + am.indexOf(Math.min(...am.filter(v => v != null)));
const pmH = 16 + pm.indexOf(Math.min(...pm.filter(v => v != null)));
msg.payload = {
    weekday: wd, weekend: we, weekdayCongestion: wdc, weekendCongestion: wec,
    insight: `On weekdays the network is slowest at ${HOURS[amH]} (${wd[amH]} km/h) and ${HOURS[pmH]} (${wd[pmH]} km/h) rush hours; ` +
             `weekend speeds at ${HOURS[pmH]} are ${r1(we[pmH] - wd[pmH])} km/h higher.`,
    charts: {
        diurnal: [{series: ['Weekday', 'Weekend'], data: [wd, we], labels: HOURS}],
        congestion: [{series: ['Weekday', 'Weekend'], data: [wdc, wec], labels: HOURS}],
        trend: [{series: ['Mean speed (km/h)', '% segments < 30 km/h'],
                 data: [R.trend.map(d => ({x: new Date(d.snapshotTime).getTime(), y: d.meanSpeed})),
                        R.trend.map(d => ({x: new Date(d.snapshotTime).getTime(), y: d.pctBelow30}))], labels: ['']}]
    }
};
return msg;
"""

CARPARK_Q = r"""
msg.queries = [
  {key: 'district', collection: 'carpark_vacancy', pipeline: [
    {$sort: {slotTime: -1}}, {$limit: 1},
    {$unwind: '$parks'},
    {$match: {'parks.type': 'A', 'parks.vacancy': {$gte: 0}}},
    {$lookup: {from: 'carpark_info', localField: 'parks.id', foreignField: 'park_Id', as: 'info'}},
    {$unwind: '$info'},
    {$set: {districtName: {$trim: {input: {$replaceAll: {input: {$ifNull: ['$info.district', 'Unknown']}, find: ' District', replacement: ''}}}}}},
    {$group: {_id: '$districtName', slot: {$first: '$slotTime'}, vacancy: {$sum: '$parks.vacancy'}, parks: {$sum: 1},
              full: {$sum: {$cond: [{$eq: ['$parks.vacancy', 0]}, 1, 0]}}}},
    {$sort: {vacancy: -1}}]},
  {key: 'trend', collection: 'carpark_vacancy', pipeline: [
    {$match: {slotTime: {$gte: new Date(Date.now() - 7 * DAY)}}},
    {$sort: {slotTime: 1}}, {$project: {slotTime: 1, totalVacancy: 1}}]},
  {key: 'diurnal', collection: 'carpark_vacancy', pipeline: [
    {$group: {_id: {$hour: {date: '$slotTime', timezone: TZ}}, v: {$avg: '$totalVacancy'}}}]}
];
return msg;
"""

CARPARK_C = r"""
const R = msg.results;
const rows = R.district.filter(d => d._id).map(d => ({district: d._id, vacancy: d.vacancy, parks: d.parks, full: d.full,
    perPark: r1(d.vacancy / d.parks)}));
const tight = rows.slice().sort((a, b) => a.perPark - b.perPark).slice(0, 3);
const di = Array(24).fill(null);
R.diurnal.forEach(d => di[d._id] = Math.round(d.v));
msg.payload = {
    asOf: R.district[0] && R.district[0].slot,
    districts: rows, totalVacancy: rows.reduce((a, r) => a + r.vacancy, 0),
    fullCarparks: rows.reduce((a, r) => a + r.full, 0),
    tightest: tight,
    insight: tight.length ? 'Hardest to park now (fewest free spaces per carpark): ' + tight.map(t => `${t.district} (${t.perPark})`).join(', ') : '',
    charts: {
        district: [{series: ['Free private-car spaces'], data: [rows.map(r => r.vacancy)], labels: rows.map(r => r.district.replace(' District', ''))}],
        trend: [{series: ['Total free spaces'], data: [R.trend.map(d => ({x: new Date(d.slotTime).getTime(), y: d.totalVacancy}))], labels: ['']}],
        diurnal: [{series: ['Average free spaces'], data: [di], labels: HOURS}]
    }
};
return msg;
"""

# ------------------------------------------------------------------ cross-domain correlation
CORR_Q = r"""
const since = new Date(Date.now() - 42 * DAY);
const hourKey = f => ({$dateTrunc: {date: '$' + f, unit: 'hour'}});
const H = (key, collection, tf, val, match) => ({key, collection, pipeline: [
    {$match: Object.assign({[tf]: {$gte: since}}, match || {})},
    {$group: {_id: hourKey(tf), v: {$avg: val}}}]});
msg.queries = [
  H('aqhiGeneral', 'aqhi', 'time', '$aqhi', {stationType: 'General Stations'}),
  H('aqhiRoadside', 'aqhi', 'time', '$aqhi', {stationType: 'Roadside Stations'}),
  H('temperature', 'hko_regional', 'time', '$temperature'),
  H('humidity', 'hko_regional', 'time', '$humidity'),
  H('windSpeed', 'hko_regional', 'time', '$windSpeed'),
  H('aeWait', 'ae_waiting', 'updateTime', '$t45P50Min'),
  H('roadSpeed', 'traffic_speed', 'snapshotTime', '$meanSpeed'),
  {key: 'rainfall', collection: 'Weather Report', pipeline: [
    {$project: {t: {$dateTrunc: {date: {$toDate: '$rainfall.endTime'}, unit: 'hour'}}, rain: {$max: '$rainfall.data.max'}}},
    {$group: {_id: '$t', v: {$max: '$rain'}}}]}
];
return msg;
"""

CORR_C = r"""
// Hourly series aligned on the hour, then Pearson r twice:
//  raw r     : includes the shared daily rhythm (everything follows the clock)
//  adjusted r: each value minus that variable's mean for the same hour-of-day,
//              so only day-to-day deviations are compared (removes the diurnal confound)
const LABEL = {aqhiGeneral: 'AQHI (general)', aqhiRoadside: 'AQHI (roadside)', temperature: 'Temperature',
               humidity: 'Humidity', windSpeed: 'Wind speed', aeWait: 'A&E wait', roadSpeed: 'Road speed', rainfall: 'Rainfall'};
const S = {};
for (const k of Object.keys(LABEL)) {
    S[k] = {};
    (msg.results[k] || []).forEach(d => { if (d._id && d.v != null) S[k][new Date(d._id).getTime()] = d.v; });
}
function anomalies(ser) {
    const sum = Array(24).fill(0), n = Array(24).fill(0), out = {};
    for (const t in ser) { const h = hkHour(new Date(+t)); sum[h] += ser[t]; n[h]++; }
    for (const t in ser) { const h = hkHour(new Date(+t)); out[t] = ser[t] - sum[h] / n[h]; }
    return out;
}
function pearson(a, b) {
    const ks = Object.keys(a).filter(k => k in b), n = ks.length;
    if (n < 24) return {r: null, n};
    const x = ks.map(k => a[k]), y = ks.map(k => b[k]);
    const mx = x.reduce((p, c) => p + c) / n, my = y.reduce((p, c) => p + c) / n;
    let sxy = 0, sxx = 0, syy = 0;
    for (let i = 0; i < n; i++) { sxy += (x[i] - mx) * (y[i] - my); sxx += (x[i] - mx) ** 2; syy += (y[i] - my) ** 2; }
    return {r: sxx && syy ? Math.round(sxy / Math.sqrt(sxx * syy) * 100) / 100 : null, n};
}
const A = {};
for (const k in S) A[k] = anomalies(S[k]);
const keys = Object.keys(LABEL), pairs = [];
for (let i = 0; i < keys.length; i++) for (let j = i + 1; j < keys.length; j++) {
    const raw = pearson(S[keys[i]], S[keys[j]]), adj = pearson(A[keys[i]], A[keys[j]]);
    pairs.push({a: LABEL[keys[i]], b: LABEL[keys[j]], rawR: raw.r, adjustedR: adj.r, n: raw.n,
                strength: adj.r == null ? 'insufficient data' : Math.abs(adj.r) >= 0.5 ? 'strong' : Math.abs(adj.r) >= 0.3 ? 'moderate' : Math.abs(adj.r) >= 0.1 ? 'weak' : 'none'});
}
pairs.sort((p, q) => Math.abs(q.adjustedR ?? 0) - Math.abs(p.adjustedR ?? 0));
// scatter data for the headline pairs (hourly anomalies)
function scatter(ka, kb) { return Object.keys(A[ka]).filter(t => t in A[kb]).map(t => ({x: r1(S[ka][t]), y: r1(S[kb][t])})); }
// rain impact on road speed (needs live rainfall)
const rainy = [], dry = [];
for (const t in A.roadSpeed) if (t in S.rainfall) (S.rainfall[t] > 0 ? rainy : dry).push(A.roadSpeed[t]);
const avg = a => a.length ? a.reduce((p, c) => p + c, 0) / a.length : null;
msg.payload = {
    variables: keys.map(k => ({key: k, label: LABEL[k], hours: Object.keys(S[k]).length})),
    pairs,
    top: pairs.filter(p => p.adjustedR != null).slice(0, 5),
    rainImpact: {rainyHours: rainy.length, dryHours: dry.length,
                 speedAnomalyRain: r1(avg(rainy)), speedAnomalyDry: r1(avg(dry)),
                 note: rainy.length < 6 ? 'Not enough rainy hours collected yet' :
                       `Road speed is ${r1(avg(rainy) - avg(dry))} km/h vs dry hours at the same time of day`},
    charts: {
        scatterTempAqhi: scatter('temperature', 'aqhiGeneral'),
        scatterAqhiAe: scatter('aqhiRoadside', 'aeWait'),
        scatterHumSpeed: scatter('humidity', 'roadSpeed')
    }
};
return msg;
"""

# ------------------------------------------------------------------ current weather & data health
WEATHER_Q = r"""
msg.queries = [
  {key: 'stations', collection: 'hko_regional', pipeline: [
    {$match: {time: {$gte: new Date(Date.now() - 45 * 60e3)}}},
    {$sort: {time: -1}},
    {$group: {_id: '$station', time: {$first: '$time'}, temp: {$max: '$temperature'}, hum: {$max: '$humidity'},
              wind: {$max: '$windSpeed'}, gust: {$max: '$gust'}}}]},
  {key: 'warnings', collection: 'weather_warnings', pipeline: [{$sort: {observedAt: -1}}, {$limit: 1}]},
  {key: 'report', collection: 'Weather Report', pipeline: [{$sort: {_id: -1}}, {$limit: 1},
    {$project: {rainfall: 1, updateTime: 1}}]},
  {key: 'trend', collection: 'hko_regional', pipeline: [
    {$match: {time: {$gte: new Date(Date.now() - 2 * DAY)}}},
    {$group: {_id: {$dateTrunc: {date: '$time', unit: 'hour'}}, temp: {$avg: '$temperature'}, hum: {$avg: '$humidity'}}},
    {$sort: {_id: 1}}]}
];
return msg;
"""

WEATHER_C = r"""
const R = msg.results, st = R.stations;
const avg = f => { const v = st.map(s => s[f]).filter(x => x != null); return v.length ? r1(v.reduce((a, b) => a + b, 0) / v.length) : null; };
const ext = (f, cmp) => st.filter(s => s[f] != null).reduce((m, s) => !m || cmp(s[f], m[f]) ? s : m, null);
const hot = ext('temp', (a, b) => a > b), cool = ext('temp', (a, b) => a < b), gusty = ext('gust', (a, b) => a > b);
const w = R.warnings[0] || {warnings: []};
const rain = R.report[0] && R.report[0].rainfall;
const maxRain = rain ? Math.max(...rain.data.map(d => d.max || 0)) : null;
msg.payload = {
    asOf: st.reduce((m, s) => s.time > m ? s.time : m, new Date(0)),
    temperature: avg('temp'), humidity: avg('hum'), windSpeed: avg('wind'),
    hottest: hot && {station: hot._id, temp: hot.temp}, coolest: cool && {station: cool._id, temp: cool.temp},
    gustiest: gusty && {station: gusty._id, gust: gusty.gust},
    warnings: w.warnings.map(x => x.name), maxHourlyRain: maxRain,
    charts: {
        trend: [{series: ['Temperature (°C)'], data: [R.trend.map(d => ({x: new Date(d._id).getTime(), y: r1(d.temp)}))], labels: ['']}]
    }
};
return msg;
"""

HEALTH_Q = r"""
const C = [['Weather Report', 'updateTime'], ['hko_regional', 'time'], ['weather_warnings', 'observedAt'],
           ['aqhi', 'time'], ['ae_waiting', 'updateTime'], ['journey_time', 'captureTime'],
           ['traffic_speed', 'snapshotTime'], ['carpark_vacancy', 'slotTime'], ['carpark_info', 'updatedAt']];
msg.queries = C.map(([c, f]) => ({key: c, collection: c, pipeline: [
    {$group: {_id: null, n: {$sum: 1}, first: {$min: '$' + f}, last: {$max: '$' + f},
              archived: {$sum: {$cond: [{$eq: ['$source', 'archive']}, 1, 0]}}}}]}));
return msg;
"""

HEALTH_C = r"""
const rows = Object.keys(msg.results).map(c => {
    const d = msg.results[c][0] || {};
    const last = d.last ? new Date(d.last) : null;
    const ageMin = last ? Math.round((now - last) / 60e3) : null;
    return {collection: c, documents: d.n || 0, archived: d.archived || 0,
            first: d.first ? new Date(d.first) : null, last, ageMin,
            days: d.first ? r1((last - new Date(d.first)) / DAY) : 0};
});
msg.payload = {collections: rows, totalDocuments: rows.reduce((a, r) => a + r.documents, 0)};
return msg;
"""

ANALYSES = [
    ("weather_now", "Current weather", 600, WEATHER_Q, WEATHER_C),
    ("data_health", "Data collection health", 600, HEALTH_Q, HEALTH_C),
    ("aqhi_latest", "UC1 · Current AQHI & health risk", 900, AQHI_LATEST_Q, AQHI_LATEST_C),
    ("aqhi_patterns", "UC1 · AQHI trend & daily pattern", 1800, AQHI_PATTERN_Q, AQHI_PATTERN_C),
    ("ae_status", "UC2 · A&E waiting now vs typical", 900, AE_STATUS_Q, AE_STATUS_C),
    ("ae_patterns", "UC2 · A&E waiting patterns", 1800, AE_PATTERN_Q, AE_PATTERN_C),
    ("traffic_status", "UC3 · Traffic now vs typical", 900, TRAFFIC_STATUS_Q, TRAFFIC_STATUS_C),
    ("traffic_patterns", "UC3 · Traffic patterns", 1800, TRAFFIC_PATTERN_Q, TRAFFIC_PATTERN_C),
    ("carpark_status", "UC3 · Carpark vacancy by district", 900, CARPARK_Q, CARPARK_C),
    ("correlations", "Cross-domain correlation analysis", 1800, CORR_Q, CORR_C),
]
