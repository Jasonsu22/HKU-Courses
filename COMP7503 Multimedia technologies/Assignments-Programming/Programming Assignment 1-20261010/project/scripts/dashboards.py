"""Dashboard pages (node-red-dashboard 3.x) fed by the analytics bus. Imported by build_flows.py.

Pages: Overview · Air Quality (UC1) · A&E (UC2) · Mobility (UC3) · Correlations.
Charts use ui_chart (built-in hover tooltips); tables, KPI cards, heatmap and scatter plots are
HTML/SVG strings built in function nodes and rendered by a ui_template.
Colours: validated categorical slots (dark) blue/orange/aqua; status colours always with icon + label.
"""
import json

DTAB = "da5hboard0tab001"
DASH_IN = "da5hboard0in0001"

# validated dark-mode slots (dataviz reference palette)
S1, S2, S3 = "#3987e5", "#d95926", "#199e70"
SERIES = [S1, S2, S3, "#c98500", "#d55181", "#0ca30c", "#9085e9", "#e66767", "#c3c2b7"]

# JS shared by every view function: escaping, status badges, tables, KPI cards, heatmap, scatter
VIEW_LIB = r"""
const C = {text: '#f0efec', text2: '#c3c2b7', muted: '#8f8e88', line: '#383835', surface: '#1a1a19',
           good: '#0ca30c', warning: '#fab219', serious: '#ec835a', critical: '#d03b3b',
           blue: '#3987e5', red: '#e66767', mid: '#383835'};
const esc = s => String(s ?? '–').replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
const fmtT = d => d ? new Date(d).toLocaleString('en-GB', {timeZone: 'Asia/Hong_Kong', day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'}) : '–';
const fmtN = (v, dp = 0) => v == null ? '–' : Number(v).toLocaleString('en-GB', {maximumFractionDigits: dp, minimumFractionDigits: dp});
// status -> colour + icon + label (never colour alone)
const STATUS = {good: ['●', C.good], warning: ['▲', C.warning], serious: ['▲', C.serious], critical: ['■', C.critical], neutral: ['○', C.muted]};
const badge = (level, label) => { const [i, c] = STATUS[level] || STATUS.neutral;
    return `<span style="color:${c};font-weight:600;white-space:nowrap">${i} <span style="color:${C.text}">${esc(label)}</span></span>`; };
const AQHI_LEVEL = {'Low': 'good', 'Moderate': 'warning', 'High': 'serious', 'Very High': 'critical', 'Serious': 'critical'};
const WRAP = 'font-size:13px;color:' + C.text + ';line-height:1.45';
function table(cols, rows) {
    const th = cols.map(c => `<th style="text-align:${c.num ? 'right' : 'left'};padding:4px 8px;color:${C.text2};font-weight:500;border-bottom:1px solid ${C.line}">${esc(c.h)}</th>`).join('');
    const tr = rows.map(r => '<tr>' + cols.map(c => `<td style="text-align:${c.num ? 'right' : 'left'};padding:4px 8px;border-bottom:1px solid ${C.line};font-variant-numeric:tabular-nums">${c.html ? c.f(r) : esc(c.f(r))}</td>`).join('') + '</tr>').join('');
    return `<div style="overflow-x:auto;${WRAP}"><table style="width:100%;border-collapse:collapse">${'<tr>' + th + '</tr>'}${tr}</table></div>`;
}
function card(title, value, unit, sub) {
    return `<div style="flex:1 1 150px;min-width:150px;padding:10px 12px;border:1px solid ${C.line};border-radius:8px">
      <div style="font-size:12px;color:${C.text2}">${esc(title)}</div>
      <div style="font-size:28px;font-weight:600;color:${C.text};font-variant-numeric:tabular-nums">${esc(value)}<span style="font-size:14px;color:${C.text2};font-weight:400"> ${esc(unit || '')}</span></div>
      <div style="font-size:12px;color:${C.text2};margin-top:2px">${sub || ''}</div></div>`;
}
const cards = list => `<div style="display:flex;flex-wrap:wrap;gap:8px;${WRAP}">${list.join('')}</div>`;
const note = (txt, by) => `<div style="${WRAP}">${txt}${by ? `<div style="color:${C.muted};font-size:11px;margin-top:6px">${esc(by)}</div>` : ''}</div>`;
// diverging blue <-> grey <-> red for correlation r in [-1, 1]
function divColor(r) {
    if (r == null) return 'transparent';
    const hex = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
    const [a, b] = r < 0 ? [hex(C.mid), hex(C.blue)] : [hex(C.mid), hex(C.red)];
    const t = Math.min(1, Math.abs(r));
    return 'rgb(' + a.map((v, i) => Math.round(v + (b[i] - v) * t)).join(',') + ')';
}
function scatter(points, xl, yl, colour) {
    const W = 340, H = 240, P = {l: 44, r: 10, t: 10, b: 36};
    if (!points || points.length < 3) return note('Not enough data yet.');
    const xs = points.map(p => p.x), ys = points.map(p => p.y);
    const [x0, x1] = [Math.min(...xs), Math.max(...xs)], [y0, y1] = [Math.min(...ys), Math.max(...ys)];
    const sx = v => P.l + (v - x0) / ((x1 - x0) || 1) * (W - P.l - P.r), sy = v => H - P.b - (v - y0) / ((y1 - y0) || 1) * (H - P.t - P.b);
    const n = points.length, mx = xs.reduce((a, b) => a + b) / n, my = ys.reduce((a, b) => a + b) / n;
    let sxy = 0, sxx = 0, syy = 0; points.forEach(p => { sxy += (p.x - mx) * (p.y - my); sxx += (p.x - mx) ** 2; syy += (p.y - my) ** 2; });
    const k = sxy / sxx, r = sxy / Math.sqrt(sxx * syy);
    const ticks = (a, b) => [a, (a + b) / 2, b];
    const dots = points.map(p => `<circle cx="${sx(p.x).toFixed(1)}" cy="${sy(p.y).toFixed(1)}" r="2.5" fill="${colour}" fill-opacity="0.35"><title>${p.x}, ${p.y}</title></circle>`).join('');
    const axis = ticks(x0, x1).map(v => `<text x="${sx(v)}" y="${H - P.b + 14}" fill="${C.text2}" font-size="10" text-anchor="middle">${fmtN(v, 1)}</text>`).join('') +
                 ticks(y0, y1).map(v => `<text x="${P.l - 6}" y="${sy(v) + 3}" fill="${C.text2}" font-size="10" text-anchor="end">${fmtN(v, 0)}</text>`).join('');
    const fit = `<line x1="${sx(x0)}" y1="${sy(my + k * (x0 - mx))}" x2="${sx(x1)}" y2="${sy(my + k * (x1 - mx))}" stroke="${C.text}" stroke-width="2" stroke-dasharray="5 4"/>`;
    return `<div style="${WRAP}"><svg viewBox="0 0 ${W} ${H}" style="width:100%;height:auto;display:block">
      <line x1="${P.l}" y1="${H - P.b}" x2="${W - P.r}" y2="${H - P.b}" stroke="${C.line}"/><line x1="${P.l}" y1="${P.t}" x2="${P.l}" y2="${H - P.b}" stroke="${C.line}"/>
      ${dots}${fit}${axis}
      <text x="${(W + P.l) / 2}" y="${H - 4}" fill="${C.text2}" font-size="11" text-anchor="middle">${esc(xl)}</text>
      <text x="12" y="${(H - P.b) / 2}" fill="${C.text2}" font-size="11" text-anchor="middle" transform="rotate(-90 12 ${(H - P.b) / 2})">${esc(yl)}</text>
    </svg><div style="color:${C.text2};font-size:12px">${n} hourly points · Pearson r = <b style="color:${C.text}">${fmtN(r, 2)}</b> · dashed line = least-squares fit</div></div>`;
}
const m = p => ({payload: p});
// time-axis charts: shift x by +8 h and render with useUTC, so axes read in Hong Kong time on any computer
const hk = ch => ch.map(c => Object.assign({}, c, {data: c.data.map(s => s.map(pt => ({x: pt.x + 288e5, y: pt.y})))}));
"""

# ------------------------------------------------------------------ view functions (one per analysis)
# Each returns an array of messages, one per output, in the order of the widgets listed in PAGES.

VIEWS = {}

VIEWS["aqhi_latest"] = r"""
const p = msg.payload;
const kpi = cards([
  card('Highest AQHI now', p.worst.display, '', `${esc(p.worst.station)} · ${badge(AQHI_LEVEL[p.worst.band], p.worst.band + ' risk')}`),
  card('General stations (mean)', fmtN(p.generalMean, 1), '', 'Background exposure'),
  card('Roadside stations (mean)', fmtN(p.roadsideMean, 1), '', 'Street-level exposure'),
]) + note(`<div style="margin-top:8px">${badge(p.worst.aqhi >= 7 ? 'serious' : 'good', p.alert)}</div>
  <div style="color:${C.text2};margin-top:4px">Health advice for the worst station: ${esc(p.worstAdvice)}</div>`, 'Updated ' + fmtT(p.asOf));
const tbl = table([
  {h: 'Station', f: r => r.station}, {h: 'Type', f: r => r.type}, {h: 'AQHI', num: true, f: r => r.display},
  {h: 'Health risk', html: true, f: r => badge(AQHI_LEVEL[r.band], r.band)}], p.stations);
return [m(kpi), m(p.charts.byStation), m(tbl)];
"""

VIEWS["aqhi_patterns"] = r"""
const p = msg.payload;
const wd = p.worstDay ? ` Worst day in the record: <b>${esc(p.worstDay.date)}</b> (mean ${p.worstDay.mean}, peak ${p.worstDay.max}).` : '';
return [m(hk(p.charts.trend)), m(p.charts.diurnal), m(hk(p.charts.daily)), m(note(esc(p.insight) + wd, `${p.days} days of hourly data`))];
"""

VIEWS["weather_now"] = r"""
const p = msg.payload;
const html = cards([
  card('Temperature (station mean)', fmtN(p.temperature, 1), '°C', p.hottest ? `Hottest ${esc(p.hottest.station)} ${p.hottest.temp}°C` : ''),
  card('Relative humidity', fmtN(p.humidity, 0), '%', ''),
  card('Wind (mean)', fmtN(p.windSpeed, 0), 'km/h', p.gustiest ? `Max gust ${p.gustiest.gust} km/h at ${esc(p.gustiest.station)}` : ''),
  card('Max hourly rainfall', fmtN(p.maxHourlyRain, 0), 'mm', 'Across 18 districts'),
]) + note(`<div style="margin-top:8px">${p.warnings.length ? badge('serious', 'In force: ' + p.warnings.join(', ')) : badge('good', 'No weather warnings in force')}</div>`, 'HKO · updated ' + fmtT(p.asOf));
return [m(html), m(hk(p.charts.trend))];
"""

VIEWS["ae_status"] = r"""
const p = msg.payload;
const lvl = s => s === 'Busier than usual' ? 'serious' : s === 'Quieter than usual' ? 'good' : s === 'Normal' ? 'neutral' : 'neutral';
const kpi = cards([
  card('Shortest wait now', fmtN(p.shortest.t45), 'min', esc(p.shortest.hospital)),
  card('Longest wait now', fmtN(p.longest.t45), 'min', esc(p.longest.hospital)),
  card('Average across A&E', fmtN(p.territoryMeanT45), 'min', `Typical for this hour: ${fmtN(p.territoryTypicalT45)} min`),
]) + note(`<div style="margin-top:8px">${badge(/All/.test(p.alert) ? 'good' : 'serious', p.alert)}</div>`,
          'Median wait for semi-urgent / non-urgent (triage 4–5) patients · HA update ' + fmtT(p.asOf));
const tbl = table([
  {h: 'Hospital', f: r => r.hospital},
  {h: 'Wait now (min)', num: true, f: r => fmtN(r.t45)},
  {h: 'Typical (min)', num: true, f: r => fmtN(r.typicalT45)},
  {h: 'vs typical', num: true, f: r => r.vsTypicalPct == null ? '–' : (r.vsTypicalPct > 0 ? '+' : '') + r.vsTypicalPct + '%'},
  {h: 'Status', html: true, f: r => badge(lvl(r.status), r.status)}], p.hospitals);
return [m(kpi), m(p.charts.byHospital), m(tbl)];
"""

VIEWS["ae_patterns"] = r"""
const p = msg.payload;
return [m(hk(p.charts.trend)), m(p.charts.diurnal), m(p.charts.weekday), m(p.charts.ranking), m(note(esc(p.insight)))];
"""

VIEWS["traffic_status"] = r"""
const p = msg.payload;
const lvl = p.status === 'Slower than usual' ? 'serious' : p.status === 'Faster than usual' ? 'good' : 'neutral';
const kpi = cards([
  card('Network mean speed', fmtN(p.meanSpeed, 1), 'km/h', `Typical: ${fmtN(p.typicalSpeed, 1)} km/h · ${badge(lvl, p.status)}`),
  card('Segments below 30 km/h', fmtN(p.pctBelow30, 1), '%', `Typical: ${fmtN(p.typicalPctBelow30, 1)}%`),
  card('Congested (red) routes', p.redRoutes, '', `of ${p.routes.length} monitored journeys`),
]) + note(`<div style="margin-top:8px">${badge(p.redRoutes ? 'serious' : 'good', p.alert)}</div>`, `${fmtN(p.validSegments)} road segments · ${fmtT(p.asOf)}`);
const colLvl = c => c === 'Red' ? 'critical' : c === 'Amber' ? 'warning' : c === 'Green' ? 'good' : 'neutral';
const tbl = table([
  {h: 'Journey', f: r => r.route}, {h: 'Now (min)', num: true, f: r => fmtN(r.minutes)},
  {h: 'Typical (min)', num: true, f: r => fmtN(r.typical, 1)},
  {h: 'Delay (min)', num: true, f: r => r.delayMin == null ? '–' : (r.delayMin > 0 ? '+' : '') + fmtN(r.delayMin, 1)},
  {h: 'TD status', html: true, f: r => badge(colLvl(r.colour), r.colour)}], p.routes.slice(0, 15));
return [m(kpi), m(p.charts.routeDelay), m(tbl)];
"""

VIEWS["traffic_patterns"] = r"""
const p = msg.payload;
return [m(p.charts.diurnal), m(p.charts.congestion), m(hk(p.charts.trend)), m(note(esc(p.insight)))];
"""

VIEWS["carpark_status"] = r"""
const p = msg.payload;
const kpi = cards([
  card('Free private-car spaces', fmtN(p.totalVacancy), '', `${p.districts.length} districts reporting`),
  card('Carparks full', p.fullCarparks, '', 'Vacancy = 0'),
]) + note(`<div style="margin-top:8px">${esc(p.insight)}</div>`, 'Updated ' + fmtT(p.asOf));
return [m(kpi), m(p.charts.district), m(hk(p.charts.trend)), m(p.charts.diurnal)];
"""

VIEWS["correlations"] = r"""
const p = msg.payload;
const labels = p.variables.map(v => v.label);
const lookup = {};
p.pairs.forEach(q => { lookup[q.a + '|' + q.b] = q; lookup[q.b + '|' + q.a] = q; });
const cell = (a, b) => {
    if (a === b) return `<td style="padding:6px;text-align:center;color:${C.muted}">—</td>`;
    const q = lookup[a + '|' + b], r = q && q.adjustedR;
    const fg = r != null && Math.abs(r) > 0.45 ? '#ffffff' : C.text;
    return `<td title="${esc(a)} ~ ${esc(b)}: adjusted r ${r ?? 'n/a'}, raw r ${q ? q.rawR ?? 'n/a' : 'n/a'}, n=${q ? q.n : 0}"
              style="padding:6px;text-align:center;background:${divColor(r)};color:${fg};border:2px solid ${C.surface};font-variant-numeric:tabular-nums">${r == null ? '·' : fmtN(r, 2)}</td>`;
};
const heat = `<div style="overflow-x:auto;${WRAP}"><table style="border-collapse:collapse;width:100%">
  <tr><th></th>${labels.map(l => `<th style="padding:4px;color:${C.text2};font-weight:500;font-size:11px">${esc(l)}</th>`).join('')}</tr>
  ${labels.map(a => `<tr><th style="text-align:right;padding:4px 8px;color:${C.text2};font-weight:500;font-size:11px;white-space:nowrap">${esc(a)}</th>${labels.map(b => cell(a, b)).join('')}</tr>`).join('')}
  </table>
  <div style="color:${C.text2};font-size:12px;margin-top:6px">
   <span style="display:inline-block;width:60px;height:10px;background:linear-gradient(90deg,${C.blue},${C.mid},${C.red});vertical-align:middle"></span>
   −1 negative · 0 none · +1 positive. Values are <b>time-of-day-adjusted</b> Pearson r on hourly data; “·” = not enough overlapping hours.</div></div>`;
const tbl = table([
  {h: 'Variable pair', f: q => q.a + ' ~ ' + q.b},
  {h: 'Raw r', num: true, f: q => fmtN(q.rawR, 2)},
  {h: 'Adjusted r', num: true, f: q => fmtN(q.adjustedR, 2)},
  {h: 'Hours (n)', num: true, f: q => fmtN(q.n)},
  {h: 'Strength', f: q => q.strength}], p.pairs.filter(q => q.adjustedR != null).slice(0, 10));
const ri = p.rainImpact;
const method = note(`<b>Method.</b> Every source is averaged per hour and aligned on the hour. <i>Raw r</i> compares the values directly, so it
  includes the shared daily rhythm (most city activity follows the clock). <i>Adjusted r</i> first subtracts each variable's
  average for that hour of day, so only deviations from the normal daily pattern are compared — a more honest measure of
  whether two phenomena are linked.<br><br><b>Rain → road speed:</b> ${esc(ri.note)} (${ri.rainyHours} rainy / ${ri.dryHours} dry hours matched).`);
return [m(heat), m(tbl),
        m(scatter(p.charts.scatterTempAqhi, 'Temperature (°C)', 'AQHI (general)', C.blue)),
        m(scatter(p.charts.scatterAqhiAe, 'AQHI (roadside)', 'A&E wait (min)', C.orange || '#d95926')),
        m(scatter(p.charts.scatterHumSpeed, 'Humidity (%)', 'Road speed (km/h)', '#199e70')),
        m(method)];
"""

VIEWS["data_health"] = r"""
const p = msg.payload;
const lvl = r => r.ageMin == null ? 'neutral' : r.collection === 'carpark_info' ? 'good' : r.ageMin <= 90 ? 'good' : r.ageMin <= 240 ? 'warning' : 'critical';
const tbl = table([
  {h: 'Collection', f: r => r.collection},
  {h: 'Documents', num: true, f: r => fmtN(r.documents)},
  {h: 'From archive', num: true, f: r => fmtN(r.archived)},
  {h: 'Covers (days)', num: true, f: r => fmtN(r.days, 1)},
  {h: 'Latest record', f: r => fmtT(r.last)},
  {h: 'Feed', html: true, f: r => badge(lvl(r), r.ageMin == null ? 'no data' : r.ageMin + ' min ago')}], p.collections);
return [m(tbl + note('', `${fmtN(p.totalDocuments)} documents in MongoDB database “smartcity”`))];
"""

# ------------------------------------------------------------------ page layout
# page -> list of groups; group = (name, width, [widgets]); widget = (source analysis, kind, opts)
# kind: html | line | bar | hbar
PAGES = [
    ("Overview", "dashboard", [
        ("Headline indicators", 12, [("overview", "html", {"h": 5})]),
        ("Current weather", 12, [("weather_now", "html", {"h": 5})]),
        ("Alerts & insights", 12, [("overview_alerts", "html", {"h": 7})]),
        ("Data collection health (MongoDB)", 12, [("data_health", "html", {"h": 7})]),
    ]),
    ("Air Quality", "cloud", [
        ("Health risk now", 12, [("aqhi_latest", "html", {"h": 4})]),
        ("AQHI by station", 6, [("aqhi_latest", "hbar", {"h": 12, "label": "Current AQHI", "ymin": 0, "ymax": 11, "one": True})]),
        ("Station table", 6, [("aqhi_latest", "html", {"h": 12})]),
        ("Last 7 days", 12, [("aqhi_patterns", "line", {"h": 6, "label": "Hourly AQHI (mean)", "xformat": "ddd HH:mm"})]),
        ("Typical day (28-day average)", 6, [("aqhi_patterns", "bar", {"h": 6, "label": "AQHI by hour of day"})]),
        ("Daily mean & peak", 6, [("aqhi_patterns", "line", {"h": 6, "label": "Daily AQHI", "xformat": "D/M"})]),
        ("Insight", 6, [("aqhi_patterns", "html", {"h": 2})]),
        ("Temperature, last 48 h", 6, [("weather_now", "line", {"h": 4, "label": "Station mean (°C)", "xformat": "ddd HH:mm"})]),
    ]),
    ("A&E Waiting", "local_hospital", [
        ("Right now", 12, [("ae_status", "html", {"h": 4})]),
        ("Now vs typical for this hour", 12, [("ae_status", "hbar", {"h": 10, "label": "Median wait, semi/non-urgent (min)"})]),
        ("All A&E departments", 12, [("ae_status", "html", {"h": 12})]),
        ("Last 7 days", 12, [("ae_patterns", "line", {"h": 6, "label": "Average wait across A&E (min)", "xformat": "ddd HH:mm"})]),
        ("Typical day", 6, [("ae_patterns", "bar", {"h": 6, "label": "Wait by hour of day (min)"})]),
        ("Day of week", 6, [("ae_patterns", "bar", {"h": 6, "label": "Wait by day of week (min)", "one": True})]),
        ("28-day hospital ranking", 6, [("ae_patterns", "hbar", {"h": 9, "label": "Average wait (min)", "one": True})]),
        ("Insight", 6, [("ae_patterns", "html", {"h": 2})]),
    ]),
    ("Mobility", "directions_car", [
        ("Road network now", 12, [("traffic_status", "html", {"h": 4})]),
        ("Journeys: now vs typical", 6, [("traffic_status", "hbar", {"h": 8, "label": "Journey time (min)"})]),
        ("Journey times", 6, [("traffic_status", "html", {"h": 8})]),
        ("Typical day: speed", 6, [("traffic_patterns", "bar", {"h": 6, "label": "Mean speed by hour (km/h)"})]),
        ("Typical day: congestion", 6, [("traffic_patterns", "bar", {"h": 6, "label": "% segments < 30 km/h"})]),
        ("Last 7 days", 12, [("traffic_patterns", "line", {"h": 5, "label": "Network speed & congestion", "xformat": "ddd HH:mm"})]),
        ("Traffic insight", 12, [("traffic_patterns", "html", {"h": 1})]),
        ("Parking now", 12, [("carpark_status", "html", {"h": 3})]),
        ("Free spaces by district", 6, [("carpark_status", "hbar", {"h": 9, "label": "Free private-car spaces", "one": True})]),
        ("Free spaces over time", 6, [("carpark_status", "line", {"h": 4, "label": "Total free spaces", "xformat": "ddd HH:mm"}),
                                      ("carpark_status", "bar", {"h": 5, "label": "Average free spaces by hour", "one": True})]),
    ]),
    ("Correlations", "insights", [
        ("Correlation matrix (time-of-day adjusted)", 12, [("correlations", "html", {"h": 8})]),
        ("Strongest relationships", 12, [("correlations", "html", {"h": 7})]),
        ("Temperature vs air quality", 6, [("correlations", "html", {"h": 7})]),
        ("Air quality vs A&E waiting", 6, [("correlations", "html", {"h": 7})]),
        ("Humidity vs road speed", 6, [("correlations", "html", {"h": 7})]),
        ("Method", 6, [("correlations", "html", {"h": 7})]),
    ]),
]

OVERVIEW = r"""
// Keep the latest result of every analysis, then (re)draw the headline cards and the alert list
const all = flow.get('latest') || {};
all[msg.topic] = msg.payload;
flow.set('latest', all);
const a = all.aqhi_latest, e = all.ae_status, t = all.traffic_status, c = all.carpark_status, w = all.weather_now;
const head = cards([
  card('Air quality (highest AQHI)', a ? a.worst.display : '…', '', a ? `${esc(a.worst.station)} · ${badge(AQHI_LEVEL[a.worst.band], a.worst.band)}` : ''),
  card('A&E average wait', e ? fmtN(e.territoryMeanT45) : '…', 'min', e ? `Typical now: ${fmtN(e.territoryTypicalT45)} min` : ''),
  card('Road network speed', t ? fmtN(t.meanSpeed, 1) : '…', 'km/h', t ? `Typical: ${fmtN(t.typicalSpeed, 1)} · ${badge(t.status === 'Slower than usual' ? 'serious' : 'neutral', t.status)}` : ''),
  card('Free parking spaces', c ? fmtN(c.totalVacancy) : '…', '', c ? `${c.fullCarparks} carparks full` : ''),
  card('Temperature', w ? fmtN(w.temperature, 1) : '…', '°C', w ? `Humidity ${fmtN(w.humidity)}%` : ''),
]);
const alertRow = (ok, txt, page) => `<li style="margin:4px 0">${badge(ok ? 'good' : 'serious', txt)} <span style="color:${C.muted}">· ${page}</span></li>`;
const items = [];
if (a) items.push(alertRow(a.worst.aqhi < 7, a.alert, 'Air Quality'));
if (e) items.push(alertRow(/All/.test(e.alert), e.alert, 'A&E'));
if (t) items.push(alertRow(!t.redRoutes, t.alert, 'Mobility'));
if (w) items.push(alertRow(!w.warnings.length, w.warnings.length ? 'Weather warnings: ' + w.warnings.join(', ') : 'No weather warnings in force', 'Weather'));
const ins = ['aqhi_patterns', 'ae_patterns', 'traffic_patterns'].filter(k => all[k]).map(k => `<li style="margin:4px 0">${esc(all[k].insight)}</li>`);
const c1 = all.correlations && all.correlations.top.find(q => !/AQHI \(general\) ~ AQHI \(roadside\)/.test(q.a + ' ~ ' + q.b));
if (c1) ins.push(`<li style="margin:4px 0">Strongest cross-domain link: <b>${esc(c1.a)} ~ ${esc(c1.b)}</b> (time-of-day-adjusted r = ${c1.adjustedR}).</li>`);
const alerts = `<div style="${WRAP}"><div style="color:${C.text2};font-weight:500">Alerts</div><ul style="margin:4px 0 10px;padding-left:18px;list-style:none">${items.join('')}</ul>
  <div style="color:${C.text2};font-weight:500">Insights from the collected data</div><ul style="margin:4px 0;padding-left:18px">${ins.join('')}</ul></div>`;
return [m(head), m(alerts)];
"""


# ------------------------------------------------------------------ node generation
def build_dashboard_tab(add, nid, ui_base_id):
    add({"id": DTAB, "type": "tab", "label": "Dashboards", "disabled": False,
         "info": "Receives every analysis result from the analytics bus and renders the dashboard pages at /ui."})

    # dashboard pages, groups
    tab_ids, groups = {}, []
    for order, (page, icon, glist) in enumerate(PAGES, start=1):
        tid = nid("ut")
        tab_ids[page] = tid
        add({"id": tid, "type": "ui_tab", "name": page, "icon": icon, "order": order, "disabled": False, "hidden": False})
        for gorder, (gname, width, widgets) in enumerate(glist, start=1):
            gid = nid("ug")
            add({"id": gid, "type": "ui_group", "name": gname, "tab": tid, "order": gorder, "disp": True,
                 "width": str(width), "collapse": False, "className": ""})
            for w in widgets:
                groups.append((gid, width, w))

    # create widgets, remember per-source output order
    outputs = {}   # source -> [widget ids]
    y_by_src = {}
    widget_y = 40
    for gid, gwidth, (src, kind, opts) in groups:
        wid = nid("uw")
        outputs.setdefault(src, []).append(wid)
        x = 1000
        if kind == "html":
            hid = "h_" + wid
            add({"id": wid, "type": "ui_template", "z": DTAB, "group": gid, "name": f"{src} html", "order": 0,
                 "width": str(gwidth), "height": str(opts.get("h", 4)), "format":
                 f'<div id="{hid}" style="width:100%"></div>\n<script>\n(function (scope) {{\n'
                 f'  scope.$watch("msg", function (m) {{\n    if (!m || m.payload === undefined) return;\n'
                 f'    setTimeout(function () {{ var el = document.getElementById("{hid}"); if (el) el.innerHTML = m.payload; }}, 0);\n'
                 f'  }});\n}})(scope);\n</script>',
                 "storeOutMessages": True, "fwdInMessages": False, "resendOnRefresh": True,
                 "templateScope": "local", "className": "", "x": x, "y": widget_y, "wires": [[]]})
        else:
            one = opts.get("one", False)
            add({"id": wid, "type": "ui_chart", "z": DTAB, "name": f"{src} {kind}", "group": gid, "order": 0,
                 "width": str(gwidth), "height": str(opts.get("h", 6)), "label": opts.get("label", ""),
                 "chartType": {"line": "line", "bar": "bar", "hbar": "horizontalBar"}[kind],
                 "legend": "false" if one else "true", "xformat": opts.get("xformat", "HH:mm"),
                 "interpolate": "linear", "nodata": "Waiting for data…", "dot": False,
                 "ymin": str(opts.get("ymin", "")), "ymax": str(opts.get("ymax", "")),
                 "removeOlder": "1", "removeOlderPoints": "", "removeOlderUnit": "604800", "cutout": 0,
                 "useOneColor": one, "useUTC": kind == "line",
                 "colors": SERIES, "outputs": 1, "useDifferentColor": False, "className": "",
                 "x": x, "y": widget_y, "wires": [[]]})
        widget_y += 40

    # router: link in -> switch(topic) -> view functions -> widgets
    sw_id = nid("sw")
    srcs = [s for s in outputs if s not in ("overview", "overview_alerts")]
    add({"id": DASH_IN, "type": "link in", "z": DTAB, "name": "dashboard-bus", "links": ["an4lysisbus0out1"], "x": 100, "y": 40,
         "wires": [[sw_id, ov_id := nid("fn")]]})
    view_ids = [nid("fn") for _ in srcs]
    add({"id": sw_id, "type": "switch", "z": DTAB, "name": "route by analysis", "property": "topic",
         "propertyType": "msg", "rules": [{"t": "eq", "v": s, "vt": "str"} for s in srcs], "checkall": "false",
         "repair": False, "outputs": len(srcs), "x": 300, "y": 40, "wires": [[v] for v in view_ids]})
    vy = 40
    for vid, src in zip(view_ids, srcs):
        add({"id": vid, "type": "function", "z": DTAB, "name": f"View: {src}", "func": (VIEW_LIB + VIEWS[src]).strip(),
             "outputs": len(outputs[src]), "timeout": 0, "noerr": 0, "initialize": "", "finalize": "", "libs": [],
             "x": 560, "y": vy, "wires": [[w] for w in outputs[src]]})
        vy += 60
    add({"id": ov_id, "type": "function", "z": DTAB, "name": "View: overview (all analyses)",
         "func": (VIEW_LIB + OVERVIEW).strip(), "outputs": 2, "timeout": 0, "noerr": 0, "initialize": "",
         "finalize": "", "libs": [], "x": 560, "y": vy,
         "wires": [outputs["overview"], outputs["overview_alerts"]]})
    return DASH_IN
