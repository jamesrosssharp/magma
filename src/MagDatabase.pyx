# cython: language_level=3
# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map
from libc.stdio cimport FILE, fopen, fclose, getline, fwrite
from libc.stdlib cimport free, atoi
from cython.operator cimport dereference as deref, preincrement as inc

cdef class Rect:
    cdef public int xbot
    cdef public int ybot
    cdef public int xtop
    cdef public int ytop

    def __init__(self, _xbot, _ybot, _xtop, _ytop):
        self.xbot = _xbot
        self.ybot = _ybot
        self.xtop = _xtop
        self.ytop = _ytop

    def dump(self):
        print(str(self))

    def __str__(self):
        return f"    {self.xbot} {self.ybot} {self.xtop} {self.ytop}"

    def __repr__(self):
        return self.__str__()

    def abuts(self, Rect r):
        # Check for side-by-side contact (vertical edge match + overlapping Y interval)
        touch_horizontal = self.xtop == r.xbot or self.xbot == r.xtop
        overlap_y = max(self.ybot, r.ybot) < min(self.ytop, r.ytop)

        # Check for top-and-bottom contact (horizontal edge match + overlapping X interval)
        touch_vertical = self.ytop == r.ybot or self.ybot == r.ytop
        overlap_x = max(self.xbot, r.xbot) < min(self.xtop, r.xtop)

        return (touch_horizontal and overlap_y) or (touch_vertical and overlap_x)

    def overlaps(self, Rect r):
       
        # If the rects are identical, don't return true
        #if self.xtop == r.xtop and self.xbot == r.xbot and self.ytop == r.ytop and self.ybot == r.ybot:
        #    return False

        overlap_top = self.xbot <= r.xtop and self.xtop >= r.xtop and self.ybot <= r.ytop and self.ytop >= r.ytop
        overlap_bot = self.xbot <= r.xbot and self.xtop >= r.xbot and self.ybot <= r.ybot and self.ytop >= r.ybot

        if overlap_top or overlap_bot:
            return True

        overlap_top = r.xbot <= self.xtop and r.xtop >= self.xtop and r.ybot <= self.ytop and r.ytop >= self.ytop
        overlap_bot = r.xbot <= self.xbot and r.xtop >= self.xbot and r.ybot <= self.ybot and r.ytop >= self.ybot

        if overlap_top or overlap_bot:
            return True

        return False


cdef class Transistor:

    cdef list gates
    cdef list source_drains

    def __init__(self):
        self.gates         = []
        self.source_drains = []

cdef class Cell:
    cdef dict layers
    cdef str name
    cdef str tech

    def __init__(self):
        self.layers = {}

    def setTech(self, str tech):
        self.tech = tech

    def addRect(self, str layer, int xbot, int ybot, int xtop, int ytop):

        r = Rect(xbot, ybot, xtop, ytop)

        if layer not in self.layers:
            self.layers[layer] = []

        self.layers[layer].append(r)

    def dump(self):
        print(f"cell {self.name}")
        for l in self.layers:
            print(f" layer {l}")
            for r in self.layers[l]:
                r.dump()

    def find_transistors(self):
        """
        Returns a list of Transistor objects for all transistors in the cell
        """

        # 1. First, find all nmos rects. This is the active region of an nmos transistor.

        if self.layers['nmos'] is not None:
            for r in self.layers['nmos']:
            
                # Find all polysilicon rects which abut the nmos rects

                poly_r = []

                for rp in self.layers['poly']:
                    if rp.abuts(r):
                        poly_r.append(rp)


                for rp in self.layers['poly']:
                    for i in range(0, len(poly_r)):
                        if poly_r[i].abuts(rp):
                            poly_r.append(rp)

                print(poly_r)
                
                # Find all polycont rects which overlap poly_r
                
                poly_c = []

                for pc in self.layers['polycont']:
                    for pr in poly_r:
                        print(f"{pc} {pr}")
                        if pc.overlaps(pr):
                            poly_c.append(pc)
                            break

                print(poly_c)


cdef class MagDatabase:

    cdef dict cells
    cdef dict cell_transistors

    def __init__(self):
        self.cells = {}
        self.cell_transistors = {}

    def createCell(self, str name):
        
        c = Cell()

        c.name = name 

        self.cells[name] = c

    def addRectToCell(self, str name, str layer, int xbot, int ybot, int xtop, int ytop):

        self.cells[name].addRect(layer, xbot, ybot, xtop, ytop)

    def setCellTech(self, str name, str tech):

        self.cells[name].setTech(tech)

    def dump(self):

        for c in self.cells:
            self.cells[c].dump()

    def findCellTransistors(self, str name):

        t = self.cells[name].find_transistors()
        
        self.cell_transistors[name] = t

    def findAllTransistors(self):

        for c in self.cells:
            self.findCellTransistors(c)
