"""Builds Cyan_Reference_Generation.json: a ComfyUI workflow (UI format) plus the same graph in
API format (for queueing). Every image is made by the 'Cyan Image API' node (gpt-image-2.6)
from Clip 2 frames, so the characters and the flat match Clip 2.

    python3 build_generation_workflow.py            # writes both JSON files next to this script
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
MODEL, SIZE, QUALITY = "gpt-image-2.6-sunburst", "1920x1080", "high"

STYLE = ("Match the illustration style of the Clip 2 reference frames exactly: clean hand-drawn ink contour lines, "
         "smooth even colour with soft transparent watercolour shading, warm muted palette, smooth clean skin, "
         "crisp clean fabric, very subtle paper texture only. Clean and tidy: no grime, stains, mottling, blotches, "
         "splatter or torn-paper border; the picture fills the whole frame edge to edge. "
         "No text, no labels, no captions, no logos, no watermark, no signature, no star or sparkle marks.")

APOSE = ("Character turnaround reference sheet on a plain warm off-white background. Four full-body views side by side "
         "at exactly the same scale, feet on one shared ground line, evenly spaced: front view, three-quarter view, "
         "side profile view facing right, back view. Relaxed A-pose in every view: standing straight, arms straight "
         "and angled about 30 degrees away from the body, open relaxed hands, feet slightly apart, calm neutral "
         "expression. Even soft studio lighting, identical clothing and proportions in all four views. "
         "Clothing uses flat, even, clean colour fills with only soft simple shading: no watercolour blotches, "
         "no mottled or stained patches on trousers, jeans, hoodie or apron. ")

CLIP2 = "Cyan_Asset_Library/clip2/"
SRC = "Cyan_Asset_Library/refs_clean/"  # source frames cropped so their corner sparkle is not copied

# id: (title, prompt, [ref inputs: filename str or other asset id])
ASSETS = {
    "mei": ("01 Mei - A-pose turnaround",
            APOSE + "The character is Mei, the woman in the reference frames: a youthful 29-year-old Hong Kong woman, "
            "slim, average height, the same face, black hair tied in a low ponytail with a dark hair tie, a few loose "
            "strands at the temples, cream long-sleeved button-up blouse with the sleeves slightly rolled, grey straight "
            "trousers with a thin dark belt, simple dark flat shoes. " + STYLE,
            [CLIP2 + "t000.3.jpg", CLIP2 + "t009.6.jpg", CLIP2 + "t007.5.jpg"]),
    "kaho": ("02 Ka-ho - A-pose turnaround",
             APOSE + "The character is Ka-ho, the man with thin round glasses in references 1 and 2: a 31-year-old Hong "
             "Kong man, the same face, short black hair, thin round wire glasses, light stubble, navy pullover hoodie "
             "with white drawstrings over a white crew-neck t-shirt, dark blue-grey jeans, white canvas sneakers. "
             "He is about 10 cm taller than Mei. Draw him at the same scale, framing and style as the Mei turnaround "
             "sheet in reference 3, so the two sheets match. " + STYLE,
             [SRC + "scene09.jpg", SRC + "scene13.jpg", "mei"]),
    "volunteer": ("03 Community volunteer - A-pose turnaround (new design)",
                  APOSE + "The character is a friendly community-centre cooking volunteer: a Hong Kong woman in her "
                  "mid-forties, warm smile lines, shoulder-length black hair tucked behind her ears, mustard-yellow "
                  "bib apron over a light blue button shirt, navy trousers, comfortable black shoes. Draw her at the "
                  "same scale, framing and style as the Mei turnaround sheet in reference 1. " + STYLE,
                  ["mei", SRC + "scene14.jpg"]),
    "kitchen": ("04 Kitchen - overview (empty)",
                "Empty establishing view of exactly this kitchen from the Clip 2 reference frames, with no people. "
                "Wide eye-level view from the kitchen doorway that shows the whole small galley kitchen in one image, "
                "keeping every object where it is in the references: on the left wall a square wooden wall clock and "
                "a hook rail with a blue checked tea towel; wooden upper cabinets with round knobs; a stainless range "
                "hood above a two-burner gas hob with a pot; white square wall tiles and a rail with a ladle and "
                "spatulas; a narrow silver two-door fridge with its long handle on the LEFT edge of the door (door "
                "hinged on the right), a few magnets, notes and a calendar on the door, storage boxes and a steel pot "
                "on top; to the right of the fridge a wooden counter with a wire dish rack holding sauce jars, a "
                "wooden utensil pot, a cutting board and a cabbage; a stainless sink with a tall faucet, dish soap and "
                "a sponge; a window on the right overlooking lit Hong Kong housing towers at dusk. A clean, tidy, "
                "well-kept middle-class home in warm evening light. " + STYLE,
                [CLIP2 + "t000.3.jpg", CLIP2 + "t009.6.jpg", CLIP2 + "t003.5.jpg", CLIP2 + "t005.0.jpg"]),
    "living": ("05 Living and dining room - overview (empty), matches approved layout A",
               "Empty establishing view of the living and dining room of the apartment shown in the isometric layout "
               "in reference 3 (the approved floor plan), with no people. Keep exactly that layout: the kitchen is OPEN "
               "to the dining area, with no door and no doorway between them. Eye-level wide view standing near the "
               "front door and looking into the flat: on the left a compact beige fabric sofa with a mustard cushion "
               "against the wall, a tall floor lamp with a warm cream shade, a large monstera plant in a woven basket "
               "and a small wall shelf with books and a trailing plant; in the centre a small light-wood dining table "
               "for two with two wooden chairs, a cream table runner and a small potted plant; at the back a large "
               "window with sheer cream curtains looking out on lit Hong Kong housing towers at dusk; at the back right "
               "the open kitchen corner from reference 2, seen directly beyond the dining table: the silver two-door "
               "fridge with its handle on the left edge, the two-burner hob under the range hood, wooden cabinets, "
               "white wall tiles and the blue checked tea towel. Same light-wood flooring through both areas, warm "
               "evening light. A clean, tidy, comfortable middle-class home. " + STYLE,
               [SRC + "scene13.jpg", "kitchen", "Cyan_Asset_Library/approved/06_Flat_isometric_A.png"]),
}

ORDER = list(ASSETS)
nodes, links, groups, api = [], [], [], {}
nid, lid = [0], [0]
api_node_of = {}
load_cache = {}
COL_W, ROW_H = 1900, 760


def new_id(c):
    c[0] += 1
    return c[0]


def add_load(fname, pos):
    i = new_id(nid)
    nodes.append({"id": i, "type": "LoadImage", "pos": pos, "size": [300, 320], "flags": {}, "order": i, "mode": 0,
                  "title": fname.split("/")[-1], "inputs": [],
                  "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": []},
                              {"name": "MASK", "type": "MASK", "links": []}],
                  "properties": {"Node name for S&R": "LoadImage"}, "widgets_values": [fname, "image"]})
    api[str(i)] = {"class_type": "LoadImage", "inputs": {"image": fname}, "_meta": {"title": fname}}
    return i


def node(i):
    return next(n for n in nodes if n["id"] == i)


def link(src, src_slot, dst, dst_slot, typ="IMAGE"):
    l = new_id(lid)
    links.append([l, src, src_slot, dst, dst_slot, typ])
    node(src)["outputs"][src_slot]["links"].append(l)
    node(dst)["inputs"][dst_slot]["link"] = l


for row, key in enumerate(ORDER):
    title, prompt, refs = ASSETS[key]
    y = row * ROW_H
    gen = new_id(nid)
    gen_x = 700
    nodes.append({"id": gen, "type": "CyanImageAPI", "pos": [gen_x, y + 60], "size": [520, 600], "flags": {},
                  "order": 100 + row, "mode": 0, "title": "Generate · " + title,
                  "color": "#223", "bgcolor": "#335",
                  "inputs": [{"name": f"ref_{k}", "type": "IMAGE", "link": None} for k in range(1, 5)],
                  "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": []}],
                  "properties": {"Node name for S&R": "CyanImageAPI"},
                  "widgets_values": [prompt, MODEL, SIZE, QUALITY, 1000 + row, "fixed"]})
    api_inputs = {"prompt": prompt, "model": MODEL, "size": SIZE, "quality": QUALITY, "seed": 1000 + row}
    for k, r in enumerate(refs):
        if r in api_node_of:                       # output of an earlier asset
            src = api_node_of[r]
        else:
            src = add_load(r, [0 if k % 2 == 0 else 330, y + 60 + (k // 2) * 340])
        link(src, 0, gen, k)
        api_inputs[f"ref_{k + 1}"] = [str(src), 0]
    api[str(gen)] = {"class_type": "CyanImageAPI", "inputs": api_inputs, "_meta": {"title": title}}
    save = new_id(nid)
    nodes.append({"id": save, "type": "SaveImage", "pos": [gen_x + 560, y + 60], "size": [1200, 680], "flags": {},
                  "order": 200 + row, "mode": 0, "title": "Result · " + title,
                  "inputs": [{"name": "images", "type": "IMAGE", "link": None}], "outputs": [],
                  "properties": {"Node name for S&R": "SaveImage"},
                  "widgets_values": [f"Cyan_Refs/{key}"]})
    link(gen, 0, save, 0)
    api[str(save)] = {"class_type": "SaveImage", "inputs": {"filename_prefix": f"Cyan_Refs/{key}",
                                                            "images": [str(gen), 0]}, "_meta": {"title": title}}
    api_node_of[key] = gen
    groups.append({"title": title, "bounding": [-30, y, 3000, ROW_H - 40], "color": "#3f789e", "font_size": 28})

wf = {"last_node_id": nid[0], "last_link_id": lid[0], "nodes": nodes, "links": links, "groups": groups,
      "config": {}, "extra": {"ds": {"scale": 0.35, "offset": [100, 100]}}, "version": 0.4}
(HERE / "Cyan_Reference_Generation.json").write_text(json.dumps(wf, indent=1))
(HERE / "Cyan_Reference_Generation.api.json").write_text(json.dumps(api, indent=1))
print("nodes", len(nodes), "links", len(links))
