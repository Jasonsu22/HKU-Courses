// Puts a MiniMax clip over the matching 10 s of narration from the current video.
// swift mux_narration.swift clip.mp4 source_with_narration.mp4 start_seconds out.mp4
import AVFoundation
let a = CommandLine.arguments
let clip = AVURLAsset(url: URL(fileURLWithPath: a[1])), src = AVURLAsset(url: URL(fileURLWithPath: a[2]))
let start = CMTime(seconds: Double(a[3])!, preferredTimescale: 600), out = URL(fileURLWithPath: a[4])
try? FileManager.default.removeItem(at: out)
let comp = AVMutableComposition(); let dur = clip.duration
let v = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
try! v.insertTimeRange(CMTimeRange(start: .zero, duration: dur), of: clip.tracks(withMediaType: .video)[0], at: .zero)
let au = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
try! au.insertTimeRange(CMTimeRange(start: start, duration: dur), of: src.tracks(withMediaType: .audio)[0], at: .zero)
let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
ex.outputURL = out; ex.outputFileType = .mp4
let s = DispatchSemaphore(value: 0); ex.exportAsynchronously { s.signal() }; s.wait()
print(ex.status == .completed ? "Wrote \(out.path)" : "failed \(String(describing: ex.error))")
