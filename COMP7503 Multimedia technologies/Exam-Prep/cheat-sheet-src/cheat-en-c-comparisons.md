### Key comparisons (from the slides)
**Multimedia vs monomedia (单媒体):** monomedia (computer vision, audio processing) analyses one medium in isolation; multimedia follows how humans experience the world, correlating and combining partial information from multiple sources in the problem's context. e.g. COVID gate (thermal + camera) vs face detection alone.
**Experiential vs current information environments:** experiential = direct senses, same query/presentation space, user state/context, exploration; current = alphanumeric tables, formal queries/commands, separate result space, one medium, so humans do the logical work.
**Human vs digital computer (人机差异):** human = objects/events/concepts, perceptual and contextual, tolerates ambiguity, learns by experience; computer = bits/bytes in lists/arrays/tables, exact fast maths/logic, no meaning without models -> semantic gap.
**Experience vs information vs knowledge:** experience = direct observation/participation; information = abstract communication of it (the act of experiencing is lost); knowledge = accumulated experiences.
**Objects vs events:** objects = static components; events = changes in relationships among objects over time. e.g. person vs person entering a restricted zone.
**Content vs context vs metadata:** content = acquired data (pixels); context = conditions of acquisition; metadata = data about data giving context (Exif time/GPS).
**Procedural vs OO vs functional:** steps (how, step by step) vs classes = objects + methods = events vs declare what you want (not how).
**Sampling vs quantization:** sampling discretises time (fs; error = discretization; sets max frequency fs/2); quantization discretises amplitude (n bits; error = quantization noise; sets precision). Neither replaces the other.
**Nyquist rate vs Nyquist frequency:** Nyquist rate = 2B, the minimum sampling rate for highest frequency B; Nyquist frequency = fs/2, the highest frequency a given fs can represent.
**Resistive vs capacitive touch:** both layered sensors giving x-y. Resistive = pressure makes two conductive layers touch; any object/glove, dust/water-proof, firm press, single touch. Capacitive = finger changes capacitance; light multi-touch, no ordinary gloves, water disturbs.
**Dynamic vs condenser mic:** both diaphragm -> analog voltage. Dynamic = coil in magnet (induction), no power, robust, high SPL. Condenser = capacitor plates (C=epsilon*A/d), needs power, more sensitive, studio.
**Omni vs cardioid vs supercardioid vs shotgun:** all angles (quiet studio, conference table) vs front, null 180 deg vs narrower, rear lobe, null 120 deg vs highly directional.
**Echo vs reverberation vs interference:** one delayed reflection (merged if < 0.1 s) vs many decaying reflections in a room vs superposition (in phase 2A, anti-phase cancel = ANC).
**ITD vs ILD vs HRTF:** time difference vs level difference (both left/right) vs pinna filtering (front/back/up/down).
**Frequency vs temporal masking:** loud sound hides a softer one in a nearby band (simultaneous) vs a quiet sound just after a loud one is hidden (ear gain recovering).
**LPC vs MPEG audio:** LPC models speech production (source-filter, parameters, GSM, speech only); MPEG models hearing (psychoacoustic masking, bit allocation, any audio). "How was it produced?" vs "which errors are hard to hear?".
**Stabilization vs deblurring:** frame-to-frame camera shake (track background, compensate) vs blur within one exposure (blur kernel, deconvolution).
**Detection vs recognition vs tracking:** is there a face and where vs whose face vs same identity across frames.
**Feature-based vs model-based:** face detection = Haar features + AdaBoost; head tracking / 3-D reconstruction = fit a general model (spline, AAM, mesh); model-based tolerates expression and pose.
**VR vs AR:** fully virtual environment vs digital content overlaid on the real view.
**Pitch vs timbre:** perceived fundamental F0 vs spectrum + envelope quality. Harmonic = k*f0; overtone = harmonic above the fundamental (1st overtone = 2nd harmonic); partial = any component.
**Photometry vs radiometry:** weighted by human sensitivity (cd, lm, lx) vs physical power (W, W/sr).
**Candela vs lumen vs lux:** one direction (spotlight) vs total output (bulb, projector) vs per area received (desk, camera low-light rating). 1 lm = 1 cd*sr; 1 lx = 1 lm/m^2.
**Reflection vs refraction:** bounces back (angle in = angle out) vs bends into a new medium (wavelength changes, frequency fixed). Specular (mirror, directional) vs diffuse (scattered).
**Monochromatic vs coherent vs polarized:** one frequency vs stable relative phase (laser) vs fixed field orientation.
**CCD vs CMOS (slide table):** pixel transfer shift register vs direct pixel address; charge->voltage after readout vs in-pixel; exposure single frame vs frame/line-sequential; sensitivity higher vs lower; control circuit off-sensor vs integrated. CCD better low light; megapixel phones use CMOS.
**Stereo vs ToF:** passive, two views, Z=fB/d vs active near-IR, Z=c*Delta t/2.
**Photo vs video camera:** still images (up to 32 MP) vs image sequence at FPS, compressed into one file (up to 16 MP).
**Additive vs subtractive:** emit and mix light (RGB, screens, zero = black) vs absorb ambient light (CMYK ink, needs light, white paper).
**RGB vs CMYK vs YUV:** display vs printing vs compression (luma + chroma, chroma subsampled).
**LCD vs OLED:** backlight + liquid crystal + polarisers (grey black, thicker) vs self-emitting pixels (true black, thin, flexible).
**Photopic vs scotopic:** cones 6-7M, fovea, own nerve each, colour + detail, bright light vs rods 75-150M, periphery, shared nerves, dim light, no colour.
**Luminance vs luma vs subjective brightness:** physical photometric light vs weighted Y' signal (0.299R+0.587G+0.114B) vs perceived, logarithmic, context-dependent.

### Past-paper answer cues (finals 2015-2025: Q1-Q2 = L1-L5)
**Most asked:** experiential environment (6x), sampling + quantization effects (5x), human vs computer (4x), Neisser/perception diagram, DIKW, mic digitization.
**Digitize audio with a mic (model answer):** sound pressure -> diaphragm -> analog voltage (dynamic/condenser) -> preamp gain (avoid clipping, keep headroom) -> anti-alias low-pass -> sample at fs > 2B (Nyquist; 44.1 kHz for 20-22 kHz hearing) -> quantize to n bits (quantization noise = rounding error, SNR about 6.02n dB) -> encode PCM -> store/transmit.
**Sampling-rate choice:** signal bandwidth (Nyquist), human perceptual limits, storage/bandwidth cost, processing/ML needs, anti-alias filter margin. Standards: CD 44.1 kHz (20 kHz audio), telephone 8 kHz (about 3.4-4 kHz speech), PAL 25 / NTSC 30 fps.
**Effects per medium (采样/量化对质量的影响):** AUDIO low fs -> lost highs + aliasing, few bits -> hiss, low dynamic range. IMAGE low spatial sampling -> pixelation, jagged edges, moire; few bits -> banding/false contours. VIDEO low fps -> jerky motion, wagon-wheel aliasing; each frame as image.
**Quantization = "the other process":** A-law/mu-law = non-uniform (perceptual) quantization, 8 bits at 8 kHz = 64 kb/s, finer steps for quiet sounds (Weber-Fechner: perceived change proportional to dI/I).
**SPL logarithmic:** pressures span about 10^7 (20 microPa to 200 Pa) and hearing responds roughly logarithmically.
**Sinusoid for sound vs light:** SOUND A = pressure (Pa, dB SPL) -> loudness, f (Hz) -> pitch, phi -> interference; LIGHT A = E-field -> intensity (cd, lm, lx), f or lambda (nm) -> colour, phi -> coherence.
**Speech in frequency domain:** phonemes show as formant patterns; the waveform changes with loudness/phase; the cochlea analyses frequency.
**Conference-table mic:** omnidirectional (participants all around). Polar pattern measured by rotating the mic before a constant-SPL source, per angle, at several frequencies.
**Nit (cd/m^2):** suits displays: luminance per area is independent of screen size and viewing distance. Phone cameras: lenses close together to minimise parallax; ultra-wide/wide/tele = zoom range + fusion + depth (bokeh), HDR/night.
**Calcs seen:** CD 44.1k*16*2 = 1.4112 Mb/s; 5 min CD 52.92 MB vs A-law 2.4 MB -> about 22:1; FHD RGB24 PAL 1920*1080*24*25 = 1.244 Gb/s; fovea 337,500 vs 1080p 2,073,600.
