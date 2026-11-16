"""
Regenerate the 3D layout screenshots used in doc/designs.md.

Uses mag_viewer3d's offscreen renderer with fixed camera angles, then crops
each image to its content. Standard cells are resolved from the sky130A PDK:

    PDK_ROOT=/path/to/pdk QT_QPA_PLATFORM=offscreen python3 doc/render_screenshots.py

(PDK_ROOT must contain sky130A/libs.ref/sky130_fd_sc_hd/mag.)
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import mag_viewer3d as mv
from PIL import Image, ImageChops
from PySide6.QtGui import QGuiApplication, QSurfaceFormat

ISO = (-60.0, 35.0)       # same as the viewer's default (R) view
TOP = (-90.0, 89.95)      # same as the viewer's top-down (T) view

# (mag file, output png, (yaw, pitch), zoom, (width, height))
SHOTS = [
    ("high_speed_comp/high_speed_comp_top_routed.mag", "high_speed_comp_iso.png", ISO, 0.8, (1600, 1000)),
    ("high_speed_comp/high_speed_comp_top_routed.mag", "high_speed_comp_top.png", TOP, 1.0, (1000, 1400)),
    ("high_speed_comp/strong_arm_latch_routed.mag", "strong_arm_latch_iso.png", ISO, 0.95, (1600, 1000)),
    ("high_speed_comp/post_amplifier_routed.mag", "post_amplifier_iso.png", ISO, 1.0, (1600, 1000)),
    ("1bit_am/1bit_am_routed.mag", "1bit_am_iso.png", ISO, 0.8, (1600, 1000)),
    ("1bit_am/1bit_am_routed.mag", "1bit_am_top.png", TOP, 1.0, (1000, 1400)),
]


def crop_to_content(path, margin=30):
    im = Image.open(path).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
    x0, y0, x1, y1 = ImageChops.difference(im, bg).getbbox()
    im.crop((max(0, x0 - margin), max(0, y0 - margin),
             min(im.width, x1 + margin), min(im.height, y1 + margin))).save(path, optimize=True)


def main():
    pdk = os.environ.get("PDK_ROOT")
    if not pdk:
        sys.exit("Set PDK_ROOT so the sky130_fd_sc_hd standard cells can be found")
    lib_paths = [os.path.join(pdk, "sky130A", "libs.ref", "sky130_fd_sc_hd")]

    fmt = QSurfaceFormat()
    fmt.setVersion(3, 3)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setDepthBufferSize(24)
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)
    app = QGuiApplication(sys.argv[:1])  # noqa: F841 (must outlive the renders)

    out_dir = os.path.join(ROOT, "doc", "images")
    os.makedirs(out_dir, exist_ok=True)

    for mag, png, (yaw, pitch), zoom, (w, h) in SHOTS:
        db, top = mv.load(os.path.join(ROOT, mag), lib_paths)
        scene = mv.LayoutScene(db, top)
        r = mv.LayoutRenderer(scene)
        r.yaw, r.pitch = yaw, pitch
        r.distance *= zoom
        out = os.path.join(out_dir, png)
        mv.render_to_image(scene, w, h, r).save(out)
        crop_to_content(out)
        print("Wrote", out)


if __name__ == "__main__":
    main()
