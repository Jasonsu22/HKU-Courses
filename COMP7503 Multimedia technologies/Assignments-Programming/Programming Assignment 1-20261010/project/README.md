# COMP7503 Programming Assignment – Smart City (Node-RED + MongoDB)

## Run
```bash
docker compose up -d --build
```
- Node-RED editor: http://localhost:1880
- Dashboard: http://localhost:1880/ui
- MongoDB: `mongodb://localhost:27017` (database `smartcity`; inside Docker the host is `mongo`)

`nodered/Dockerfile` extends `nodered/node-red:latest` and preinstalls
`node-red-contrib-mongodb3@2.0.1` and `node-red-dashboard@3.6.6`.

## Data collected (database `smartcity`)
| Collection | Source (data.gov.hk) | Poll | Key |
|---|---|---|---|
| `Weather Report` | HKO current weather report (`rhrread`) | 5 min | updateTime |
| `hko_regional` | HKO per-station temperature / humidity / wind CSVs (merged) | 10 min | station + time |
| `weather_warnings` | HKO warning summary (`warnsum`) | 10 min, stored on change | observedAt |
| `aqhi` | EPD past-24h AQHI, all stations | 30 min | station + time |
| `ae_waiting` | Hospital Authority A&E waiting time v2 | 10 min | hospital + updateTime |
| `journey_time` | TD journey time indicators | 10 min | from + to + captureTime |
| `traffic_speed` | TD average speed, strategic road network | 15 min | snapshotTime |
| `carpark_vacancy` | TD/data.gov.hk carpark vacancy (private car) | 15 min | 15-min slot |
| `carpark_info` | Carpark static info | daily | park_Id |

All writes are `bulkWrite` upserts on the key above, so re-polling never creates duplicates.

## Historical backfill
The live feeds only start on 18 Nov 2026, so earlier data is loaded from the
[data.gov.hk Historical Archive](https://data.gov.hk/en/help/api-spec#historicalAPI):
```bash
uv run scripts/backfill_archive.py --start 20261020 --end 20261117
```
It writes with the same schema as the Node-RED collectors, tagged `source: "archive"`.
Archive coverage: AQHI, A&E and HKO regional weather are continuous from 20 Oct;
journey time ends 31 Oct and road speed ends 5 Nov (gaps until live collection starts);
carpark vacancy and HKO rainfall are not archived (live only).

## Regenerating the collection flow
`python3 scripts/build_flows.py` rebuilds `nodered/data/flows.json` (sample HKO tab + Data Collection tab),
then `docker restart comp7503-nodered`. Once flows are edited in the editor, export from the editor instead.

## Analysis tab
`scripts/analyses.py` defines 8 analyses (MongoDB aggregation pipelines + JavaScript), run every 15–30 min.
A shared query runner (`link call` → `run-queries`) executes each analysis's pipelines; results go to the
**analytics bus**, which stores the latest result per analysis in the `analytics` collection (`_id` = name)
and feeds the dashboards.

| Analysis | Use case | Output |
|---|---|---|
| `aqhi_latest` | UC1 | AQHI per station, health-risk band, alert |
| `aqhi_patterns` | UC1 | 7-day trend, hour-of-day profile (general vs roadside), daily mean/max |
| `ae_status` | UC2 | Current wait per hospital vs typical for this hour, busier-than-usual alert |
| `ae_patterns` | UC2 | 7-day trend, hour-of-day and day-of-week profile, 28-day hospital ranking |
| `traffic_status` | UC3 | Network speed vs typical (hour × weekday/weekend), route delays, red routes |
| `traffic_patterns` | UC3 | Weekday vs weekend speed / congestion by hour |
| `carpark_status` | UC3 | Free spaces by district (joined with `carpark_info`), trend, hour profile |
| `correlations` | All | Hourly Pearson r between 8 variables, raw and time-of-day-adjusted |

## Dashboards (http://localhost:1880/ui)
`scripts/dashboards.py` builds the **Dashboards** flow tab: a link-in on the analytics bus routes each result
(switch on `msg.topic`) to a view function that formats it for the widgets.

| Page | Shows |
|---|---|
| Overview | Headline KPIs, current weather & warnings, alerts, key insights, data-collection health |
| Air Quality (UC1) | AQHI by station with health-risk band, 7-day trend, typical day, daily mean/peak, temperature |
| A&E Waiting (UC2) | Wait now vs typical per hospital, 7-day trend, hour-of-day and day-of-week profile, 28-day ranking |
| Mobility (UC3) | Network speed vs typical, journey delays, weekday/weekend profiles, carpark vacancy by district |
| Correlations | Time-of-day-adjusted correlation matrix, raw vs adjusted r table, scatter plots, method note |

Charts use node-red-dashboard `ui_chart` (hover tooltips); tables, KPI cards, heatmap and scatter plots are
HTML/SVG rendered by `ui_template`. Time axes are shown in Hong Kong time on any viewer's computer.
