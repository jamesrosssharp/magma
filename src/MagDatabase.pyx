# cython: language_level=3
# distutils: language = c++

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.unordered_map cimport unordered_map
from libc.stdio cimport FILE, fopen, fclose, getline, fwrite
from libc.stdlib cimport free, atoi
from cython.operator cimport dereference as deref, preincrement as inc

cdef class MagDatabase:

    def __init__(self):
        pass

    def createCell(self, str name):
        
        c = Cell()

        cdef string name_str = name.encode('utf-8')

        c.name = name_str 

        self.cells[name_str] = c

        

