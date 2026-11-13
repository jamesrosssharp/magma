"""
3D viewer for Magic .mag cell hierarchies.

Parses a layout with the magma MagParser / MagDatabase, extrudes every
rect to its physical z extent (see src/LayerStack.py) and renders the
hierarchy with OpenGL 3.3 via PySide6.

Each cell definition is uploaded to the GPU once; instances are drawn
with their accumulated Magic transform as the model matrix, so the
hierarchy is never flattened.

Usage:
    python3 mag_viewer3d.py strong-arm/strong_arm_latch_routed.mag
    python3 mag_viewer3d.py top.mag -L /opt/pdk/sky130A/libs.ref/sky130_fd_sc_hd/mag
    python3 mag_viewer3d.py top.mag --screenshot top.png

Controls:
    left drag   orbit            middle/right drag   pan
    wheel       zoom             F   frame selection (or whole design)
    T           top-down view    R   reset view
"""

import argparse
import glob
import math
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = sorted(glob.glob(os.path.join(_here, "build", "lib*"))) + [os.path.join(_here, "src")]

import numpy as np

import MagParser
import MagDatabase
import LayerStack

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import (QColor, QGuiApplication, QIcon, QMatrix4x4, QOffscreenSurface, QOpenGLContext,
                           QPixmap, QSurfaceFormat, QVector3D, QVector4D)
from PySide6.QtOpenGL import (QOpenGLBuffer, QOpenGLFramebufferObject, QOpenGLFramebufferObjectFormat, QOpenGLShader, QOpenGLShaderProgram,
                              QOpenGLVertexArrayObject)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QDockWidget, QDoubleSpinBox, QFormLayout,
                               QListWidget, QListWidgetItem, QMainWindow, QTreeWidget,
                               QTreeWidgetItem, QWidget)

GL_TRIANGLES        = 0x0004
GL_LINES            = 0x0001
GL_FLOAT            = 0x1406
GL_DEPTH_TEST       = 0x0B71
GL_BLEND            = 0x0BE2
GL_SRC_ALPHA        = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_COLOR_BUFFER_BIT = 0x4000
GL_DEPTH_BUFFER_BIT = 0x0100

IDENTITY = MagDatabase.Transform(1, 0, 0, 0, 1, 0)

CONTACT_LAYERS = {"ndiffc", "pdiffc", "nsubdiffcont", "psubdiffcont", "polycont",
                  "viali", "via1", "via2", "via3", "via4",
                  "xpolycontact", "mimcapcontact", "mimcap2contact"}
CONTACT_INSET_UM = 0.004

# ---------------------------------------------------------------------------
# Geometry
# ---------------------------------------------------------------------------

# Box corner c = (x[c & 1], y[(c >> 1) & 1], z[(c >> 2) & 1])
_FACES = [((0, 2, 3, 1), (0, 0, -1)), ((4, 5, 7, 6), (0, 0, 1)),
          ((0, 4, 6, 2), (-1, 0, 0)), ((1, 3, 7, 5), (1, 0, 0)),
          ((0, 1, 5, 4), (0, -1, 0)), ((2, 6, 7, 3), (0, 1, 0))]
_TRI_CORNERS = np.array([q[i] for q, _ in _FACES for i in (0, 1, 2, 0, 2, 3)])
_TRI_NORMALS = np.array([n for _, n in _FACES for _ in range(6)], dtype=np.float32)

# Unit cube edges for wireframe bounding boxes
_EDGE_CORNERS = np.array([0, 1, 2, 3, 4, 5, 6, 7, 0, 2, 1, 3, 4, 6, 5, 7, 0, 4, 1, 5, 2, 6, 3, 7])


def extrude_rects(rects, z0, z1):
    """(N, 4) array of xbot, ybot, xtop, ytop -> (N*36, 6) position/normal vertices."""
    xs = rects[:, [0, 2]]
    ys = rects[:, [1, 3]]
    c = _TRI_CORNERS
    pos = np.stack([xs[:, c & 1], ys[:, (c >> 1) & 1],
                    np.where((c >> 2) & 1, z1, z0)[None, :].repeat(len(rects), 0)], axis=-1)
    nrm = np.broadcast_to(_TRI_NORMALS, pos.shape)
    return np.concatenate([pos, nrm], axis=-1).reshape(-1, 6).astype(np.float32)


def unit_cube_lines():
    c = _EDGE_CORNERS
    pos = np.stack([c & 1, (c >> 1) & 1, (c >> 2) & 1], axis=-1).astype(np.float32)
    return np.concatenate([pos, np.zeros_like(pos)], axis=-1)


class Instance:
    """One placement of a cell in the flattened instance tree (hierarchy kept)."""

    def __init__(self, path, cell, transform, parent, depth):
        self.path      = path          # e.g. "x1/XM3"
        self.cell      = cell          # cell definition name
        self.transform = transform     # MagDatabase.Transform, cell -> top coords
        self.parent    = parent        # index of parent Instance, -1 for top
        self.depth     = depth
        self.end       = None          # one past the last descendant index
        self.checked   = True
        self.bbox      = None          # (xbot, ybot, xtop, ytop) in top db units

    def matrix(self):
        t = self.transform
        return QMatrix4x4(t.a, t.b, 0, t.c,
                          t.d, t.e, 0, t.f,
                          0,   0,   1, 0,
                          0,   0,   0, 1)


class LayoutScene:
    """Builds GPU-ready geometry for a MagDatabase cell hierarchy."""

    def __init__(self, db, top, stack=LayerStack.SKY130_LAYERS):
        self.db     = db
        self.top    = top
        self.layers = LayerStack.layer_map(stack)
        self.order  = [l.name for l in stack]

        self.ranges       = {}   # cell -> {layer: (first_vertex, count)}
        self.local_bbox   = {}   # cell -> own-geometry bbox in cell coords, or None
        self.placeholders = {}   # cell -> bbox, for cells whose .mag was not found
        self.unknown      = set()
        self.rect_count   = 0

        chunks = []
        nverts = 0
        for name, cell in db.cells.items():
            self.ranges[name] = {}
            bb = None
            for lname in self.order:
                if lname not in cell.layers:
                    continue
                L = self.layers[lname]
                # De-duplicate in case a .mag file repeats a rect
                rects = np.array(sorted({(r.xbot, r.ybot, r.xtop, r.ytop)
                                         for r in cell.layers[lname]}), dtype=np.float32)
                # Inset multi-layer contacts slightly so their faces don't z-fight
                # with the conductors they connect
                eps = CONTACT_INSET_UM if L.name in CONTACT_LAYERS else 0.0
                v = extrude_rects(rects, L.z0 + eps, L.z1 - eps)
                self.ranges[name][lname] = (nverts, len(v))
                chunks.append(v)
                nverts += len(v)
                self.rect_count += len(rects)
                lo, hi = rects[:, :2].min(0), rects[:, 2:].max(0)
                bb = _union(bb, (lo[0], lo[1], hi[0], hi[1]))

            for lname in cell.layers:
                if lname not in self.layers and lname not in LayerStack.NON_PHYSICAL:
                    self.unknown.add(lname)

            self.local_bbox[name] = bb
            b = cell.bbox
            if not cell.layers and not cell.uses and b.xbot < b.xtop:
                self.placeholders[name] = (b.xbot, b.ybot, b.xtop, b.ytop)

        self.vertices = np.concatenate(chunks) if chunks else np.zeros((0, 6), np.float32)

        self.instances = []
        self._flatten(top, IDENTITY, "", -1, 0)

    def _flatten(self, cell_name, transform, path, parent, depth):
        idx = len(self.instances)
        inst = Instance(path or cell_name, cell_name, transform, parent, depth)
        self.instances.append(inst)

        own = self.local_bbox.get(cell_name) or self.placeholders.get(cell_name)
        inst.bbox = _transform_bbox(transform, own) if own else None

        for use in self.db.getCell(cell_name).uses:
            child = transform.Transform(use['transform'] or IDENTITY)   # parent @ child
            cpath = use['inst_name'] if not path else path + "/" + use['inst_name']
            cidx = self._flatten(use['name'], child, cpath, idx, depth + 1)
            inst.bbox = _union(inst.bbox, self.instances[cidx].bbox)

        inst.end = len(self.instances)
        return idx


def _union(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def _transform_bbox(t, bb):
    xs, ys = [], []
    for x, y in ((bb[0], bb[1]), (bb[2], bb[1]), (bb[0], bb[3]), (bb[2], bb[3])):
        xs.append(t.a * x + t.b * y + t.c)
        ys.append(t.d * x + t.e * y + t.f)
    return (min(xs), min(ys), max(xs), max(ys))


# ---------------------------------------------------------------------------
# OpenGL widget
# ---------------------------------------------------------------------------

VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 a_pos;
layout(location = 1) in vec3 a_nrm;
uniform mat4 u_mvp;
uniform mat4 u_model;
out vec3 v_nrm;
void main() {
    v_nrm = mat3(u_model) * a_nrm;
    gl_Position = u_mvp * vec4(a_pos, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 v_nrm;
uniform vec4  u_color;
uniform float u_lit;
uniform float u_highlight;
out vec4 frag;
void main() {
    vec3 c = u_color.rgb;
    if (u_lit > 0.5) {      // lines have no normal
        vec3 n = normalize(v_nrm);
        float d = abs(dot(n, normalize(vec3(0.35, 0.55, 1.0)))) * 0.65
                + abs(dot(n, normalize(vec3(-0.6, -0.3, 0.4)))) * 0.20;
        c *= 0.30 + d;
    }
    c = mix(c, vec3(1.0, 0.9, 0.2), 0.35 * u_highlight);
    frag = vec4(c, u_color.a);
}
"""


class LayoutRenderer:
    """Camera, GL resources and drawing. Needs a current OpenGL 3.3 context."""

    def __init__(self, scene):
        self.scene = scene
        self.visible_layers = {n for n, l in scene.layers.items() if l.visible}
        self.selected = 0
        self.z_scale = 1.0
        self.width, self.height = 1, 1
        self.reset_view()

    # -- camera -------------------------------------------------------------

    def reset_view(self):
        self.yaw, self.pitch = -60.0, 35.0
        self.frame(0)

    def frame(self, idx):
        bb = self.scene.instances[idx].bbox or (0, 0, 1, 1)
        u = LayerStack.DB_UNIT_UM
        w, h = (bb[2] - bb[0]) * u, (bb[3] - bb[1]) * u
        self.target = QVector3D((bb[0] + bb[2]) * 0.5 * u, (bb[1] + bb[3]) * 0.5 * u,
                                2.0 * self.z_scale)
        self.distance = max(w, h, 1.0) * 1.8

    def orbit(self, dx, dy):
        self.yaw -= dx * 0.4
        self.pitch = max(-89.9, min(89.9, self.pitch + dy * 0.4))

    def pan(self, dx, dy):
        y, p = math.radians(self.yaw), math.radians(self.pitch)
        right = QVector3D(-math.sin(y), math.cos(y), 0)
        up = QVector3D(-math.sin(p) * math.cos(y), -math.sin(p) * math.sin(y), math.cos(p))
        k = self.distance / max(self.height, 1)
        self.target += (right * -dx + up * dy) * k

    def _eye(self):
        y, p = math.radians(self.yaw), math.radians(self.pitch)
        d = QVector3D(math.cos(p) * math.cos(y), math.cos(p) * math.sin(y), math.sin(p))
        return self.target + d * self.distance

    def _view_proj(self):
        proj = QMatrix4x4()
        proj.perspective(40.0, max(self.width, 1) / max(self.height, 1),
                         self.distance * 0.01, self.distance * 100.0)
        view = QMatrix4x4()
        up = QVector3D(0, 1, 0) if abs(self.pitch) > 89.0 else QVector3D(0, 0, 1)
        view.lookAt(self._eye(), self.target, up)
        return proj * view

    def _units(self):
        m = QMatrix4x4()
        u = LayerStack.DB_UNIT_UM
        m.scale(u, u, self.z_scale)
        return m

    # -- GL -----------------------------------------------------------------

    def initialize(self):
        self.gl = QOpenGLContext.currentContext().functions()
        self.gl.glClearColor(0.12, 0.13, 0.15, 1.0)

        self.prog = QOpenGLShaderProgram()
        self.prog.addShaderFromSourceCode(QOpenGLShader.Vertex, VERTEX_SHADER)
        self.prog.addShaderFromSourceCode(QOpenGLShader.Fragment, FRAGMENT_SHADER)
        if not self.prog.link():
            raise RuntimeError(self.prog.log())

        self.mesh_vao, self.mesh_vbo = self._upload(self.scene.vertices)
        self.cube_vao, self.cube_vbo = self._upload(unit_cube_lines())

    def _upload(self, verts):
        vao = QOpenGLVertexArrayObject()
        vao.create()
        vao.bind()
        vbo = QOpenGLBuffer(QOpenGLBuffer.VertexBuffer)
        vbo.create()
        vbo.bind()
        data = np.ascontiguousarray(verts, dtype=np.float32)
        vbo.allocate(data.tobytes(), data.nbytes)
        self.prog.bind()
        for loc, off in ((0, 0), (1, 12)):
            self.prog.enableAttributeArray(loc)
            self.prog.setAttributeBuffer(loc, GL_FLOAT, off, 3, 24)
        vao.release()
        vbo.release()
        return vao, vbo

    def paint(self):
        gl = self.gl
        gl.glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gl.glEnable(GL_DEPTH_TEST)

        sc = self.scene
        vp = self._view_proj()
        units = self._units()
        self.prog.bind()

        # Visibility: an instance is shown only if it and all its ancestors are checked
        shown = []
        for inst in sc.instances:
            shown.append(inst.checked and (inst.parent < 0 or shown[inst.parent]))
        sel = sc.instances[self.selected]
        sel_range = range(self.selected, sel.end) if self.selected > 0 else range(0)

        opaque = [n for n in sc.order if n in self.visible_layers and sc.layers[n].color[3] >= 1.0]
        translucent = [n for n in sc.order if n in self.visible_layers and sc.layers[n].color[3] < 1.0]

        self.mesh_vao.bind()
        self.prog.setUniformValue1f("u_lit", 1.0)
        for layers, blend in ((opaque, False), (translucent, True)):
            if blend:
                gl.glEnable(GL_BLEND)
                gl.glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                gl.glDepthMask(False)
            for i, inst in enumerate(sc.instances):
                ranges = sc.ranges.get(inst.cell)
                if not shown[i] or not ranges:
                    continue
                model = units * inst.matrix()
                self.prog.setUniformValue("u_mvp", vp * model)
                self.prog.setUniformValue("u_model", model)
                self.prog.setUniformValue1f("u_highlight", 1.0 if i in sel_range else 0.0)
                for lname in layers:
                    r = ranges.get(lname)
                    if r:
                        self.prog.setUniformValue("u_color", QVector4D(*sc.layers[lname].color))
                        gl.glDrawArrays(GL_TRIANGLES, r[0], r[1])
        gl.glDepthMask(True)
        gl.glDisable(GL_BLEND)
        self.mesh_vao.release()

        # Wireframes: unresolved cells (orange) and the selection (yellow)
        self.cube_vao.bind()
        self.prog.setUniformValue1f("u_lit", 0.0)
        self.prog.setUniformValue1f("u_highlight", 0.0)
        for i, inst in enumerate(sc.instances):
            if shown[i] and inst.cell in sc.placeholders:
                self._draw_box(vp, units, _transform_bbox(inst.transform, sc.placeholders[inst.cell]),
                               (0.0, 1.0), (1.0, 0.55, 0.1, 1.0))
        if sel_range and sel.bbox:
            self._draw_box(vp, units, sel.bbox, (-0.3, 7.0), (1.0, 0.9, 0.2, 1.0))
        self.cube_vao.release()

    def _draw_box(self, vp, units, bb, z, color):
        m = QMatrix4x4()
        m.translate(bb[0], bb[1], z[0])
        m.scale(bb[2] - bb[0], bb[3] - bb[1], z[1] - z[0])
        model = units * m
        self.prog.setUniformValue("u_mvp", vp * model)
        self.prog.setUniformValue("u_model", model)
        self.prog.setUniformValue("u_color", QVector4D(*color))
        self.gl.glDrawArrays(GL_LINES, 0, len(_EDGE_CORNERS))



class LayoutView(QOpenGLWidget):

    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.r = LayoutRenderer(scene)
        self._last = QPoint()
        self.setFocusPolicy(Qt.StrongFocus)

    def initializeGL(self):
        self.r.initialize()

    def resizeGL(self, w, h):
        self.r.width, self.r.height = w, h

    def paintGL(self):
        self.r.paint()

    # -- input --------------------------------------------------------------

    def mousePressEvent(self, e):
        self._last = e.position().toPoint()

    def mouseMoveEvent(self, e):
        pos = e.position().toPoint()
        dx, dy = pos.x() - self._last.x(), pos.y() - self._last.y()
        self._last = pos
        if e.buttons() & Qt.LeftButton:
            self.r.orbit(dx, dy)
        elif e.buttons() & (Qt.MiddleButton | Qt.RightButton):
            self.r.pan(dx, dy)
        self.update()

    def wheelEvent(self, e):
        self.r.distance *= 0.85 ** (e.angleDelta().y() / 120.0)
        self.update()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F:
            self.r.frame(self.r.selected)
        elif e.key() == Qt.Key_T:
            self.r.yaw, self.r.pitch = -90.0, 89.95
        elif e.key() == Qt.Key_R:
            self.r.reset_view()
        else:
            return super().keyPressEvent(e)
        self.update()


# ---------------------------------------------------------------------------
# Main window
# ---------------------------------------------------------------------------

class ViewerWindow(QMainWindow):

    def __init__(self, scene, title):
        super().__init__()
        self.scene = scene
        self.setWindowTitle(f"magma 3D - {title}")
        self.view = LayoutView(scene, self)
        self.setCentralWidget(self.view)

        # Hierarchy
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Instance", "Cell"])
        items = []
        for i, inst in enumerate(scene.instances):
            name = inst.path.split("/")[-1]
            it = QTreeWidgetItem([name, inst.cell])
            it.setFlags(it.flags() | Qt.ItemIsUserCheckable)
            it.setCheckState(0, Qt.Checked)
            it.setData(0, Qt.UserRole, i)
            if inst.cell in scene.placeholders:
                it.setForeground(1, QColor(255, 140, 25))
                it.setToolTip(1, "Cell .mag not found: shown as bounding box")
            if inst.parent < 0:
                self.tree.addTopLevelItem(it)
            else:
                items[inst.parent].addChild(it)
            items.append(it)
        self.tree.expandToDepth(0)
        self.tree.resizeColumnToContents(0)
        self.tree.itemChanged.connect(self._instance_toggled)
        self.tree.currentItemChanged.connect(self._instance_selected)
        self.tree.resizeColumnToContents(1)
        hier = self._dock("Hierarchy", self.tree, Qt.LeftDockWidgetArea)
        self.resizeDocks([hier], [340], Qt.Horizontal)

        # Layers
        self.layer_list = QListWidget()
        for lname in reversed(scene.order):
            if not any(lname in r for r in scene.ranges.values()):
                continue
            L = scene.layers[lname]
            pm = QPixmap(14, 14)
            pm.fill(QColor.fromRgbF(*L.color[:3]))
            it = QListWidgetItem(QIcon(pm), lname)
            it.setFlags(it.flags() | Qt.ItemIsUserCheckable)
            it.setCheckState(Qt.Checked if lname in self.view.r.visible_layers else Qt.Unchecked)
            self.layer_list.addItem(it)
        self.layer_list.itemChanged.connect(self._layer_toggled)

        zs = QDoubleSpinBox()
        zs.setRange(0.1, 20.0)
        zs.setSingleStep(0.5)
        zs.setValue(1.0)
        zs.setPrefix("z scale ")
        zs.valueChanged.connect(self._z_scale)
        panel = QWidget()
        form = QFormLayout(panel)
        form.addRow(zs)
        form.addRow(self.layer_list)
        self._dock("Layers", panel, Qt.RightDockWidgetArea)

        n_placeholder = sum(1 for i in scene.instances if i.cell in scene.placeholders)
        msg = (f"{len(scene.instances)} instances, {scene.rect_count} rects, "
               f"{len(scene.vertices) // 3} triangles")
        if n_placeholder:
            msg += f", {n_placeholder} unresolved (use -L to add library paths)"
        self.statusBar().showMessage(msg)

    def _dock(self, title, widget, area):
        d = QDockWidget(title, self)
        d.setWidget(widget)
        self.addDockWidget(area, d)
        return d

    def _instance_toggled(self, item, column):
        if column == 0:
            self.scene.instances[item.data(0, Qt.UserRole)].checked = item.checkState(0) == Qt.Checked
            self.view.update()

    def _instance_selected(self, item, _prev):
        if item is not None:
            self.view.r.selected = item.data(0, Qt.UserRole)
            self.view.update()

    def _layer_toggled(self, item):
        if item.checkState() == Qt.Checked:
            self.view.r.visible_layers.add(item.text())
        else:
            self.view.r.visible_layers.discard(item.text())
        self.view.update()

    def _z_scale(self, v):
        self.view.r.z_scale = v
        self.view.update()


# ---------------------------------------------------------------------------

def load(mag_file, lib_paths):
    parser = MagParser.MagParser()
    db = MagDatabase.MagDatabase()
    # Cells not found next to their parent are searched for in the
    # sub directories of each lib path, in order
    parser.parse(mag_file, db, lib_paths)

    top = os.path.splitext(os.path.basename(mag_file))[0]
    return db, top


def main():
    ap = argparse.ArgumentParser(description="3D viewer for Magic .mag cell hierarchies")
    ap.add_argument("mag", help="top-level .mag file")
    ap.add_argument("-L", "--libpath", action="append", default=[],
                    help="directory whose sub directories are searched for unresolved cells (repeatable)")
    ap.add_argument("--screenshot", metavar="PNG", help="render to an image and exit")
    ap.add_argument("--size", default="1400x900", help="window size, WxH")
    args = ap.parse_args()

    lib_paths = list(args.libpath)
    pdk = os.environ.get("PDK_ROOT")
    if pdk:
        lib_paths.append(os.path.join(pdk, "sky130A", "libs.ref", "sky130_fd_sc_hd", "mag"))

    fmt = QSurfaceFormat()
    fmt.setVersion(3, 3)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setDepthBufferSize(24)
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    if args.screenshot:
        app = QGuiApplication(sys.argv[:1])
    else:
        app = QApplication(sys.argv[:1])
    db, top = load(args.mag, lib_paths)
    scene = LayoutScene(db, top)
    if scene.unknown:
        print("Ignoring layers with no z mapping: " + ", ".join(sorted(scene.unknown)))
    w, h = (int(v) for v in args.size.split("x"))

    if args.screenshot:
        render_to_image(scene, w, h).save(args.screenshot)
        print(f"Wrote {args.screenshot}")
        return 0

    win = ViewerWindow(scene, top)
    win.resize(w, h)
    win.show()
    return app.exec()


def render_to_image(scene, w, h, renderer=None):
    """Render a scene without a window (works with QT_QPA_PLATFORM=offscreen)."""
    ctx = QOpenGLContext()
    ctx.setFormat(QSurfaceFormat.defaultFormat())
    if not ctx.create():
        raise RuntimeError("Could not create an OpenGL context")
    surface = QOffscreenSurface()
    surface.setFormat(ctx.format())
    surface.create()
    ctx.makeCurrent(surface)

    ffmt = QOpenGLFramebufferObjectFormat()
    ffmt.setAttachment(QOpenGLFramebufferObject.Depth)
    ffmt.setSamples(4)
    fbo = QOpenGLFramebufferObject(w, h, ffmt)
    fbo.bind()

    r = renderer or LayoutRenderer(scene)
    r.width, r.height = w, h
    r.initialize()
    ctx.functions().glViewport(0, 0, w, h)
    r.paint()
    img = fbo.toImage()
    fbo.release()
    ctx.doneCurrent()
    return img


if __name__ == "__main__":
    sys.exit(main())
