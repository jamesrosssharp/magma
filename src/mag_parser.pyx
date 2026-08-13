# cython: language_level=3
import os
import numpy as np
cimport numpy as cnp

from libc.stdio cimport FILE, fopen, fclose, fgets, sscanf
from libc.string cimport strncmp

cdef class MagParser:
    cdef public float min_x, min_y, max_x, max_y
    cdef public int rect_count

    def __init__(self):
        self.min_x = 1e9
        self.min_y = 1e9
        self.max_x = -1e9
        self.max_y = -1e9
        self.rect_count = 0

    cdef void transform_point(self, float x, float y, float t[6], float* out_x, float* out_y) nogil:
        out_x[0] = t[0] * x + t[1] * y + t[2]
        out_y[0] = t[3] * x + t[4] * y + t[5]

    cdef void combine_transforms(self, float p[6], float c[6], float out[6]) nogil:
        out[0] = p[0] * c[0] + p[1] * c[3]
        out[1] = p[0] * c[1] + p[1] * c[4]
        out[2] = p[0] * c[2] + p[1] * c[5] + p[2]
        out[3] = p[3] * c[0] + p[4] * c[3]
        out[4] = p[3] * c[1] + p[4] * c[4]
        out[5] = p[3] * c[2] + p[4] * c[5] + p[5]

    cdef void parse_file_recursive(self, str file_path, float current_t[6], dict all_layers, str base_dir):
        if not os.path.exists(file_path):
            if not file_path.endswith('.mag'):
                file_path += '.mag'
            if not os.path.exists(file_path):
                return

        cdef bytes b_path = file_path.encode('utf-8')
        cdef FILE* fp = fopen(b_path, "r")
        if fp == NULL:
            return

        cdef char line[1024]
        cdef char layer_buf[256]
        cdef char use_cell_buf[256]
        cdef int x1, y1, x2, y2
        cdef float ta, tb, tc, td, te, tf
        cdef float child_t[6], combined_t[6]
        cdef str cur_layer = ""
        cdef str pending_child_cell = ""
        cdef float p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y
        cdef float rx1, ry1, rx2, ry2

        try:
            while fgets(line, sizeof(line), fp) != NULL:
                if strncmp(line, "<< ", 3) == 0:
                    if sscanf(line, "<< %255s >>", layer_buf) == 1:
                        cur_layer = layer_buf.decode('utf-8').lower()
                    continue

                if strncmp(line, "rect ", 5) == 0:
                    if sscanf(line, "rect %d %d %d %d", &x1, &y1, &x2, &y2) == 4:
                        self.transform_point(x1, y1, current_t, &p1x, &p1y)
                        self.transform_point(x2, y1, current_t, &p2x, &p2y)
                        self.transform_point(x2, y2, current_t, &p3x, &p3y)
                        self.transform_point(x1, y2, current_t, &p4x, &p4y)

                        rx1 = min(p1x, min(p2x, min(p3x, p4x)))
                        rx2 = max(p1x, max(p2x, max(p3x, p4x)))
                        ry1 = min(p1y, min(p2y, min(p3y, p4y)))
                        ry2 = max(p1y, max(p2y, max(p3y, p4y)))

                        all_layers.setdefault(cur_layer, []).append((rx1, ry1, rx2, ry2))
                        self.rect_count += 1

                        if rx1 < self.min_x: self.min_x = rx1
                        if ry1 < self.min_y: self.min_y = ry1
                        if rx2 > self.max_x: self.max_x = rx2
                        if ry2 > self.max_y: self.max_y = ry2
                    continue

                if strncmp(line, "use ", 4) == 0:
                    if sscanf(line, "use %255s", use_cell_buf) == 1:
                        pending_child_cell = use_cell_buf.decode('utf-8')
                    continue

                if strncmp(line, "transform ", 10) == 0:
                    if pending_child_cell and sscanf(line, "transform %f %f %f %f %f %f", 
                                                       &ta, &tb, &tc, &td, &te, &tf) == 6:
                        child_t[0] = ta; child_t[1] = tb; child_t[2] = tc
                        child_t[3] = td; child_t[4] = te; child_t[5] = tf

                        self.combine_transforms(current_t, child_t, combined_t)
                        child_path = os.path.join(base_dir, pending_child_cell)
                        self.parse_file_recursive(child_path, combined_t, all_layers, base_dir)
                        pending_child_cell = ""
                    continue
        finally:
            fclose(fp)


