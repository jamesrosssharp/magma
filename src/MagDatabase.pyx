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

    
cdef class Cell:
    cdef dict layers
    cdef str name
    cdef str tech

    def __init__(self):
        self.layers = {}

    def setTech(self, str tech):
        self.tech = tech

    def addRect(self, str layer, int xbot, int ybot, int xtop, int ytop):

        r = Rect()

        r.xbot = xbot
        r.ybot = ybot
        r.xtop = xtop
        r.ytop = ytop

        if layer not in self.layers:
            self.layers[layer] = []

        self.layers[layer].append(r)

    def dump(self):
        print(f"cell {self.name}")
        for l in self.layers:
            print(f" layer {l}")
            for r in self.layers[l]:
                print(f"  ({r.xbot} {r.ybot}) ({r.xtop} {r.ytop})")


cdef class MagDatabase:

    cdef dict cells

    def __init__(self):
        self.cells = {}

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

