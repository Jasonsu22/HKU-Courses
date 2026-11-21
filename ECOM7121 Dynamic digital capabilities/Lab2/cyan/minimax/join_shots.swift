// Joins 10-second shots end to end at 1920x1080 and lays the matching stretch of an existing
// narrated video underneath as the soundtrack (each clip's own sound is dropped).
//
//   swift join_shots.swift <audio_source.mp4> <audio_start_s> <out.mp4> clip1.mp4 clip2.mp4 ...
import AVFoundation

let a = CommandLine.arguments
let audioSrc = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let audioStart = Double(a[2])!
let out = URL(fileURLWithPath: a[3])
// Each clip may carry its own length as "path@seconds"; otherwise it is cut to 10 s.
let specs: [(AVURLAsset, Double)] = a[4...].map { arg in
    let parts = arg.split(separator: "@", maxSplits: 1).map(String.init)
    return (AVURLAsset(url: URL(fileURLWithPath: parts[0])), parts.count > 1 ? Double(parts[1])! : 10)
}
try? FileManager.default.removeItem(at: out)

let W: CGFloat = 1920, H: CGFloat = 1080
let comp = AVMutableComposition()
let v = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
var instructions: [AVMutableVideoCompositionInstruction] = []
var t = CMTime.zero
for (c, secs) in specs {
    let src = c.tracks(withMediaType: .video)[0]
    let len = CMTimeMinimum(CMTime(seconds: secs, preferredTimescale: 600), c.duration)
    try! v.insertTimeRange(CMTimeRange(start: .zero, duration: len), of: src, at: t)
    let sz = src.naturalSize
    let s = min(W / sz.width, H / sz.height)
    let ins = AVMutableVideoCompositionInstruction()
    ins.timeRange = CMTimeRange(start: t, duration: len)
    let li = AVMutableVideoCompositionLayerInstruction(assetTrack: v)
    li.setTransform(CGAffineTransform(scaleX: s, y: s)
        .concatenating(CGAffineTransform(translationX: (W - sz.width * s) / 2, y: (H - sz.height * s) / 2)), at: t)
    ins.layerInstructions = [li]
    instructions.append(ins)
    t = t + len
}
let au = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
try! au.insertTimeRange(CMTimeRange(start: CMTime(seconds: audioStart, preferredTimescale: 600), duration: t),
                        of: audioSrc.tracks(withMediaType: .audio)[0], at: .zero)

let vc = AVMutableVideoComposition()
vc.renderSize = CGSize(width: W, height: H)
vc.frameDuration = CMTime(value: 1, timescale: 24)
vc.instructions = instructions
let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
ex.outputURL = out; ex.outputFileType = .mp4; ex.videoComposition = vc
let sem = DispatchSemaphore(value: 0); ex.exportAsynchronously { sem.signal() }; sem.wait()
print(ex.status == .completed ? "Wrote \(out.path) (\(t.seconds) s)" : "failed \(String(describing: ex.error))")
