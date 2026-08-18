# cython: language_level=3
# distutils: language = c++

from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map

cdef struct Rect:
    int x1
    int y1
    int x2
    int y2

cdef struct Cell:
    string name

cdef class MagDatabase:

    cdef unordered_map[string, Cell] cells

