# distutils: language = c++
# cython: language_level=3

from libc.stdio cimport FILE, fopen, fprintf, fclose
from database cimport MagicCell, MagicDatabase  # Assuming class definition from database module

def write_cell_to_mag(MagicCell cell, str filepath):
    """Writes a single MagicCell to a .mag file using C I/O."""
    cdef bytes b_path = filepath.encode('utf-8')
    cdef FILE* f = fopen(b_path, "w")
    if f == NULL:
        raise IOError(f"Failed to open file for writing: {filepath}")

    # 1. File Header
    fprintf(f, "magic\n")
    cdef bytes tech_bytes = cell.tech.encode('utf-8') if cell.tech else b"scmos"
    fprintf(f, "tech %s\n", <char*>tech_bytes)
    fprintf(f, "timestamp 0\n")  # Standard default timestamp

    # 2. Geometry (Grouped by Layer)
    for pair in cell._geometry:
        fprintf(f, "<< %s >>\n", pair.first.c_str())
        for r in pair.second:
            fprintf(f, "rect %d %d %d %d\n", r.xbot, r.ybot, r.xtop, r.ytop)

    # 3. Labels
    if not cell._labels.empty():
        fprintf(f, "<< labels >>\n")
        for l in cell._labels:
            fprintf(f, "rlabel %s %d %d %d %d %d %s\n",
                    l.layer.c_str(),
                    l.bbox.xbot, l.bbox.ybot, l.bbox.xtop, l.bbox.ytop,
                    l.position,
                    l.text.c_str())

    # 4. Subcell Instances (Uses)
    if not cell._uses.empty():
        for u in cell._uses:
            fprintf(f, "<< use >>\n")
            fprintf(f, "use %s %s\n", u.cell_name.c_str(), u.instance_name.c_str())
            fprintf(f, "transform %d %d %d %d %d %d\n",
                    u.transform.a, u.transform.b, u.transform.c,
                    u.transform.d, u.transform.e, u.transform.f)
            # Mandatory placeholder box for Magic instance bounding box positioning
            fprintf(f, "box 0 0 0 0\n")

    # 5. File End
    fprintf(f, "<< end >>\n")
    fclose(f)

def write_database_to_directory(MagicDatabase db, str output_dir):
    """Exports all cells in the database into individual .mag files inside output_dir."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    for cell_name, cell in db.cells.items():
        filepath = os.path.join(output_dir, f"{cell_name}.mag")
        write_cell_to_mag(cell, filepath)
