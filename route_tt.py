import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("tt/tt_um_jamesrosssharp_high_speed_comp_master.mag", db, "~/.ciel/sky130A")

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(t)

db.findAllResistors()

res = db.getCellResistors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(cap)

p = db.getCellPins('tt_um_jamesrosssharp_high_speed_comp_master')

#print(p)

top = db.getCell('tt_um_jamesrosssharp_high_speed_comp_master')

r = Router.Router(db, "tt_um_jamesrosssharp_high_speed_comp_master")

# Route VDD and VSS to x1 (1bit am) and x11 (comparator)

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

# Power stripes

for v, vv in [('VPWR', 'VDPWR'), ('VGND', 'VGND')]:

    a = p['children']['x18']['self'][v].centroid()
    b = p['children']['x10']['self'][v].centroid()
    c = p['self'][vv].centroid()

    # Metal 1 stripe
    r.begin(a[0], a[1], 'metal1')
    r.routeTo('e', b[0], 80)

    # Locali body bias
    r.begin(a[0], a[1], 'locali')
    for i in range(0, 7):
        r.route('w', (a[0] - b[0]) / 7, 34)
        r.push()
        r.viaExpansion('metal1', 34, 34, 34, 34, 80, 80)
        r.pop()


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

# Route analog pins

a = p['self']['ua[0]'].centroid()
b = p['children']['x11']['self']['VINP'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0], 100)

a = p['self']['ua[1]'].centroid()
b = p['children']['x11']['self']['VINN'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('n', b[1] - 3500, 100)
r.routeTo('e', b[0] + 1000, 100)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0], 100)

# Route analog pins to 1bit AM fronted

a = p['self']['ua[0]'].centroid()
b = p['children']['x1']['self']['VIN'].centroid()

r.begin(a[0], a[1], 'metal4')
r.route('n', 1500, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0] + 1000, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

a = p['self']['ua[1]'].centroid()
b = p['children']['x1']['self']['VIN_MINUS'].centroid()

r.begin(a[0], a[1], 'metal4')
r.route('n', 1100, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0] + 800, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route x1.PWM_IN

a = p['children']['x1']['self']['PWM_IN'].centroid()
b = p['self']['ui_in[0]'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 1000, 100)
r.routeTo('n', b[1] - 2000, 100) 
r.routeTo('e', b[0], 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)

# Route x1.CLK

a = p['children']['x1']['self']['CLK'].centroid()
b = p['children']['x18']['self']['X'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 800, 100)
r.routeTo('n', b[1] - 800, 100) 
r.routeTo('e', b[0] + 50, 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1] + 50, 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x1.VOUT

a = p['children']['x1']['self']['VOUT'].centroid()
b = p['children']['x22']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 600, 100)
r.routeTo('n', b[1] - 500, 100) 
r.routeTo('e', b[0], 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x22.X to uo_out[0]

a = p['children']['x22']['self']['X'].centroid()
b = p['self']['uo_out[0]'].centroid()

r.begin(a[0], a[1], 'locali')
r.viaExpansion('metal1', 34, 34, 34, 34, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.route('n', 50, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

# Route x11.CLK to x1.CLK
a = p['children']['x11']['self']['CLK'].centroid()
b = p['children']['x1']['self']['CLK'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 3200, 100)
r.route('n', b[1] - 9000, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route x11.COMP_OUT to x21.A

a = p['children']['x11']['self']['COMP_OUT'].centroid()
b = p['children']['x21']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 1650, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1] - 300, 100)
r.routeTo('w', b[0], 100)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x21.X to uo_out[1]

a = p['children']['x21']['self']['X'].centroid()
b = p['self']['uo_out[1]'].centroid()

r.begin(a[0], a[1], 'locali')
r.viaExpansion('metal1', 34, 34, 34, 34, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.route('n', 50, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

# Route clock input to x18.A

a = p['self']['clk'].centroid()
b = p['children']['x18']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('s', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

top.writeMagFile(db, "tt/tt_um_jamesrosssharp_high_speed_comp.mag")
