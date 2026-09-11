# cython: language_level=3
# distutils: language = c++

import numpy as np
import time

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

        # TODO: Rects which completely straddle each other

        return False

    def centroid(self):

        return ((self.xbot + self.xtop) // 2, (self.ybot + self.ytop) // 2)


cdef class Transistor:

    cdef public list gates
    cdef public list source_drains

    def __init__(self):
        self.gates         = []
        self.source_drains = []

    def __repr__(self):
        return f"sources: {self.source_drains} gates: {self.gates}"

    def dump_with_transform(self, transform):
        for g in self.gates:
            p = transform.transform_point(g)
            print(f"\tgate: {p}")

        for sd in self.source_drains:
            p = transform.transform_point(sd)
            print(f"\tsource/drain: {p}")

    def transform(self, transform):

        t = Transistor()

        for g in self.gates:
            p = transform.transform_point(g)
            t.gates.append(p)

        for sd in self.source_drains:
            p = transform.transform_point(sd)
            t.source_drains.append(p)

        return t



cdef class Transform:

    cdef public int a
    cdef public int b
    cdef public int c
    cdef public int d
    cdef public int e
    cdef public int f

    def __init__(self, _a, _b, _c, _d, _e, _f):
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.e = _e
        self.f = _f

    def toMatrix(self):
        return np.array([[self.a, self.b, self.c], [self.d, self.e, self.f], [0, 0, 1]])

    def Transform(self, Transform t):

        tt = np.matmul(self.toMatrix(), t.toMatrix())

        return Transform(tt[0][0], tt[0][1], tt[0][2], tt[1][0], tt[1][1], tt[1][2])

    def transform_point(self, p):

        pp = np.matmul(self.toMatrix(), np.array([p[0], p[1], 1]))

        return (pp[0], pp[1])

cdef class Cell:
    cdef public dict layers
    cdef public str name
    cdef public str tech
    cdef public list transistors
    cdef public list uses
    
    def __init__(self):
        self.layers = {}
        self.transistors = []
        self.uses = []

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

        for u in self.uses:
            print(f" uses {u}")

    def addUse(self, name, inst_name):

        handle = len(self.uses)
        self.uses.append({'name': name, 'inst_name': inst_name, 'transform': None})

        return handle

    def setUseTransform(self, use, a, b, c, d, e, f):
        self.uses[use]['transform'] = Transform(a, b, c, d, e, f)

    def dump_transistors_with_transform(self, db, transform):    
        """
        Dump transistors in this cell and in child cells
        """
        print(f"Dumping transistors in cell {self.name}")

        for i, t in enumerate(self.transistors):
            print(f"Dumping transistor {i}")
            t.dump_with_transform(transform)

        for u in self.uses:
            db.cells[u['name']].dump_transistors_with_transform(db, u['transform'].Transform(transform))

    def dump_transistors(self, db):
        self.dump_transistors_with_transform(db, Transform(1, 0, 0, 0, 1, 0))

    def get_transistors_with_transform(self, db, transform):    
        """
        Get transistors in this cell and in child cells
        """
        t = [tt.transform(transform) for tt in self.transistors]

        for u in self.uses:
            t += db.cells[u['name']].get_transistors_with_transform(db, u['transform'].Transform(transform))

        return t

    def get_transistors(self, db):
        return self.get_transistors_with_transform(db, Transform(1, 0, 0, 0, 1, 0))

    def find_transistors(self):
        """
        Returns a list of Transistor objects for all transistors in the cell
        """

        # 1. First, find all nmos rects. This is the active region of an nmos transistor.

        if 'nmos' in self.layers:
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

                
                # Find all polycont rects which overlap poly_r
                
                poly_c = []

                for pc in self.layers['polycont']:
                    for pr in poly_r:
                        if pc.overlaps(pr):
                            poly_c.append(pc)
                            break


                # Find source and drain contacts

                ndiff_r = []

                for rp in self.layers['ndiff']:
                    if rp.abuts(r):
                        ndiff_r.append(rp)


                for rp in self.layers['ndiff']:
                    for i in range(0, len(ndiff_r)):
                        if ndiff_r[i].abuts(rp):
                            ndiff_r.append(rp)

                # Find all ndiffc rects which overlap ndiff_r
                
                ndiff_c = []

                for nc in self.layers['ndiffc']:
                    for nr in ndiff_r:
                        if nc.overlaps(nr):
                            ndiff_c.append(nc)
                            break

                t = Transistor() 

                for r in poly_c:
                    t.gates.append(r.centroid())

                for r in ndiff_c:
                    t.source_drains.append(r.centroid())

                print(f"Found transistor {t}")

                self.transistors.append(t)

    def getBbox(self, db):

        xbot = 1e10
        ybot = 1e10
        xtop = -1e10
        ytop = -1e10

        for k, v in self.layers.items():
            for r in v:
                if r.xbot < xbot:
                    xbot = r.xbot
                if r.ybot < ybot:
                    ybot = r.ybot
                if r.xtop > xtop:
                    xtop = r.xtop
                if r.ytop > ytop:
                    ytop = r.ytop

        for u in self.uses:
            r = db.getCell(u['name']).getBbox(db)
            if r.xbot < xbot:
                xbot = r.xbot
            if r.ybot < ybot:
                ybot = r.ybot
            if r.xtop > xtop:
                xtop = r.xtop
            if r.ytop > ytop:
                ytop = r.ytop

        return Rect(xbot, ybot, xtop, ytop)



    def writeMagFile(self, db, fname):

        with open(fname, "w") as f:

            f.write("magic\n")

            f.write(f"tech {self.tech}\n")

            # FIXME: Load from file when parsing
            f.write(f"magscale 1 2\n")

            f.write(f"timestamp {int(time.time())}\n")

            f.write(f"<< checkpaint >>\n")

            r = self.getBbox(db)

            f.write(f"rect {r.xbot} {r.ybot} {r.xtop} {r.ytop}\n")

            for k, v in self.layers.items():
                f.write(f"<< {k} >>\n")
                
                for r in v:
                    f.write(f"rect {r.xbot} {r.ybot} {r.xtop} {r.ytop}\n")

            for inst in self.uses:
                f.write(f"use {inst['name']}  {inst['inst_name']}\n")
                f.write(f"timestamp {int(time.time() - 100)}\n")
                f.write(f"transform {inst['transform'].a} {inst['transform'].b} {inst['transform'].c} {inst['transform'].d} {inst['transform'].e} {inst['transform'].f}\n")
                r = db.getCell(inst['name']).getBbox(db)
                f.write(f"box {r.xbot} {r.ybot} {r.xtop} {r.ytop}\n")


            f.write("<< end >>\n")


cdef class MagDatabase:

    cdef public dict cells

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

    def setCellUse(self, str name, str new_cell, str inst_name):

       return self.cells[name].addUse(new_cell, inst_name)

    def setCellUseTransform(self, name, cell_inst, a, b, c, d, e, f):
    
        self.cells[name].setUseTransform(cell_inst, a, b, c, d, e, f)

    def dump(self):

        for c in self.cells:
            self.cells[c].dump()

    def findCellTransistors(self, str name):

        t = self.cells[name].find_transistors()
        
    def findAllTransistors(self):

        for c in self.cells:
            self.findCellTransistors(c)

    def dumpCellTransistors(self, str name):

        cell = self.cells[name]

        cell.dump_transistors(self)

    def getCellTransistors(self, str name):
        """
        Returns all transistors in the cell and in all child cells.
        """

        cell = self.cells[name]

        return cell.get_transistors(self)

    def getCell(self, str name):

        return self.cells[name]


