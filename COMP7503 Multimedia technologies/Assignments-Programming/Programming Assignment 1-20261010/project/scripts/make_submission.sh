#!/usr/bin/env bash
# Build the Moodle submission zip:
#   flows.json                 exported Node-RED flows (from the running editor)
#   docker-compose.yml         Docker description of the environment
#   nodered/Dockerfile         Node-RED image with the required palette nodes
#   nodered/data/flows.json    same flows, so `docker compose up` starts with them loaded
#   scripts/                   flow builder, analyses, dashboards, archive backfill
#   README.md                  how to run
#   *.pdf                      project report (put the exported PDF in report/ first)
#
# Usage (from the project folder, stack running):  bash scripts/make_submission.sh [zip-name]
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="${1:-COMP7503_Programming_Assignment}"
OUT="$PWD/submission"
STAGE="$OUT/$NAME"
rm -rf "$STAGE" "$OUT/$NAME.zip"
mkdir -p "$STAGE/nodered/data" "$STAGE/scripts"

# 1. export flows from the running Node-RED (same as Menu > Export > All flows)
curl -sf -H "Node-RED-API-Version: v1" http://localhost:1880/flows \
  | python3 -c 'import json,sys; json.dump(json.load(sys.stdin), sys.stdout, indent=4)' > "$STAGE/flows.json"
cp "$STAGE/flows.json" "$STAGE/nodered/data/flows.json"

# 2. Docker description + code + docs
cp docker-compose.yml README.md "$STAGE/"
cp nodered/Dockerfile "$STAGE/nodered/"
cp scripts/*.py scripts/make_submission.sh "$STAGE/scripts/"

# 3. report
if compgen -G "report/*.pdf" > /dev/null; then
  cp report/*.pdf "$STAGE/"
else
  echo "WARNING: no report PDF in report/ - export the report to PDF and re-run." >&2
fi

(cd "$OUT" && zip -qr "$NAME.zip" "$NAME" -x '*.DS_Store' '*/__pycache__/*')
echo "Built $OUT/$NAME.zip"
unzip -l "$OUT/$NAME.zip"
