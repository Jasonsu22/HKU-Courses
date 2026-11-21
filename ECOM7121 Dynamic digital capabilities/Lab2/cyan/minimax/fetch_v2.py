"""Poll a MiniMax v2 (H3) task and download the video.  python3 fetch_v2.py <task_id> <out.mp4>"""
import json, sys, time, urllib.request, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from generate_clip import call
task, out = sys.argv[1], sys.argv[2]
def find_url(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and v.startswith("http") and ("url" in k or "video" in k): return v
            u = find_url(v)
            if u: return u
    if isinstance(o, list):
        for x in o:
            u = find_url(x)
            if u: return u
for i in range(120):
    q = call("GET", f"/v2/query/video_generation?task_ids={task}&page_size=100")
    items = q.get("items") or [q]
    it = next((item for item in items if str(item.get("id", item.get("task_id"))) == task), None)
    if it is None:
        print("  waiting for task to appear:", task, flush=True)
        time.sleep(10)
        continue
    st = it.get("status")
    print("  status:", st, flush=True)
    if st in ("succeeded", "success", "Success", "completed"):
        url = find_url(it)
        if not url and it.get("file_id"):
            url = call("GET", f"/v1/files/retrieve?file_id={it['file_id']}")["file"]["download_url"]
        if not url: sys.exit("no url in: " + json.dumps(it)[:600])
        urllib.request.urlretrieve(url, out); print("Saved", out); break
    if st in ("failed", "Fail", "Failed", "canceled"): sys.exit("failed: " + json.dumps(it)[:600])
    time.sleep(10)
