"""Generate one Household Inventory shot with the MiniMax (Hailuo) image-to-video API.

Your key is read from the MINIMAX_API_KEY environment variable or from ~/.config/minimax/api_key.
It is never printed.

    python3 generate_clip.py shot02
    python3 generate_clip.py shot02 --model MiniMax-Hailuo-02 --duration 10 --resolution 768P
    MINIMAX_HOST=https://api.minimaxi.com python3 generate_clip.py shot02   # mainland-China accounts

Shots are defined in shots.json (start frame + prompt). Output: clips/<shot>.mp4
"""
import argparse, base64, json, os, pathlib, sys, time, urllib.request, urllib.error

HERE = pathlib.Path(__file__).resolve().parent
HOST = os.environ.get("MINIMAX_HOST", "https://api.minimax.io").rstrip("/")


def api_key():
    k = os.environ.get("MINIMAX_API_KEY")
    if not k:
        p = pathlib.Path.home() / ".config/minimax/api_key"
        if p.exists():
            k = p.read_text().strip()
    if not k:
        sys.exit("No key found. Set MINIMAX_API_KEY or save it in ~/.config/minimax/api_key")
    return k


def call(method, path, body=None):
    req = urllib.request.Request(HOST + path, method=method,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {api_key()}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:400]}")


def main():
    global HOST
    ap = argparse.ArgumentParser()
    ap.add_argument("shot")
    ap.add_argument("--model", default="MiniMax-Hailuo-02")
    ap.add_argument("--duration", type=int, default=10)
    ap.add_argument("--resolution", default="768P")
    ap.add_argument("--api", default="v1", help="v1 for Hailuo-02/2.3, v2 for MiniMax-H3")
    a = ap.parse_args()

    shot = json.loads((HERE / "shots.json").read_text())[a.shot]
    HOST = os.environ.get("MINIMAX_HOST", shot.get("host", HOST)).rstrip("/")
    img = HERE / shot["start_frame"]
    data_url = "data:image/jpeg;base64," + base64.b64encode(img.read_bytes()).decode()

    if a.api == "v2":
        body = {"model": a.model, "duration": a.duration, "resolution": a.resolution, "ratio": "adaptive",
                "content": [{"type": "text", "text": shot["prompt"]},
                            {"type": "image_url", "image_url": {"url": data_url}, "role": "first_frame"}]}
        if shot.get("reference_images"):
            body["ratio"] = "16:9"
            body["content"] = [{"type": "text", "text": shot["prompt"]}]
            for reference in shot["reference_images"]:
                encoded = base64.b64encode((HERE / reference).read_bytes()).decode()
                body["content"].append({"type": "image_url", "image_url": {
                    "url": "data:image/jpeg;base64," + encoded}, "role": "reference_image"})
    else:
        body = {"model": a.model, "prompt": shot["prompt"], "first_frame_image": data_url,
                "duration": a.duration, "resolution": a.resolution, "prompt_optimizer": False}
    r = call("POST", f"/{a.api}/video_generation", body)
    if a.api == "v2": print("  submit response:", json.dumps({k: v for k, v in r.items()})[:400])
    if r.get("base_resp", {}).get("status_code", 0) != 0 or "task_id" not in r:
        sys.exit(f"Submit failed: {r.get('base_resp')}")
    task = r["task_id"]
    (HERE / "clips").mkdir(exist_ok=True)
    (HERE / "clips" / f"{a.shot}.task.json").write_text(json.dumps({
        "task_id": task, "shot": a.shot, "model": a.model,
        "duration": a.duration, "resolution": a.resolution, "api": a.api, "host": HOST,
    }, indent=2) + "\n")
    print(f"Submitted {a.shot} ({a.model}, {a.duration}s, {a.resolution}) task {task}")

    if a.api == "v2":
        import subprocess
        subprocess.run([sys.executable, str(HERE / "fetch_v2.py"), str(task),
                        str(HERE / "clips" / f"{a.shot}.mp4")], check=True,
                       env={**os.environ, "MINIMAX_HOST": HOST})
        return

    while True:
        time.sleep(10)
        q = call("GET", f"/{a.api}/query/video_generation?task_id={task}")
        st = q.get("status")
        print("  status:", st, flush=True)
        if st is None: print("  raw:", json.dumps(q)[:400])
        if st == "Success":
            break
        if st in ("Fail", "Failed"):
            sys.exit(f"Generation failed: {q.get('base_resp')}")

    f = call("GET", f"/v1/files/retrieve?file_id={q['file_id']}")
    url = f["file"]["download_url"]
    out = HERE / "clips" / f"{a.shot}.mp4"
    out.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(url, out)
    print("Saved", out)


if __name__ == "__main__":
    main()
