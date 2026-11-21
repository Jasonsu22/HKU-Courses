"""Builds Cyan_Start_Frames.json: a ComfyUI workflow that draws the first frame of shots 1, 3, 4 and 5
from the APPROVED reference images (character A-poses, kitchen, living room, flat layout A).
Each frame is then animated with MiniMax-H3 (see ../../minimax/shots.json, *_final entries).

    python3 build_startframes_workflow.py
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
MODEL, SIZE, QUALITY = "gpt-image-2.6-sunburst", "1920x1080", "high"
A = "Cyan_Asset_Library/approved/"
CLIP2 = "Cyan_Asset_Library/clip2/"
CLEAN = "Cyan_Asset_Library/refs_clean/"

STYLE = ("Draw it in exactly the illustration style of the approved references and Clip 2: clean hand-drawn ink "
         "contour lines, smooth even colour with soft transparent watercolour shading, warm muted palette, smooth "
         "clean skin, clean even clothing colour, very subtle paper texture only. Clean and tidy: no grime, stains, "
         "mottling, blotches or splatter, no torn-paper border; the picture fills the whole 16:9 frame edge to edge. "
         "A single film frame: no text, no readable writing, no captions, no logos, no watermark, no signature, "
         "no star or sparkle marks.")

MEI = ("Mei is exactly the woman on the character sheet in reference 1: same face, black hair in a low ponytail, "
       "cream long-sleeved button blouse with rolled sleeves, grey trousers with a thin dark belt. She is right-handed "
       "and holds only one phone when a phone is in the scene. ")

FRAMES = {
    "shot01": ("Shot 1 start frame - MTR ride home",
               MEI + "6:40 pm in a crowded Hong Kong MTR carriage, heading home to Kwun Tong. Follow the composition "
               "of reference 2: medium shot, Mei standing in the centre-right of frame, canvas tote bag on her left "
               "shoulder, her left hand gripping the yellow vertical pole, her right hand holding one smartphone at "
               "chest height, looking down at it, tired after work. The phone screen shows a grid of small colourful "
               "food pictures, no readable text. Behind her: blue overhead grab handles, other yellow poles, a few "
               "understated commuters looking at their own phones, and carriage windows with blurred dusk city lights. "
               + STYLE,
               [A + "01_Mei_Apose.png", CLEAN + "scene01.jpg", CLIP2 + "t007.5.jpg"]),
    "shot03": ("Shot 3 start frame - food goes in the bin",
               MEI + "Late evening, in exactly the kitchen of reference 2, standing at the wooden counter beside the "
               "sink with the window and housing towers behind. In her left hand she holds one of the flat sealed "
               "clear plastic produce bags of spinach from reference 3, now wilted, darker and slightly yellowing; "
               "in her right hand a small unopened white yoghurt pot. In front of her on the floor stands a small "
               "cream pedal bin with its lid open. She looks down at the food with a quiet, disappointed expression. "
               "Medium shot at chest height so her face, both hands, the spinach, the yoghurt and the open bin are "
               "all clearly visible. " + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", CLIP2 + "t009.6.jpg"]),
    "shot04": ("Shot 4 start frame - list, recipe book, no one knows the fridge",
               "No people. Dusk in exactly the living and dining room of reference 1, in the flat of layout "
               "reference 2. Close, slightly high view of the light-wood dining table for two: on the cream table "
               "runner next to the small potted plant lie a handwritten shopping list (abstract pen strokes only, no "
               "readable words) with a pen, and an open recipe book showing painted pictures of dishes. Beyond the "
               "table, slightly out of focus, the large window with sheer cream curtains and lit housing towers, and "
               "on the right the open kitchen corner with the closed silver fridge from reference 3. Warm lamp light. "
               + STYLE,
               [A + "05_Living_dining_overview.png", A + "06_Flat_isometric_A.png", A + "04_Kitchen_overview.png"]),
    "shot05": ("Shot 5 start frame - Mei photographs her shopping",
               MEI + "Evening, in exactly the kitchen of reference 2. Mei stands at the wooden counter beside the "
               "sink, facing the counter. Laid out neatly in a row on the counter directly in front of her: a carton "
               "of eggs, one flat sealed clear plastic produce bag of fresh spinach exactly like the bags in "
               "reference 3, three tomatoes, a small tray of chicken, a carton of soy milk and a folded paper "
               "receipt; an empty canvas tote bag beside them. She leans slightly over the groceries and holds one "
               "smartphone flat in her right hand directly above them, camera lens pointing down at the food, her "
               "eyes on the phone screen. Side three-quarter view from the left at chest height, so her face, the "
               "phone and every grocery item are clearly visible below the phone. "
               + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", CLIP2 + "t009.6.jpg"]),
    "shot02": ("Shot 2 start frame - Mei opens the fridge (colour-matched redo)",
               MEI + "Evening, just home, in exactly the kitchen of reference 2, with the same bright warm colours "
               "and lighting as reference 2. Follow the composition of reference 3: Mei stands on the left in "
               "profile facing right, her right hand reaching for the long handle on the LEFT edge of the closed "
               "silver fridge door (the door is hinged on its right side); magnets, notes and a calendar on the "
               "door; the wooden counter with the dish rack, the sink and the window with lit housing towers on "
               "the right. On the counter, two identical flat sealed clear plastic produce bags of fresh spinach "
               "lie side by side, like reference 3's later frame. Medium-wide shot. " + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", CLIP2 + "t000.3.jpg", CLIP2 + "t009.6.jpg"]),
}


def build(frames, name, seed_base):
    nodes, links, groups, api = [], [], [], {}
    counter = {"n": 0, "l": 0}
    ROW_H = 760


    def nid(k):
        counter[k] += 1
        return counter[k]


    def node(i):
        return next(n for n in nodes if n["id"] == i)


    def link(src, dst, slot):
        l = nid("l")
        links.append([l, src, 0, dst, slot, "IMAGE"])
        node(src)["outputs"][0]["links"].append(l)
        node(dst)["inputs"][slot]["link"] = l


    loaded = {}
    for row, (key, (title, prompt, refs)) in enumerate(frames.items()):
        y = row * ROW_H
        gen = nid("n")
        nodes.append({"id": gen, "type": "CyanImageAPI", "pos": [700, y + 60], "size": [520, 600], "flags": {},
                      "order": 100 + row, "mode": 0, "title": "Generate · " + title, "color": "#223", "bgcolor": "#335",
                      "inputs": [{"name": f"ref_{k}", "type": "IMAGE", "link": None} for k in range(1, 5)],
                      "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": []}],
                      "properties": {"Node name for S&R": "CyanImageAPI"},
                      "widgets_values": [prompt, MODEL, SIZE, QUALITY, seed_base + row, "fixed"]})
        api_in = {"prompt": prompt, "model": MODEL, "size": SIZE, "quality": QUALITY, "seed": seed_base + row}
        for k, r in enumerate(refs):
            src = nid("n")
            nodes.append({"id": src, "type": "LoadImage", "pos": [0 if k % 2 == 0 else 330, y + 60 + (k // 2) * 340],
                          "size": [300, 320], "flags": {}, "order": src, "mode": 0, "title": r.split("/")[-1],
                          "inputs": [], "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": []},
                                                    {"name": "MASK", "type": "MASK", "links": []}],
                          "properties": {"Node name for S&R": "LoadImage"}, "widgets_values": [r, "image"]})
            api[str(src)] = {"class_type": "LoadImage", "inputs": {"image": r}}
            link(src, gen, k)
            api_in[f"ref_{k + 1}"] = [str(src), 0]
        api[str(gen)] = {"class_type": "CyanImageAPI", "inputs": api_in}
        save = nid("n")
        nodes.append({"id": save, "type": "SaveImage", "pos": [1260, y + 60], "size": [1200, 680], "flags": {},
                      "order": 200 + row, "mode": 0, "title": "Start frame · " + title,
                      "inputs": [{"name": "images", "type": "IMAGE", "link": None}], "outputs": [],
                      "properties": {"Node name for S&R": "SaveImage"}, "widgets_values": [f"Cyan_StartFrames/{key}"]})
        link(gen, save, 0)
        api[str(save)] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Cyan_StartFrames/{key}",
                                                                "images": [str(gen), 0]}}
        groups.append({"title": title, "bounding": [-30, y, 3000, ROW_H - 40], "color": "#3f789e", "font_size": 28})

    wf = {"last_node_id": counter["n"], "last_link_id": counter["l"], "nodes": nodes, "links": links,
          "groups": groups, "config": {}, "extra": {"ds": {"scale": 0.35, "offset": [100, 100]}}, "version": 0.4}
    (HERE / f"{name}.json").write_text(json.dumps(wf, indent=1))
    (HERE / f"{name}.api.json").write_text(json.dumps(api, indent=1))
    print("nodes", len(nodes), "links", len(links))


if __name__ == "__main__":
    build(FRAMES, "Cyan_Start_Frames", 2000)
