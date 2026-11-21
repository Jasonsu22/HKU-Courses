// Puts a still photo (fitted on a cream background) in front of a video for `hold` seconds.
//   swift prepend_photo.swift team_photo.jpg in.mp4 out.mp4 [hold=1.5]
import AVFoundation; import AppKit
let a = CommandLine.arguments
let photo = NSImage(contentsOfFile: a[1])!, src = AVURLAsset(url: URL(fileURLWithPath: a[2]))
let out = URL(fileURLWithPath: a[3]); let hold = a.count > 4 ? Double(a[4])! : 1.5
let tmp = out.deletingLastPathComponent().appendingPathComponent("_photo_intro.mp4")
try? FileManager.default.removeItem(at: tmp); try? FileManager.default.removeItem(at: out)
let vt = src.tracks(withMediaType: .video)[0]; let W = Int(vt.naturalSize.width), H = Int(vt.naturalSize.height)

// 1) still clip
let w = try! AVAssetWriter(outputURL: tmp, fileType: .mp4)
let inp = AVAssetWriterInput(mediaType: .video, outputSettings: [AVVideoCodecKey: AVVideoCodecType.h264, AVVideoWidthKey: W, AVVideoHeightKey: H])
let ad = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: inp, sourcePixelBufferAttributes: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA, kCVPixelBufferWidthKey as String: W, kCVPixelBufferHeightKey as String: H])
w.add(inp); w.startWriting(); w.startSession(atSourceTime: .zero)
var pb: CVPixelBuffer?; CVPixelBufferPoolCreatePixelBuffer(nil, ad.pixelBufferPool!, &pb); let buf = pb!
CVPixelBufferLockBaseAddress(buf, [])
let ctx = CGContext(data: CVPixelBufferGetBaseAddress(buf), width: W, height: H, bitsPerComponent: 8, bytesPerRow: CVPixelBufferGetBytesPerRow(buf), space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedFirst.rawValue | CGBitmapInfo.byteOrder32Little.rawValue)!
ctx.setFillColor(CGColor(red: 0.984, green: 0.965, blue: 0.925, alpha: 1)); ctx.fill(CGRect(x: 0, y: 0, width: W, height: H))
let cg = photo.cgImage(forProposedRect: nil, context: nil, hints: nil)!
let sc = min(Double(W) / Double(cg.width), Double(H) / Double(cg.height))
let pw = Double(cg.width) * sc, ph = Double(cg.height) * sc
ctx.interpolationQuality = .high
ctx.draw(cg, in: CGRect(x: (Double(W) - pw) / 2, y: (Double(H) - ph) / 2, width: pw, height: ph))
// team title card (top-left, same style as the in-video cards)
let k = Double(H) / 1080.0
let tFont = NSFont(name: "Helvetica Neue Bold", size: 40 * k)!, sFont = NSFont(name: "Helvetica Neue", size: 24 * k)!
let title = "Team Climbing Cat · Group Cyan", sub = "Household Inventory · ECOM7121 Innovation Lab 2"
let tA: [NSAttributedString.Key: Any] = [.font: tFont, .foregroundColor: NSColor(calibratedRed: 0.17, green: 0.15, blue: 0.13, alpha: 1)]
let sA: [NSAttributedString.Key: Any] = [.font: sFont, .foregroundColor: NSColor(calibratedRed: 0.12, green: 0.43, blue: 0.43, alpha: 1)]
let tS = (title as NSString).size(withAttributes: tA), sS = (sub as NSString).size(withAttributes: sA)
let padX = 22 * k, padY = 14 * k, bar = 8 * k, gap = 4 * k, m = 44 * k
let cw = max(tS.width, sS.width) + padX * 2 + bar, ch = tS.height + sS.height + gap + padY * 2
let cx = (Double(W) - pw) / 2 + m, cy = Double(H) - m - ch
ctx.saveGState()
ctx.setShadow(offset: CGSize(width: 0, height: -3 * k), blur: 12 * k, color: CGColor(gray: 0, alpha: 0.3))
ctx.setFillColor(CGColor(red: 0.98, green: 0.96, blue: 0.92, alpha: 0.95))
ctx.addPath(CGPath(roundedRect: CGRect(x: cx, y: cy, width: cw, height: ch), cornerWidth: 12 * k, cornerHeight: 12 * k, transform: nil)); ctx.fillPath()
ctx.restoreGState()
ctx.setFillColor(CGColor(red: 0.12, green: 0.48, blue: 0.48, alpha: 1)); ctx.fill(CGRect(x: cx, y: cy, width: bar, height: ch))
NSGraphicsContext.current = NSGraphicsContext(cgContext: ctx, flipped: false)
(title as NSString).draw(at: NSPoint(x: cx + bar + padX, y: cy + padY + sS.height + gap), withAttributes: tA)
(sub as NSString).draw(at: NSPoint(x: cx + bar + padX, y: cy + padY), withAttributes: sA)
NSGraphicsContext.current = nil
CVPixelBufferUnlockBaseAddress(buf, [])
let fps: Int32 = 30
for f in 0...Int(hold * Double(fps)) { while !inp.isReadyForMoreMediaData { usleep(1000) }; ad.append(buf, withPresentationTime: CMTime(value: CMTimeValue(f), timescale: fps)) }
inp.markAsFinished(); let sem = DispatchSemaphore(value: 0); w.finishWriting { sem.signal() }; sem.wait()

// 2) join: photo, then the video (audio shifted by `hold`)
let intro = AVURLAsset(url: tmp); let introDur = CMTime(seconds: hold, preferredTimescale: 600)
let comp = AVMutableComposition()
let cv = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
try! cv.insertTimeRange(CMTimeRange(start: .zero, duration: introDur), of: intro.tracks(withMediaType: .video)[0], at: .zero)
try! cv.insertTimeRange(CMTimeRange(start: .zero, duration: src.duration), of: vt, at: introDur)
for at in src.tracks(withMediaType: .audio) {
  let ca = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
  try! ca.insertTimeRange(CMTimeRange(start: .zero, duration: src.duration), of: at, at: introDur)
}
let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
ex.outputURL = out; ex.outputFileType = .mp4; ex.exportAsynchronously { sem.signal() }; sem.wait()
try? FileManager.default.removeItem(at: tmp)
print(ex.status == .completed ? "Wrote \(out.path) (\(String(format: "%.1f", comp.duration.seconds)) s)" : "Export failed: \(String(describing: ex.error))")
