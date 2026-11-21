import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("3bit-flash-converter/flash_converter.mag", db, "~/.ciel/sky130A")

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('flash_converter')

#print(t)

db.findAllResistors()

res = db.getCellResistors('flash_converter')

#print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('flash_converter')

#print(cap)

p = db.getCellPins('flash_converter')

#print(p)

top = db.getCell('flash_converter')

r = Router.Router(db, "flash_converter")

# Route all outputs in metal1

for i in range(1,9):
    cell = f"x{i}"
    pin = f"O{i - 1}"

    a = p['children'][cell]['self']['COMP_OUT'].centroid()
    b = p['self'][pin].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.route('e', 300 + (abs(4-i))*250, 100)
    r.routeTo('s', b[1], 100)
    r.routeTo('w', b[0], 100)

    # Route clock tree
    a = p['self']['CLK'].centroid()
    b = p['children'][cell]['self']['CLK'].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.route('w', 600, 100)
    r.routeTo('s', b[1], 100)
    r.routeTo('w', b[0], 100)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

    # Route VINP
    a = p['self']['VIN'].centroid()
    b = p['children'][cell]['self']['VINP'].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
    r.route('e', 300, 100)
    r.routeTo('s', b[1], 100)
    r.routeTo('e', b[0] - 500, 100)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.routeTo('e', b[0], 100)

    arr = [0, 1, 2, 3, 4, 4, 3, 2, 1]

    # Route VINN
    a = res['children'][f'XR{i}']['self'][0].contacts[1]
    b = p['children'][cell]['self']['VINN'].centroid()
    r.begin(a[0], a[1], 'metal1')
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.route('e', 300 + arr[i]*250, 100)
    r.routeTo('s', b[1], 100)
    r.routeTo('e', b[0] - 500, 100)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.routeTo('e', b[0], 100)



# VDD stripes 

stripe_w = 500
via_w = 400

r.begin(11200, 20600, 'metal1')
r.viaExpansion('metal2', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
r.viaExpansion('metal3', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
r.viaExpansion('metal4', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
for i in range(0, 4):
    r.route('s', 8400, stripe_w)
    r.push()
    r.viaExpansion('metal3', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.viaExpansion('metal2', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.viaExpansion('metal1', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.pop()

# VSS stripes

r.begin(12000, 20600 - 4200, 'metal1')
r.viaExpansion('metal2', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
r.viaExpansion('metal3', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
r.viaExpansion('metal4', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
for i in range(0, 3):
    r.route('s', 8400, stripe_w)
    r.push()
    r.viaExpansion('metal3', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.viaExpansion('metal2', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.viaExpansion('metal1', via_w, via_w, stripe_w, stripe_w, stripe_w, stripe_w)
    r.pop()

# Route resistor chain

i = 0

for i in range(0,7):

    rr = f'XR{i+1}'
    rrr = f'XR{i+2}'

    a = res['children'][rr]['self'][0].contacts[0]
    b = res['children'][rrr]['self'][0].contacts[1]

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('n', ((a[1] + b[1]) / 2) + i*0, 100)
    r.routeTo('e', b[0], 100)
    r.routeTo('n', b[1], 100)

    i += 1

# Route RES_TOP

a = p['self']['RES_TOP'].centroid()
b = res['children']['XR1']['self'][0].contacts[1]

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 100)
r.routeTo('s', b[1], 100)

# Route RES_OUT

a = p['self']['RES_OUT'].centroid()
b = res['children']['XR8']['self'][0].contacts[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('s', b[1] - 300, 100)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)


top.writeMagFile(db, "3bit-flash-converter/flash_converter_routed.mag")
