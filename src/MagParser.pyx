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

            
                    if (len(s.split()) > 3):
                        newfile = os.path.expanduser(s.split()[3]) + "/" + new_cell + ".mag"
                    else:
                        newfile = os.path.dirname(filename) + "/" + new_cell + ".mag"

                    try:
                        self.parse(newfile, db)
                    except Exception as e:
                        print(f"Error: {e} ")

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

                elif s.startswith("box"):

                    parms = s.split()

                    blx = int(parms[1])
                    bly = int(parms[2])
                    trx = int(parms[3])
                    _try = int(parms[4])

                    db.setCellBBox(new_cell, blx, bly, trx, _try)


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

                # flabel metal1 1826 222 2026 422 0 FreeSans 256 0 0 0 VDD
                # port 0 nsew

                elif s.startswith("flabel"):

                    ss = s.split()

                    layer = ss[1] 
                    
                    idx = 2
                    try:
                        a = int(ss[2])
                    except:
                        idx = 3

                    xbot = int(ss[idx])
                    ybot = int(ss[idx + 1])
                    xtop = int(ss[idx + 2])
                    ytop = int(ss[idx + 3])

                    pos  = int(ss[idx + 4])
                    font = ss[idx + 5]
                    a    = int(ss[idx + 6])
                    b    = int(ss[idx + 7])
                    c    = int(ss[idx + 8])
                    d    = int(ss[idx + 9])

                    labname = ss[idx + 10]

                    db.addLabelToCell(cell_name_str, layer, xbot, ybot, xtop, ytop, pos, font, a, b, c, d, labname)

                elif s.startswith("port"):

                    ss = s.split()

                    port = int(ss[1])
                    directions = ss[2]
                    
                    db.setLabelPort(cell_name_str, labname, port, directions)


