# distutils: language = c++
# cython: language_level=3

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map

cdef struct Rect:
    int xbot
    int ybot
    int xtop
    int ytop

cdef struct Transform:
    int a, b, c, d, e, f  # Transformation matrix (scalings and offsets)

cdef struct CellUse:
    string instance_name
    string cell_name
    Transform transform

cdef struct Label:
    Rect bbox
    string layer
    string text
    int position

cdef class MagicCell:
    cdef public str name
    cdef public str tech
    
    # Store geometry as C++ vectors keyed by layer name string
    cdef unordered_map[string, vector[Rect]] _geometry
    cdef vector[CellUse] _uses
    cdef vector[Label] _labels

    def __init__(self, str name, str tech=""):
        self.name = name
        self.tech = tech

    cdef void c_add_rect(self, const string& layer, int xbot, int ybot, int xtop, int ytop) noexcept:
        cdef Rect r = Rect(xbot, ybot, xtop, ytop)
        self._geometry[layer].push_back(r)

    def add_rect(self, str layer, int xbot, int ybot, int xtop, int ytop):
        self.c_add_rect(layer.encode('utf-8'), xbot, ybot, xtop, ytop)

    cdef void c_add_use(self, const string& cell_name, const string& inst_name, 
                       int a, int b, int c, int d, int e, int f) noexcept:
        cdef Transform t = Transform(a, b, c, d, e, f)
        cdef CellUse u = CellUse(inst_name, cell_name, t)
        self._uses.push_back(u)

    def add_use(self, str cell_name, str inst_name, tuple transform):
        a, b, c, d, e, f = transform
        self.c_add_use(cell_name.encode('utf-8'), inst_name.encode('utf-8'), a, b, c, d, e, f)

    cdef void c_add_label(self, const string& layer, int xbot, int ybot, int xtop, int ytop, 
                         int pos, const string& text) noexcept:
        cdef Rect r = Rect(xbot, ybot, xtop, ytop)
        cdef Label l = Label(r, layer, text, pos)
        self._labels.push_back(l)

    def add_label(self, str layer, int xbot, int ybot, int xtop, int ytop, int pos, str text):
        self.c_add_label(layer.encode('utf-8'), xbot, ybot, xtop, ytop, pos, text.encode('utf-8'))

    def get_rects(self, str layer):
        cdef string l_bytes = layer.encode('utf-8')
        if self._geometry.count(l_bytes) == 0:
            return []
        cdef vector[Rect] rects = self._geometry[l_bytes]
        return [(r.xbot, r.ybot, r.xtop, r.ytop) for r in rects]

    def get_uses(self):
        return [
            {
                "cell_name": u.cell_name.decode('utf-8'),
                "instance_name": u.instance_name.decode('utf-8'),
                "transform": (u.transform.a, u.transform.b, u.transform.c, 
                              u.transform.d, u.transform.e, u.transform.f)
            }
            for u in self._uses
        ]

    def get_bounding_box(self):
        """Computes cell bounding box fast in C space."""
        if self._geometry.empty():
            return (0, 0, 0, 0)
            
        cdef int min_x = 2147483647
        cdef int min_y = 2147483647
        cdef int max_x = -2147483648
        cdef int max_y = -2147483648

        for pair in self._geometry:
            for r in pair.second:
                if r.xbot < min_x: min_x = r.xbot
                if r.ybot < min_y: min_y = r.ybot
                if r.xtop > max_x: max_x = r.xtop
                if r.ytop > max_y: max_y = r.ytop

        return (min_x, min_y, max_x, max_y)

cdef class MagicDatabase:
    cdef dict cells

    def __init__(self):
        self.cells = {}

    def get_or_create_cell(self, str name, str tech=""):
        if name not in self.cells:
            self.cells[name] = MagicCell(name, tech)
        return self.cells[name]
