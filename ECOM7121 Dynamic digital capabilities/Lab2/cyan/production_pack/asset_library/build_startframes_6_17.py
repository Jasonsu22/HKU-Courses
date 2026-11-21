"""Builds Cyan_Start_Frames_6_17.json: ComfyUI start frames for shots 6-17, from the approved references.
Composition hints come from the version-one scenes (cropped so their corner mark is not copied).

    python3 build_startframes_6_17.py
"""
from build_startframes_workflow import A, CLIP2, CLEAN, STYLE, MEI, build

KAHO = ("Ka-ho is exactly the man on the character sheet in reference 2: same face, short black hair, thin round "
        "wire glasses, light stubble, navy pullover hoodie with white drawstrings over a white t-shirt, dark jeans. "
        "He is right-handed. ")
MEI_KAHO = MEI.replace("reference 1", "reference 1") + KAHO

FRAMES = {
    "shot06": ("Shot 6 - Mei checks a flagged item against the label",
               MEI + "Evening, in exactly the kitchen of reference 2, at the wooden counter by the window. Medium "
               "close-up over her shoulder: in her right hand one smartphone showing a simple app list of food "
               "pictures where one row is softly highlighted in amber (no readable text); in her left hand the "
               "small white yoghurt pot, turned so she can read its lid. She compares the pot with the phone, "
               "attentive and calm. " + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", CLEAN + "scene06.jpg"]),
    "shot07": ("Shot 7 - inside the fridge, use-first items glow",
               "No people. Inside the open fridge of the kitchen in reference 1, seen straight on at shelf height, "
               "tidy and well lit by the warm fridge light. Top shelf: the flat clear produce bag of spinach (like "
               "reference 2) and an open carton of eggs, each traced by a soft glowing cyan-teal outline. Middle "
               "shelf: a bowl of tomatoes, a carton of soy milk, a tray of chicken and two jars, with no glow. Door "
               "shelves with sauces. Clean white interior, no clutter. " + STYLE,
               [A + "04_Kitchen_overview.png", CLIP2 + "t009.6.jpg", CLEAN + "scene07.jpg"]),
    "shot08": ("Shot 8 - dinner idea from what she has",
               MEI + "Evening in exactly the living room of reference 2, lamp on. Mei sits relaxed on the beige "
               "sofa, holding one smartphone in her right hand and looking at it with a small hopeful smile. Above "
               "the phone, a soft dreamy watercolour vision floats in the air like warm steam: a black skillet of "
               "spinach and fried eggs. Medium shot. " + STYLE,
               [A + "01_Mei_Apose.png", A + "05_Living_dining_overview.png", CLEAN + "scene08.jpg"]),
    "shot09": ("Shot 9 - Ka-ho avoids dairy; chicken left out",
               MEI_KAHO + "Morning in exactly the kitchen of reference 3. Mei and Ka-ho stand facing each other "
               "near the counter, mid-conversation. Ka-ho holds a plain carton of milk in his right hand and a "
               "small yoghurt pot in his left, holding them slightly away with an apologetic smile, as if saying "
               "he is avoiding dairy now. Mei listens. On the counter beside the sink, a tray of raw chicken has "
               "been left out uncovered. Medium-wide shot, both characters fully in frame from the knees up, the "
               "chicken tray clearly visible. " + STYLE,
               [A + "01_Mei_Apose.png", A + "02_Kaho_Apose.png", A + "04_Kitchen_overview.png"]),
    "shot10": ("Shot 10 - the Guardrail blocks yoghurt and chicken",
               "No people. Close view along the wooden counter of the kitchen in reference 1: on the left a bowl "
               "of yoghurt topped with berries, on the right the same small plastic tray of raw chicken breast "
               "fillets as in reference 3 (fillets, not a whole bird), uncovered. A translucent cyan-teal "
               "shield of light, like a curved pane of glowing glass, stands in front of both dishes, softly "
               "glowing, the dishes slightly dimmed behind it. Clean tidy counter, wall tiles behind. " + STYLE,
               [A + "04_Kitchen_overview.png", CLEAN + "scene10.jpg", A + "shot11_start.png"]),
    "shot11": ("Shot 11 - Mei inspects the chicken and bins it",
               MEI + "Evening in exactly the kitchen of reference 2, by the counter next to the cream pedal bin "
               "from reference 3. Mei holds one smartphone in her left hand, its screen showing a simple red "
               "warning symbol and a chicken picture (no readable text), and looks with a doubtful frown at the "
               "tray of raw chicken that she holds in her right hand. The pedal bin is on the floor in front of "
               "her with its lid closed. Medium shot. " + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", A + "shot03_start.png"]),
    "shot12": ("Shot 12 - Mei cooks the skillet",
               MEI + "Evening in exactly the kitchen of reference 2. Mei stands at the two-burner gas hob, cooking: "
               "a black cast-iron skillet on the lit burner with wilted spinach and three frying eggs, steam "
               "rising. Her right hand stirs with a wooden spatula, her left hand holds the skillet handle. She "
               "looks pleased and focused. Medium shot from beside the hob so the skillet, her hands and face are "
               "clear. " + STYLE,
               [A + "01_Mei_Apose.png", A + "04_Kitchen_overview.png", CLEAN + "scene12.jpg"]),
    "shot13": ("Shot 13 - Mei and Ka-ho eat together",
               MEI_KAHO + "Evening at the small dining table for two in exactly the living room of reference 3, lamp "
               "on, window with lit towers behind. Mei and Ka-ho sit opposite each other at the two chairs, eating "
               "the spinach and egg skillet from the middle of the table with bowls of rice. Each holds one pair of "
               "chopsticks in the right hand. They smile and chat. A small closed sketchbook lies at the corner of "
               "the table. Medium shot from the side of the table. " + STYLE,
               [A + "01_Mei_Apose.png", A + "02_Kaho_Apose.png", A + "05_Living_dining_overview.png"]),
    "shot14": ("Shot 14 - estate and community cooking workshop",
               "Dusk outside a clean, well-kept Hong Kong public housing estate. A low community-centre building "
               "at the foot of the towers has a large bright window; inside, clearly visible, the volunteer from "
               "reference 1 (mustard apron, light blue shirt) leads a small cooking workshop at a long table with "
               "three residents: an elderly woman, a young father and a teenage girl, with bowls of vegetables. "
               "Lit tower windows above, a few trees, a tidy paved path. Wide shot centred on the bright window. "
               + STYLE,
               [A + "03_Volunteer_Apose.png", CLEAN + "scene14.jpg"]),
    "shot15": ("Shot 15 - privacy: locked notebook and the stop switch",
               "Evening, close view of the light-wood dining table from reference 1. On the left lies a closed "
               "notebook held shut by a strap with exactly one small brass padlock; there is no key anywhere. On "
               "the right lies one smartphone face up, its screen showing a single large rounded toggle switch in "
               "the ON position glowing cyan-teal, and a few plain grey list lines below it (no readable text). "
               "Mei's right hand enters from the right edge, one finger about to touch the toggle. Warm lamp light. "
               + STYLE,
               [A + "05_Living_dining_overview.png", CLEAN + "scene15.jpg", A + "01_Mei_Apose.png"]),
    "shot16": ("Shot 16 - Kwun Tong pilot map and calendar",
               "No people. Top-down view of the light-wood dining table from reference 1. On it lies a large "
               "hand-painted watercolour map of a Hong Kong harbourside district with housing estates, roads and "
               "the waterfront, with no labels or words; about thirty tiny cyan dots are scattered over the "
               "housing estates, unlit. Beside it a small spiral desk calendar showing a simple grid of four weeks "
               "with no numbers, a cup of tea and a pencil. " + STYLE,
               [A + "05_Living_dining_overview.png", CLEAN + "scene16.jpg"]),
    "shot17": ("Shot 17 - Mei at the window at dusk",
               MEI + "Dusk, in exactly the living room of reference 2. Mei stands at the large window beside the "
               "sheer cream curtains, holding a warm cup of tea in both hands, looking out at the lit housing towers "
               "with a calm, content smile. Medium shot from inside the room, slightly behind her shoulder, so both "
               "her face in profile and the view outside are visible. " + STYLE,
               [A + "01_Mei_Apose.png", A + "05_Living_dining_overview.png", CLEAN + "scene17.jpg"]),
}

if __name__ == "__main__":
    build(FRAMES, "Cyan_Start_Frames_6_17", 3000)
