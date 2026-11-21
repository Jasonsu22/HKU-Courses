# Cyan character and environment library

Status: original source references and video prompts are being imported. External image API compatibility remains unverified.
Requested model family: Image 2.6 or 2.5, pending provider verification. Requested delivery: 1080p.

## Visual direction

Use Clip 2 and the existing production pack as the visual basis. Warm, tidy middle-class Hong Kong interiors, delicate ink contours, restrained transparent watercolour, smooth even skin and fabric shading, clean painted walls, clean tiles and stainless steel. Very subtle paper texture. Eliminate water stains, limescale, weathering, grime and patchy grey surface mottling. Preserve illustration character and warm evening light.

Generate original artwork without logos, signatures or decorative star marks. Source images may contain a corner star. Do not reproduce that source overlay in newly generated artwork.

## Characters

- Mei. Source `style_refs/ref_mei_scene1.jpg`, `style_refs/ref_mei_scene6.jpg` and `scene_refs/scene02.jpg`. 29-year-old Hong Kong woman, youthful smooth face, black shoulder-length hair in a low ponytail, cream button blouse, grey trousers, canvas tote, right-handed. Deliver an identity sheet with front, three-quarter, profile and rear views, plus a separate full-body A-pose sheet with front, side and rear views. Arms approximately 35 degrees below horizontal, relaxed open hands, neutral expression. Preserve reference face and clothing. Shoes and any hidden details require user review.
- Ka-ho. Source `scene_refs/scene09.jpg` and `scene_refs/scene13.jpg`. 31-year-old Hong Kong man, short black hair, thin round glasses, navy hoodie. Deliver an identity sheet and separate front/side/rear full-body A-pose sheet. Lower-body clothing and shoes are incompletely visible and require user review.
- Community volunteer. Source `scene_refs/scene14.jpg` and the script. Friendly woman in a yellow apron. Existing image provides insufficient facial detail. Deliver proposed identity and A-pose sheets, explicitly labelled as a new design proposal pending review.

## Environments

- Kitchen. Primary baseline is Clip 2, with `scene_refs/scene02.jpg`, `scene_refs/scene03.jpg`, `scene_refs/scene05.jpg`, `scene_refs/scene09.jpg` and the kitchen style reference as supporting evidence. One narrow fridge, right-hinged with left handle. Use the actual Clip 2 kitchen geometry as the authority when other reference shots conflict. Deliver a clean unoccupied concept image, then a coherent top-down layout and four cardinal wall views. Hidden walls, dimensions, door locations and connections are proposals pending review.
- Living and dining area. Source `scene_refs/scene04.jpg`, `scene_refs/scene08.jpg`, `scene_refs/scene13.jpg`, `scene_refs/scene15.jpg` and `scene_refs/scene17.jpg`. Small table, sofa, warm lamp, plants and window with Hong Kong housing towers. Deliver an unoccupied concept image plus top-down and four wall views. Sources do not establish one continuous floor plan. Proposed connections require review.
- Community cooking classroom. Source `scene_refs/scene14.jpg` and script. Bright community centre with a cooking workshop table. Deliver an unoccupied concept and layout sheet. Interior geometry is a proposal because the source mostly shows the facade and a distant window view.
- MTR carriage. Source `scene_refs/scene01.jpg` and `style_refs/ref_mei_scene1.jpg`. Yellow poles, overhead triangular grips, windows and Hong Kong evening city view. Deliver an unoccupied concept and consistent plan/end/side views, preserving the visible reference arrangement.

## Generation order

1. Generate and review Mei identity and kitchen concept using the original source images.
2. Use the approved identity image to derive Mei A-pose and later shots.
3. Generate Ka-ho and volunteer identities, then their A-pose sheets using their respective approved identity images.
4. Establish each environment concept before deriving its layout and directional views from that concept. Do not independently generate conflicting wall views.
5. Import each approved output as a named ComfyUI Load Image node beside its source and generation prompt.

No video generation is part of this asset-review stage.
