import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("high_speed_comp/high_speed_comp_top.mag", db, "~/.ciel/sky130A")

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

mw1 = 800

r.begin  (a[0], a[1], "metal1")
r.routeTo('s',  c[1],  mw1)
r.push()
r.routeTo('e',  c[0], 250)
r.pop()
r.routeTo('s',  b[1],  mw1)
r.push()
r.routeTo('e',  b[0],  300)
r.pop()
r.routeTo('s',  d[1],  mw1)
r.routeTo('e',  d[0],  300)

# Route VSS

# 1. Route digital

a = p['self']['VSS'].centroid()
b = p['children']['x8']['self']['VGND'].centroid()
c = p['children']['x2']['self']['VSS'].centroid()
d = p['children']['x1']['self']['VSS'].centroid()

mw1 = 800

r.begin  (a[0], a[1], "metal1")
r.routeTo('s',  b[1],  mw1)
r.push()
r.routeTo('w',  b[0],  300)
r.pop()
r.routeTo('s',  c[1] - 300,  mw1)
r.push()
r.via('metal2', 120, 120)
r.routeTo('w', c[0], 300)
r.via('metal1', 120, 120)
r.routeTo('n', c[1], 200)
r.pop()
r.routeTo('s', d[1] - 200, mw1)
r.via('metal2', 120, 120)
r.routeTo('w', d[0], 300)
r.via('metal1', 120, 120)
r.routeTo('n', d[1], 200)


# Route comp out

a = p['self']['COMP_OUT'].centroid()
b = p['children']['x3']['self']['Q'].centroid()

r.begin(a[0],a[1],'metal1')
r.route('s', 200, 80)
r.via('metal2', 55, 55)
r.routeTo('s', b[1] + 20, 100)
r.routeTo('e', b[0], 100)
r.via('metal1', 52, 52)
r.route('n', 0, 64)
r.via('locali', 38, 38)

# Route x.2 vout to x3.D

a = p['children']['x2']['self']['VOUT'].centroid()
b = p['children']['x3']['self']['D'].centroid()

mw1 = 100

r.begin(a[0], a[1], 'metal1')
r.routeTo('n', (a[1] + b[1]) / 2, mw1)
r.routeTo('w', b[0], mw1)
r.route('n', 400, mw1)
r.via('metal2', 55, 55)
r.routeTo('n', b[1] - 20, mw1)
r.via('metal1', 52, 52)
r.route('n', 0, 64)
r.via('locali', 38, 38)
r.routeTo('n', b[1], 42)

# Route CLK to x3 CLK and x4 A

a = p['self']['CLK'].centroid()
b = p['children']['x3']['self']['CLK'].centroid()
c = p['children']['x4']['self']['A'].centroid()


r.begin(a[0], a[1], 'metal1')
r.route('s', 200, 100)
r.push()
r.via('locali', 60, 60)
r.routeTo('w', b[0], 80)
r.via('metal1', 60, 60)
r.route('n', 0, 100)
r.via('metal2', 60, 60)
r.routeTo('s', b[1] + 20, 100)
r.via('metal1', 52, 52)
r.route('n', 0, 64)
r.via('locali', 38, 38)
r.routeTo('s', b[1], 42)
r.pop()
r.via('metal2', 60, 60)
r.routeTo('s', c[1], 80)
r.routeTo('e', c[0], 80)
r.via('metal1', 52, 52)
r.route('n', 0, 64)
r.via('locali', 38, 38)

# Route x4 Y to x1 CLK PRIME

a = p['children']['x1']['self']['CLK'].centroid()
b = p['children']['x4']['self']['Y'].centroid()

r.begin(a[0], a[1], 'metal3')
r.via('metal4', 60, 60)
r.route('n',a[1] + (b[1] - a[1])*19//20, 300)
r.routeTo('e', b[0], 300)
r.routeTo('n', b[1] - 400, 300)
r.via('metal3', 120, 120)
r.route('n', 0, 150)
r.via('metal2', 80, 80)
r.route('n', 0, 100)
r.via('metal1', 52, 52)
r.routeTo('n', b[1], 150)
r.route('n', 0, 64)
r.via('locali', 38, 38)

# Connect x1 VOUT_MINUS to x2 VLAT_MINUS

a = p['children']['x1']['self']['VOUT_MINUS'].centroid()
b = p['children']['x2']['self']['VLAT_MINUS'].centroid()

r.begin(a[0], a[1], 'metal1')
r.via('metal2', 60, 60)
r.route('n', 0, 100)
r.via('metal3', 80, 80)
r.routeTo('n', b[1], 120)
r.routeTo('w', b[0], 120)
r.via('metal2', 80, 80)
r.route('n', 0, 100)
r.via('metal1', 60, 60)

# Connect x1 VOUT_PLUS to x2 VLAT_PLUS

a = p['children']['x1']['self']['VOUT_PLUS'].centroid()
b = p['children']['x2']['self']['VLAT_PLUS'].centroid()

r.begin(a[0], a[1], 'metal1')
r.via('metal2', 60, 60)
r.route('n', 0, 100)
r.via('metal3', 80, 80)
r.routeTo('n', b[1], 120)
r.routeTo('e', b[0], 120)
r.via('metal2', 80, 80)
r.route('n', 0, 100)
r.via('metal1', 60, 60)

# Route power stripes for digital

a = p['children']['x9']['self']['VPWR'].centroid()
b = p['children']['x8']['self']['VPWR'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 100)

a = p['children']['x9']['self']['VGND'].centroid()
b = p['children']['x8']['self']['VGND'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 100)

a = p['children']['x3']['self']['VPB'].centroid()
b = p['children']['x7']['self']['VPB'].centroid()

edge = 100

r.begin(a[0] - edge, a[1], 'locali')
r.routeTo('e', b[0] + 280, 32)

a = p['children']['x3']['self']['VNB'].centroid()
b = p['children']['x7']['self']['VNB'].centroid()

r.begin(a[0] - edge, a[1], 'locali')
r.routeTo('e', b[0] + 280, 32)


top.writeMagFile(db, "high_speed_comp/high_speed_comp_top_routed.mag")
