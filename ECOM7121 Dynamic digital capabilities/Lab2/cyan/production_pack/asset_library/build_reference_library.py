"""Import existing production references and save a visible ComfyUI library workflow."""
import json
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
PACK = HERE.parent
INPUT = pathlib.Path.home() / "ComfyUI-Shared/input"
WORKFLOWS = pathlib.Path.home() / "ComfyUI-Installs/ComfyUI/ComfyUI/user/default/workflows"


def main():
    INPUT.mkdir(parents=True, exist_ok=True)
    WORKFLOWS.mkdir(parents=True, exist_ok=True)
    nodes = []
    groups = []
    categories = [
        ("Characters - existing identity references", [
            PACK / "style_refs/ref_mei_scene1.jpg",
            PACK / "style_refs/ref_mei_scene6.jpg",
            PACK / "scene_refs/scene09.jpg",
            PACK / "scene_refs/scene13.jpg",
            PACK / "scene_refs/scene14.jpg",
        ]),
        ("Kitchen - Clip 2 baseline", [
            PACK / f"scene_refs/scene{i:02}.jpg" for i in [2, 3, 5, 6, 7, 10, 11, 12]
        ] + [PACK / "style_refs/ref_kitchen_scene7.jpg"]),
        ("Living and dining - spatial relationships need approval", [
            PACK / f"scene_refs/scene{i:02}.jpg" for i in [4, 8, 15, 17]
        ]),
        ("MTR and community classroom", [
            PACK / "scene_refs/scene01.jpg",
            PACK / "scene_refs/scene14.jpg",
        ]),
    ]
    y = 240
    for title, files in categories:
        rows = (len(files) + 3) // 4
        groups.append({"title": title, "bounding": [-30, y - 65, 2000, rows * 390 + 70],
                       "color": "#4c8c80", "font_size": 24, "flags": {}})
        for index, source in enumerate(files):
            name = "Cyan_source__" + source.parent.name + "__" + source.name
            shutil.copy2(source, INPUT / name)
            nodes.append({
                "id": len(nodes) + 1, "type": "LoadImage",
                "pos": [(index % 4) * 490, y + (index // 4) * 390],
                "size": [450, 340], "flags": {}, "order": len(nodes), "mode": 0,
                "inputs": [], "outputs": [
                    {"name": "IMAGE", "type": "IMAGE", "links": None, "slot_index": 0},
                    {"name": "MASK", "type": "MASK", "links": None, "slot_index": 1},
                ],
                "title": source.stem + " | ORIGINAL SOURCE",
                "properties": {"Node name for S&R": "LoadImage"},
                "widgets_values": [name, "image"],
            })
        y += rows * 390 + 170
    nodes.append({
        "id": len(nodes) + 1, "type": "Note", "pos": [0, 0], "size": [1850, 150],
        "flags": {}, "order": len(nodes), "mode": 0, "properties": {},
        "title": "CYAN ASSET LIBRARY - sources and original shot prompts",
        "widgets_values": [
            "Existing production_pack references. Target generation node: OpenAI GPT Image 2.6. "
            "Warm clean Clip 2 illustration style. Character identity + A-pose sheets, environment "
            "concepts + coherent plan/four wall views. Provider API compatibility is unverified. "
            "Original source overlays remain in these originals. Newly generated artwork should "
            "omit decorative stars and logos. See ASSET_BRIEF.md for confirmed details and gaps."
        ],
    })
    project = PACK.parent
    shots = json.loads((project / "minimax/shots.json").read_text())
    shot_names = ["shot01_pack_h3", "shot02_h3b", "shot03_pack_h3", "shot04_pack_h3", "shot05_pack_h3"]
    groups.append({"title": "Clips 1-5 | ORIGINAL prompts from minimax/shots.json",
                   "bounding": [2080, -65, 1050, 3600], "color": "#826b40",
                   "font_size": 24, "flags": {}})
    for index, name in enumerate(shot_names):
        shot = shots[name]
        nodes.append({
            "id": len(nodes) + 1, "type": "Note", "pos": [2110, index * 650],
            "size": [980, 610], "flags": {}, "order": len(nodes), "mode": 0,
            "properties": {}, "title": name + " | ORIGINAL VIDEO PROMPT",
            "widgets_values": ["Source: minimax/shots.json\nStart frame: " + shot["start_frame"]
                               + "\nReferences: " + ", ".join(shot.get("reference_images", []))
                               + "\n\n" + shot["prompt"]],
        })
    nodes.append({
        "id": len(nodes) + 1, "type": "Note", "pos": [2110, 3300],
        "size": [980, 540], "flags": {}, "order": len(nodes), "mode": 0,
        "properties": {}, "title": "项目说明 / Scripts and review status",
        "widgets_values": [
            "这是新整理的参考图与提示词资源库。此前的 ComfyUI 工作流尚未找到。\n"
            "Clip 2 原始提示词见上方 shot02_h3b。\n"
            "实际脚本目录\n" + str(project / "minimax") + "\n\n"
            "shots.json — 每个镜头的参考图路径与完整提示词\n"
            "generate_clip.py — 读取镜头配置，提交 MiniMax 请求，保存任务信息\n"
            "fetch_v2.py — 轮询 H3 任务并下载视频\n\n"
            "新资产要求 — 温暖插画、干净墙面与肤色、减少水彩斑驳。角色形象与 A-pose，场景概念与布局图。\n"
            "生图接口及模型兼容性待验证。当前展示的是原始参考图。新图完成后等待用户确认，再进行视频生成。\n"
            "完整资产要求见 production_pack/asset_library/ASSET_BRIEF.md"
        ],
    })
    workflow = {"last_node_id": len(nodes), "last_link_id": 0, "nodes": nodes, "links": [],
                "groups": groups, "config": {}, "extra": {"ds": {"scale": 0.55, "offset": [80, 60]}},
                "version": 0.4}
    name = "Cyan_Character_Scene_Library.json"
    text = json.dumps(workflow, ensure_ascii=False, indent=2)
    (HERE / name).write_text(text)
    (WORKFLOWS / name).write_text(text)
    print(json.dumps({"workflow": str(WORKFLOWS / name), "input": str(INPUT),
                      "source_nodes": sum(node["type"] == "LoadImage" for node in nodes)}, indent=2))


if __name__ == "__main__":
    main()
