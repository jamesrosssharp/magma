# cython: language_level=3
# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map
from libc.stdio cimport FILE, fopen, fclose, getline, fwrite
from libc.stdlib cimport free, atoi
from cython.operator cimport dereference as deref, preincrement as inc

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

                    print(f"Magscale: {nums[1]} {nums[2]}")

                elif s.startswith("tech"):
                    tech = s.split()[1]
                    print(f"Tech: {tech}")

                    # db.

                elif s.startswith("<<"):

                    if s.split()[1] == "end":
                        # Flush cell


                        break

                    cur_layer = s.split()[1]
                    print(f"Layer: {cur_layer}")

                elif s.startswith("rect"):

                    ss = s.split()

                    xbot = ss[1]
                    ybot = ss[2]
                    xtop = ss[3]
                    ytop = ss[4]

                    print(f"Rect: coords ({xbot},{ybot}) ({xtop},{ytop})")
