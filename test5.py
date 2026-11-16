import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("1bit_am/1bit_am.mag", db, "~/.ciel/sky130A")

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('1bit_am')

#print(t)

db.findAllResistors()

res = db.getCellResistors('1bit_am')

#print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('1bit_am')

#print(cap)

p = db.getCellPins('1bit_am')

#print(p)

top = db.getCell('1bit_am')

r = Router.Router(db, "1bit_am")

# Route power and ground

for vv in ['VDD', 'VSS']:

    a = p['self'][vv].centroid()
    b = p['children']['x1']['self'][vv].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('w', b[0], 600)
    r.routeTo('s', b[1], 600)

# Route clock and comparator output

for vv, vvv in [('CLK', 'CLK'), ('VOUT', 'COMP_OUT')]:
    a = p['self'][vv].centroid()
    b = p['children']['x1']['self'][vvv].centroid()

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('w', b[0], 100)
    r.routeTo('s', b[1], 100)

# Connect input bias resistors

i = 0
for rr,rrr in [('XR3', 'XR4'), ('XR4', 'XR5'), ('XR5', 'XR6')]:

    a = res['children'][rr]['self'][0].contacts[0]
    b = res['children'][rrr]['self'][0].contacts[1]

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('n', ((a[1] + b[1]) / 2) + i*200, 100)
    r.routeTo('e', b[0], 100)
    r.routeTo('n', b[1], 100)

    i += 1

# Connect VDD to input bias resistor chain

a = p['children']['x1']['self']['VDD'].centroid()
b = res['children']['XR3']['self'][0].contacts[1]

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 200)
r.routeTo('n', b[1], 200)

# Connect comparator positive input

a = p['children']['x1']['self']['VINP'].centroid()
b = res['children']['XR4']['self'][0].contacts[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0] - 600, 200)
r.routeTo('n', b[1] + 600, 200)
r.routeTo('w', b[0], 200)
r.routeTo('s', b[1], 200)

# Connect VSS to resistor chain

a = p['children']['x1']['self']['VSS'].centroid()
b = res['children']['XR6']['self'][0].contacts[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0] - 1800, 200)
r.routeTo('n', b[1] + 1200, 200)
r.routeTo('w', b[0], 200)
r.routeTo('s', b[1], 200)

# Route input mim cap

print(cap['children']['XC1']['self'])
for i in range(0, 3):
    a = cap['children']['XC1']['self'][i*4].contacts[0]
    b = cap['children']['XC1']['self'][(i+1)*4].contacts[0]
    
    fudge = 0

    r.begin(a[0] - fudge, a[1] + 200, 'metal4')
    r.route('n', 600, 108)
    r.routeTo('e', b[0] - fudge, 108)
    r.route('s', 600, 108)

for i in range(0, 3):
    a = cap['children']['XC1']['self'][i*4 + 64].contacts[1]
    b = cap['children']['XC1']['self'][(i+1)*4 + 64].contacts[1]
    
    r.begin(a[0], a[1] - 1000, 'metal4')
    r.route('s', 600, 108)
    r.routeTo('e', b[0], 108)
    r.route('n', 600, 108)

# Route vin to input cap XC1

a = p['self']['VIN'].centroid()
b = cap['children']['XC1']['self'][0].contacts[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('w', b[0], 100)
r.routeTo('n', b[1] + 800, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)

# Route input cap to resistor chain

a = cap['children']['XC1']['self'][3*4+64].contacts[1]
b = res['children']['XR4']['self'][0].contacts[0]

r.begin(a[0], a[1] - 1600, 'metal4')
r.routeTo('w', b[0], 108)
r.routeTo('s', b[1], 108)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route XC2 mim cap

for i in range(0, 3):
    a = cap['children']['XC2']['self'][i*4].contacts[0]
    b = cap['children']['XC2']['self'][(i+1)*4].contacts[0]
    
    fudge = 0

    r.begin(a[0] - fudge, a[1] + 200, 'metal4')
    r.route('n', 600, 108)
    r.routeTo('e', b[0] - fudge, 108)
    r.route('s', 600, 108)

for i in range(0, 3):
    a = cap['children']['XC2']['self'][i*4 + 64].contacts[1]
    b = cap['children']['XC2']['self'][(i+1)*4 + 64].contacts[1]
    
    r.begin(a[0], a[1] - 1000, 'metal4')
    r.route('s', 600, 108)
    r.routeTo('e', b[0], 108)
    r.route('n', 600, 108)


# Route PWM resistor

i = 0
for rr,rrr in [('XR1', 'XR7'), ('XR7', 'XR8'), ('XR8', 'XR2')]:

    a = res['children'][rr]['self'][0].contacts[0]
    b = res['children'][rrr]['self'][0].contacts[1]

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('n', ((a[1] + b[1]) / 2) + i*200, 100)
    r.routeTo('e', b[0], 100)
    r.routeTo('n', b[1], 100)

    i += 1

# Route XC2 cap to resistor chain

a = cap['children']['XC2']['self'][0].contacts[0]
b = res['children']['XR2']['self'][0].contacts[0]

r.begin(a[0], a[1] + 800, 'metal4')
r.routeTo('w', b[0], 108)
r.routeTo('n', b[1], 108)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route XR2 to VINN

a = res['children']['XR2']['self'][0].contacts[0]
b = p['children']['x1']['self']['VINN'].centroid()

r.begin(a[0], a[1], 'metal1')
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('e', b[0], 100)

# Route power stripes down to inverters

a = p['children']['x1']['self']['VDD'].centroid()
b = p['children']['x2']['self']['VPWR'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 1000, 600)
r.viaExpansion('metal2', 600, 600, 650, 650, 650, 650)
r.routeTo('w', b[0] - 600, 600)
r.routeTo('s', b[1], 600)
r.viaExpansion('metal1', 80, 80, 600, 600, 100, 100)
r.routeTo('w', b[0], 100)

a = p['children']['x1']['self']['VSS'].centroid()
b = p['children']['x4']['self']['VGND'].centroid()
c = cap['children']['XC2']['self'][3*4+64].contacts[1]

r.begin(a[0], a[1], 'metal1')
r.route('w', 1000, 600)
r.viaExpansion('metal2', 600, 600, 650, 650, 650, 650)
r.routeTo('w', b[0] + 600, 600)
r.routeTo('s', b[1], 600)
r.push()
r.viaExpansion('metal1', 80, 80, 600, 600, 100, 100)
r.routeTo('w', b[0], 100)
r.pop()
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.route('w', 200, 120)
r.viaExpansion('metal4', 80, 80, 120, 120, 108, 108)
r.routeTo('s', c[1] - 1600, 108)
r.routeTo('e', c[0], 108)

# Route PWM in to inverter chain
a = p['self']['PWM_IN'].centroid()
b = p['children']['x2']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('s', b[1] - 1000, 100)
r.routeTo('w', b[0] - 600, 100)
r.routeTo('n', b[1], 100)
r.routeTo('e', b[0], 100)
r.viaExpansion('locali', 34, 34, 100, 100, 38, 38)

a = p['children']['x2']['self']['Y'].centroid()
b = p['children']['x3']['self']['A'].centroid()

r.begin(a[0], a[1], 'locali')
r.route('e', 100, 34)
r.viaExpansion('metal1', 34, 34, 38, 38, 60, 60)
r.routeTo('e', b[0], 60)
r.viaExpansion('locali', 34, 34, 60, 60, 38, 38)

a = p['children']['x3']['self']['Y'].centroid()
b = res['children']['XR1']['self'][0].contacts[1]

r.begin(a[0], a[1], 'locali')
r.route('e', 50, 34)
r.viaExpansion('metal1', 34, 34, 34, 34, 60, 60)
r.route('e', 1000, 60)
r.routeTo('n', b[1] - 300, 60)
r.routeTo('w', b[0], 60)
r.routeTo('n', b[1], 60)


top.writeMagFile(db, "1bit_am/1bit_am_routed.mag")
