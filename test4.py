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
c = p['children']['x9']['self']['VPWR'].centroid()
d = p['children']['x1']['self']['VDD'].centroid()

mw1 = 400

r.begin  (a[0], a[1], "metal1")
r.routeTo('s',  c[1],  mw1)
r.push()
r.routeTo('e',  c[0], 100)
r.pop()
r.routeTo('s',  b[1],  mw1)
r.push()
r.routeTo('e',  b[0],  200)
r.pop()
r.routeTo('s',  d[1],  mw1)
r.routeTo('e',  d[0],  200)

# Route VSS

# 1. Route digital

a = p['self']['VSS'].centroid()
b = p['children']['x8']['self']['VGND'].centroid()
c = p['children']['x2']['self']['VSS'].centroid()
d = p['children']['x1']['self']['VSS'].centroid()

mw1 = 400

r.begin  (a[0], a[1], "metal1")
r.routeTo('s',  b[1],  mw1)
r.push()
r.routeTo('w',  b[0],  100)
r.pop()
r.routeTo('s',  c[1] - 300,  mw1)
r.push()
r.via('metal2', 60, 60)
r.routeTo('w', c[0], 200)
r.via('metal1', 60, 60)
r.routeTo('n', c[1], 100)
r.pop()
r.routeTo('s', d[1] - 200, mw1)
r.via('metal2', 60, 60)
r.routeTo('w', d[0], 200)
r.via('metal1', 60, 60)
r.routeTo('n', d[1], 100)

top.writeMagFile(db, "high_speed_comp/high_speed_comp_top_routed.mag")

