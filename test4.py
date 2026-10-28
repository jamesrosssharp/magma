import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("high_speed_comp/high_speed_comp_top.mag", db)

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('high_speed_comp_top')

print(t)

p = db.getCellPins('high_speed_comp_top')

print(p)

top = db.getCell('high_speed_comp_top')

r = Router.Router(db, "high_speed_comp_top")

pp = ['VINP', 'VINN']

for ppp in pp:

    a = p['self'][ppp].centroid()
    b = p['children']['x1']['self'][ppp].centroid()

    mw1 = 100

    r.begin(a[0], a[1], "metal1")
    r.routeTo('w', b[0], mw1)
    r.routeTo('n', b[1], mw1)

# Route VDD

# 1. route to x2

a = p['self']['VDD'].centroid()
b = p['children']['x2']['self']['VDD'].centroid()

mw1 = 200

r.begin(a[0], a[1], "metal1")
r.routeTo('s', b[1], mw1)
r.routeTo('e', b[0], mw1)



top.writeMagFile(db, "high_speed_comp/high_speed_comp_top_routed.mag")

