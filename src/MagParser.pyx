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

    # lib_path -> {cell name: .mag file path}, built on first use of each path
    cdef dict _lib_index

    def __init__(self):
        self._lib_index = {}

    cdef dict _get_lib_index(self, str lib_path):
        """Index every .mag file found in the sub directories of lib_path.

        Directories are walked top-down in sorted order, so if a cell name
        appears more than once the shallowest (then alphabetically first)
        match wins.
        """
        index = self._lib_index.get(lib_path)
        if index is None:
            index = {}
            for root, dirs, files in os.walk(lib_path):
                dirs.sort()
                for fname in sorted(files):
                    if fname.endswith(".mag"):
                        index.setdefault(fname[:-4], os.path.join(root, fname))
            self._lib_index[lib_path] = index
        return index

    def find_cell(self, str cell_name, str default_file, lib_path=None):
        """Return the .mag file for cell_name.

        default_file is used if it exists; otherwise the sub directories of
        lib_path (if given) are searched. lib_path may be a single directory
        or a list of directories, searched in order. Falls back to
        default_file so the caller reports the original path when the cell
        cannot be found.
        """
        if os.path.isfile(default_file) or not lib_path:
            return default_file
        if isinstance(lib_path, str):
            lib_path = [lib_path]
        for d in lib_path:
            found = self._get_lib_index(os.path.expanduser(d)).get(cell_name)
            if found is not None:
                return found
        return default_file

    def parse(self, str filename, db, lib_path=None):
        """Parse a .mag file and its sub cells into db.

        lib_path: optional directory, or list of directories. A sub cell that cannot be found at the
        path given by its "use" line (or next to the parent .mag file) is
        searched for in the sub directories of lib_path.
        """

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

                    newfile = self.find_cell(new_cell, newfile, lib_path)

                    # Each cell definition is parsed once; later uses only add an
                    # instance. A cell that failed to load is retried, since a later
                    # use may give a different path.
                    if not db.isCellLoaded(new_cell):
                        try:
                            self.parse(newfile, db, lib_path)
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
                    except Exception as e:
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

                    print(f"{cell_name_str} {labname}")

                    db.addLabelToCell(cell_name_str, layer, xbot, ybot, xtop, ytop, pos, font, a, b, c, d, labname)

                elif s.startswith("port"):

                    ss = s.split()

                    port = int(ss[1])
                    directions = ss[2]
                    
                    db.setLabelPort(cell_name_str, labname, port, directions)

        db.markCellLoaded(cell_name_str)


