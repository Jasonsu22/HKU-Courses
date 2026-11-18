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
| `weather_warnings` | HKO warning summary (`warnsum`) | 10 min, stored on change | observedAt |
| `aqhi` | EPD past-24h AQHI, all stations | 30 min | station + time |
| `ae_waiting` | Hospital Authority A&E waiting time v2 | 10 min | hospital + updateTime |
| `journey_time` | TD journey time indicators | 10 min | from + to + captureTime |
| `traffic_speed` | TD average speed, strategic road network | 15 min | snapshotTime |
| `carpark_vacancy` | TD/data.gov.hk carpark vacancy (private car) | 15 min | 15-min slot |
| `carpark_info` | Carpark static info | daily | park_Id |

All writes are `bulkWrite` upserts on the key above, so re-polling never creates duplicates.

## Regenerating the collection flow
`python3 scripts/build_flows.py` rebuilds `nodered/data/flows.json` (sample HKO tab + Data Collection tab),
then `docker restart comp7503-nodered`. Once flows are edited in the editor, export from the editor instead.
