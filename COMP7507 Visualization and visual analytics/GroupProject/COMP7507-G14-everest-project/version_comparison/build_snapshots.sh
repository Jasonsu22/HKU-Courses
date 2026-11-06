#!/bin/zsh
# Rebuilds v1_before (baseline commit) and v2_after (current working app), adding the difference banners.
set -e
cd "$(dirname "$0")"
PROJECT="$(cd .. && pwd)"
BASE=8e6b16f
rm -rf v1_before v2_after; mkdir v1_before v2_after
TMP=$(mktemp -d)
(cd "$PROJECT" && git archive "$BASE" -- everest-app) | tar -x -C "$TMP"
for d in css data js vendor index.html; do cp -R "$TMP/everest-app/$d" v1_before/; done
for d in css data js vendor index.html; do cp -R "$PROJECT/everest-app/$d" v2_after/; done
rm -rf "$TMP"
rm -f v1_before/data/*.json v2_after/data/*.json
inject() { # folder side
  python3 - "$1" "$2" <<'PY'
import sys
folder, side = sys.argv[1], sys.argv[2]
p = f"{folder}/index.html"
s = open(p, encoding="utf8").read()
tag = f'<script>window.SNAPSHOT_SIDE="{side}";</script>\n<script src="../changes_data.js"></script>\n<script src="../client.js"></script>\n</body>'
s = s.replace("</body>", tag)
open(p, "w", encoding="utf8").write(s)
PY
}
inject v1_before before
inject v2_after after
du -sh v1_before v2_after
