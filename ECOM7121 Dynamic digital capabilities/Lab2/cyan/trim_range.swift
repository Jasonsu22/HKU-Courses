// Removes a time range from a video (video + audio). swift trim_range.swift in.mp4 out.mp4 start end
import AVFoundation
let a = CommandLine.arguments
let src = AVURLAsset(url: URL(fileURLWithPath: a[1])); let out = URL(fileURLWithPath: a[2])
let cut = CMTimeRange(start: CMTime(seconds: Double(a[3])!, preferredTimescale: 600), end: CMTime(seconds: Double(a[4])!, preferredTimescale: 600))
try? FileManager.default.removeItem(at: out)
let comp = AVMutableComposition()
try! comp.insertTimeRange(CMTimeRange(start: .zero, duration: src.duration), of: src, at: .zero)
comp.removeTimeRange(cut)
let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
ex.outputURL = out; ex.outputFileType = .mp4
let s = DispatchSemaphore(value: 0); ex.exportAsynchronously { s.signal() }; s.wait()
print(ex.status == .completed ? "Wrote \(out.path) (\(String(format: "%.1f", comp.duration.seconds)) s)" : "failed \(String(describing: ex.error))")
