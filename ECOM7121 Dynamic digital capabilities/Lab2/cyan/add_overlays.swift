// Adds the on-screen text to the raw Google Vids export, after the fact.
// Each card sits in the top-left corner, pops in (scale + fade), holds, then pops out.
//
//   swift add_overlays.swift <raw.mp4> <out.mp4>
//
// Edit the `cards` list below to change wording or timing.

import AVFoundation
import AppKit
import QuartzCore

struct Card { let t: Double; let title: String; let sub: String?; let hold: Double }

// t = seconds from the start of the video. hold = time fully visible (pop in/out adds 0.25 s each).
let cards: [Card] = [
    Card(t: 0.4,   title: "Household Inventory", sub: "Team Climbing Cat · Group Cyan", hold: 1.5),
    Card(t: 3.0,   title: "Illustrative scenario · Mei is fictional", sub: nil, hold: 1.5),
    Card(t: 23.0,  title: "~3,000 t of food waste a day · 67% from homes", sub: "EPD, waste statistics for 2024", hold: 1.5),
    Card(t: 41.0,  title: "Working prototype · fictional data", sub: "cyan-household.vercel.app", hold: 1.5),
    Card(t: 81.0,  title: "Unexpected change", sub: nil, hold: 1.2),
    Card(t: 91.0,  title: "Guardrail veto", sub: nil, hold: 1.2),
    Card(t: 131.0, title: "No organisation has endorsed this proposal", sub: "HK$28/month tier is illustrative", hold: 1.5),
    Card(t: 154.0, title: "Proposed pilot · not yet run", sub: "Targets are hypotheses", hold: 1.5),
    Card(t: 164.5, title: "Household Inventory", sub: "Team Climbing Cat · Group Cyan · ECOM7121", hold: 2.5),
]

let args = CommandLine.arguments
guard args.count == 3 else { print("usage: swift add_overlays.swift raw.mp4 out.mp4"); exit(1) }
let src = AVURLAsset(url: URL(fileURLWithPath: args[1]))
let out = URL(fileURLWithPath: args[2])
try? FileManager.default.removeItem(at: out)

let vTrack = src.tracks(withMediaType: .video)[0]
let size = vTrack.naturalSize.applying(vTrack.preferredTransform)
let W = abs(size.width), H = abs(size.height)
let s = H / 1080.0                    // scale everything to the video height
let margin = 44 * s

let comp = AVMutableComposition()
let cv = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
try! cv.insertTimeRange(CMTimeRange(start: .zero, duration: src.duration), of: vTrack, at: .zero)
cv.preferredTransform = vTrack.preferredTransform
for a in src.tracks(withMediaType: .audio) {
    let ca = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
    try! ca.insertTimeRange(CMTimeRange(start: .zero, duration: src.duration), of: a, at: .zero)
}

let parent = CALayer(); parent.frame = CGRect(x: 0, y: 0, width: W, height: H)
let video = CALayer(); video.frame = parent.frame
parent.addSublayer(video)

func textSize(_ str: String, _ font: NSFont) -> CGSize {
    (str as NSString).size(withAttributes: [.font: font])
}

let titleFont = NSFont(name: "Helvetica Neue Bold", size: 30 * s) ?? NSFont.boldSystemFont(ofSize: 30 * s)
let subFont = NSFont(name: "Helvetica Neue", size: 20 * s) ?? NSFont.systemFont(ofSize: 20 * s)
let accent = CGColor(red: 0.12, green: 0.48, blue: 0.48, alpha: 1)   // cyan-teal bar

for c in cards {
    let tSize = textSize(c.title, titleFont)
    let sSize = c.sub.map { textSize($0, subFont) } ?? .zero
    let padX = 18 * s, padY = 12 * s, gap = c.sub == nil ? 0 : 4 * s, bar = 6 * s
    let w = max(tSize.width, sSize.width) + padX * 2 + bar
    let h = tSize.height + sSize.height + gap + padY * 2

    let card = CALayer()
    card.frame = CGRect(x: margin, y: H - margin - h, width: w, height: h)  // CA origin is bottom-left
    card.backgroundColor = CGColor(red: 0.98, green: 0.96, blue: 0.92, alpha: 0.93)
    card.cornerRadius = 10 * s
    card.shadowOpacity = 0.25; card.shadowRadius = 8 * s; card.shadowOffset = CGSize(width: 0, height: -2 * s)
    card.opacity = 0
    card.anchorPoint = CGPoint(x: 0, y: 1)          // grow from the top-left corner
    card.position = CGPoint(x: margin, y: H - margin)

    let b = CALayer(); b.frame = CGRect(x: 0, y: 0, width: bar, height: h); b.backgroundColor = accent
    b.cornerRadius = 3 * s; card.addSublayer(b)

    let tl = CATextLayer()
    tl.string = c.title; tl.font = titleFont; tl.fontSize = titleFont.pointSize
    tl.foregroundColor = CGColor(red: 0.17, green: 0.15, blue: 0.13, alpha: 1); tl.alignmentMode = .left
    tl.frame = CGRect(x: bar + padX, y: h - padY - tSize.height, width: tSize.width + 4, height: tSize.height + 2)
    tl.contentsScale = 2
    tl.displayIfNeeded(); card.addSublayer(tl)
    if let sub = c.sub {
        let sl = CATextLayer()
        sl.string = sub; sl.font = subFont; sl.fontSize = subFont.pointSize
        sl.foregroundColor = CGColor(red: 0.12, green: 0.43, blue: 0.43, alpha: 1); sl.alignmentMode = .left
        sl.frame = CGRect(x: bar + padX, y: padY, width: sSize.width + 4, height: sSize.height + 2)
        sl.contentsScale = 2
        sl.displayIfNeeded(); card.addSublayer(sl)
    }

    let pop = 0.25, total = pop * 2 + c.hold
    let kt: [NSNumber] = [0, NSNumber(value: pop * 0.7 / total), NSNumber(value: pop / total),
                          NSNumber(value: (pop + c.hold) / total), 1]
    let fade = CAKeyframeAnimation(keyPath: "opacity")
    fade.values = [0, 1, 1, 1, 0]; fade.keyTimes = kt
    let scale = CAKeyframeAnimation(keyPath: "transform.scale")
    scale.values = [0.6, 1.06, 1.0, 1.0, 0.7]; scale.keyTimes = kt
    let group = CAAnimationGroup()
    group.animations = [fade, scale]
    group.duration = total
    group.beginTime = AVCoreAnimationBeginTimeAtZero + c.t
    group.isRemovedOnCompletion = false
    group.fillMode = .both
    card.add(group, forKey: "pop")
    parent.addSublayer(card)
}

// ---- Narration subtitles (from subtitles.json), small, bottom-centre, one full sentence each ----
struct Sub: Decodable { let start: Double; let end: Double; let text: String }
let subURL = URL(fileURLWithPath: args[1]).deletingLastPathComponent().appendingPathComponent("subtitles.json")
let subs = (try? JSONDecoder().decode([Sub].self, from: Data(contentsOf: subURL))) ?? []
let subFontS = NSFont(name: "Helvetica Neue Medium", size: 25 * s) ?? NSFont.systemFont(ofSize: 25 * s)
for sb in subs {
    let ts = textSize(sb.text, subFontS)
    let padX = 16 * s, padY = 7 * s
    let w = ts.width + padX * 2, h = ts.height + padY * 2
    let box = CALayer()
    box.frame = CGRect(x: (W - w) / 2, y: 46 * s, width: w, height: h)
    box.backgroundColor = CGColor(red: 0.08, green: 0.07, blue: 0.06, alpha: 0.62)
    box.cornerRadius = 8 * s
    box.opacity = 0
    let tl = CATextLayer()
    tl.string = sb.text; tl.font = subFontS; tl.fontSize = subFontS.pointSize
    tl.foregroundColor = CGColor(red: 1, green: 1, blue: 1, alpha: 1); tl.alignmentMode = .center
    tl.frame = CGRect(x: padX - 2, y: padY - 1, width: ts.width + 4, height: ts.height + 2)
    tl.contentsScale = 2; tl.displayIfNeeded()
    box.addSublayer(tl)
    let dur = max(sb.end - sb.start, 0.3), f = min(0.12, dur / 4)
    let a = CAKeyframeAnimation(keyPath: "opacity")
    a.values = [0, 1, 1, 0]
    a.keyTimes = [0, NSNumber(value: f / dur), NSNumber(value: 1 - f / dur), 1]
    a.duration = dur
    a.beginTime = AVCoreAnimationBeginTimeAtZero + sb.start
    a.isRemovedOnCompletion = false; a.fillMode = .both
    box.add(a, forKey: "sub")
    parent.addSublayer(box)
}
print("subtitles:", subs.count)

let vc = AVMutableVideoComposition(propertiesOf: comp)
vc.renderSize = CGSize(width: W, height: H)
vc.animationTool = AVVideoCompositionCoreAnimationTool(postProcessingAsVideoLayer: video, in: parent)

let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
ex.outputURL = out; ex.outputFileType = .mp4; ex.videoComposition = vc
let done = DispatchSemaphore(value: 0)
ex.exportAsynchronously { done.signal() }
done.wait()
print(ex.status == .completed ? "Wrote \(out.path)" : "Export failed: \(String(describing: ex.error))")
