import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("tt/tt_um_jamesrosssharp_high_speed_comp.mag", db, "~/.ciel/sky130A")

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('tt_um_jamesrosssharp_high_speed_comp')

#print(t)

db.findAllResistors()

res = db.getCellResistors('tt_um_jamesrosssharp_high_speed_comp')

#print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('tt_um_jamesrosssharp_high_speed_comp')

#print(cap)

p = db.getCellPins('tt_um_jamesrosssharp_high_speed_comp')

#print(p)

top = db.getCell('tt_um_jamesrosssharp_high_speed_comp')

r = Router.Router(db, "tt_um_jamesrosssharp_high_speed_comp")

for cell in ['x1', 'x11']:

    vv = [('VDPWR', 'VDD'), ('VGND', 'VSS')]

    for vvv, vvvv in vv:

        a = p['children'][cell]['self'][vvvv].centroid()
        b = p['self'][vvv].centroid()

        r.begin(a[0], a[1], 'metal1')
        r.viaExpansion('metal2', 200,200,240,240,240,240)
        r.viaExpansion('metal3', 200,200,240,240,600,600)
        r.routeTo('w', b[0], 600)
        r.viaExpansion('metal4', 540, 540, 600, 600, 600, 600)

for v, vv in [('VPWR', 'VDPWR'), ('VGND', 'VGND')]:

    a = p['children']['x18']['self'][v].centroid()
    b = p['children']['x10']['self'][v].centroid()
    c = p['self'][vv].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('e', b[0], 80)

    r.begin(a[0], a[1], 'metal3')
    for i in range(0, 10):
        r.route('w', (a[0] - b[0]) / 10, 200)
        r.push()
        r.viaExpansion('metal2', 120, 120, 200, 200, 140, 140)
        r.viaExpansion('metal1', 60, 60, 140, 140, 80, 80)
        r.pop()
    r.routeTo('w', c[0], 200)
    if v == 'VPWR':
        r.route('s', 400, 200)
    r.viaExpansion('metal4', 200, 200, 240, 240, 400, 400)


top.writeMagFile(db, "tt/tt_um_jamesrosssharp_high_speed_comp_routed.mag")
