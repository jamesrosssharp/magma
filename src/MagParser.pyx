# cython: language_level=3
# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map
from libc.stdio cimport FILE, fopen, fclose, getline, fwrite
from libc.stdlib cimport free, atoi
from cython.operator cimport dereference as deref, preincrement as inc

import os

from MagDatabase import MagDatabase

cdef class MagParser:

    def __init__(self):
        pass

    def parse(self, str filename, db):

        cdef str cell_name_str = filename.split('/')[-1].split('\\')[-1]
        if cell_name_str.endswith(".mag"):
            cell_name_str = cell_name_str[:-4]
        cdef string cell_name = cell_name_str.encode('utf-8')

        db.createCell(cell_name_str)

        cdef str cur_layer

        with open(filename) as f:

            for line in f:

                s = line.strip()
                if s == "magic": 
                    continue
                elif s.startswith("magscale"):
                    nums = s.split()

                    #print(f"Magscale: {nums[1]} {nums[2]}")

                elif s.startswith("tech"):
                    tech = s.split()[1]
                    #print(f"Tech: {tech}")

                    db.setCellTech(cell_name_str, tech)

                elif s.startswith("use"):
                    new_cell = s.split()[1]

                    newfile = os.path.dirname(filename) + "/" + new_cell + ".mag"

                    self.parse(newfile, db)

                    cell_inst = db.setCellUse(cell_name_str, new_cell, s.split()[2])

                elif s.startswith("transform"):

                    parms = s.split()

                    a = int(parms[1])
                    b = int(parms[2])
                    c = int(parms[3])
                    d = int(parms[4])
                    e = int(parms[5])
                    f = int(parms[6])

                    db.setCellUseTransform(cell_name_str, cell_inst, a, b, c, d, e, f)

                elif s.startswith("<<"):

                    if s.split()[1] == "end":
                        # Flush cell


                        break

                    cur_layer = s.split()[1]
                    #print(f"Layer: {cur_layer}")

                elif s.startswith("rect"):

                    ss = s.split()

                    xbot = int(ss[1])
                    ybot = int(ss[2])
                    xtop = int(ss[3])
                    ytop = int(ss[4])

                    #print(f"Rect: coords ({xbot},{ybot}) ({xtop},{ytop})")

                    db.addRectToCell(cell_name_str, cur_layer, xbot, ybot, xtop, ytop)
