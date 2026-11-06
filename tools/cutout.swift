// Détourage automatique (Vision, macOS 14+) : ./cutout entrée sortie.png
import Foundation
import Vision
import CoreImage

let a = CommandLine.arguments
guard a.count >= 3, let img = CIImage(contentsOf: URL(fileURLWithPath: a[1])) else { print("usage: cutout in out.png"); exit(1) }
let req = VNGenerateForegroundInstanceMaskRequest()
let handler = VNImageRequestHandler(ciImage: img, options: [:])
do { try handler.perform([req]) } catch { print("vision error: \(error)"); exit(2) }
guard let res = req.results?.first else { print("no subject"); exit(3) }
do {
  let buf = try res.generateMaskedImage(ofInstances: res.allInstances, from: handler, croppedToInstancesExtent: true)
  let out = CIImage(cvPixelBuffer: buf)
  let ctx = CIContext()
  let cs = CGColorSpace(name: CGColorSpace.sRGB)!
  try ctx.writePNGRepresentation(of: out, to: URL(fileURLWithPath: a[2]), format: .RGBA8, colorSpace: cs, options: [:])
  print("ok \(Int(out.extent.width))x\(Int(out.extent.height))")
} catch { print("mask error: \(error)"); exit(4) }
