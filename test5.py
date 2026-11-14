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


top.writeMagFile(db, "1bit_am/1bit_am_routed.mag")
