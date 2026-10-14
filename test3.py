import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("strong-arm/strong_arm_latch.mag", db)

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('strong_arm_latch')

print(t)

p = db.getCellPins('strong_arm_latch')

print(p)

top = db.getCell('strong_arm_latch')

r = Router.Router(db, "strong_arm_latch")

# Route clock line

tr = [('XM9', 'XM8'), ('XM10', 'XM11')]

for tt in tr:

    a = t['children'][tt[0]]['self'][1].gates[0]
    b = t['children'][tt[1]]['self'][1].gates[0]

    m1w = 80
    m2w = 100
    vw = 60

    r.begin(a[0], a[1] +  m1w / 4, 'metal1')
    r.route('e', 0, m1w)
    r.via('metal2', vw, vw)
    r.routeTo('e', b[0], m2w)
    r.via('metal1', vw, vw)
    r.route('e', 0, m1w)

prt = p['self']['CLK'].centroid()
a = t['children']['XM9']['self'][0].gates[0]
b = t['children']['XM11']['self'][0].gates[0]

r.begin(prt[0], prt[1], 'metal1')
r.routeTo('s', a[1] - 20, 80)
r.routeTo('e', a[0], 80)
r.routeTo('e', b[0], 80)


tr = [('XM8', 'XM9'), ('XM10', 'XM11')]

for tt in tr:

    a = t['children'][tt[0]]['self'][1].gates[0]
    b = t['children'][tt[1]]['self'][1].gates[0]
    c = t['children'][tt[0]]['self'][0].gates[0]
    d = t['children'][tt[1]]['self'][0].gates[0]

    r.begin(a[0] + (b[0] - a[0])*2//3, a[1], 'metal2')
    r.routeTo('s', c[1] - 20, 100)
    r.via('metal1', 60, 60)

# Route VDD

prt = p['self']['VDD'].centroid()
a = t['children']['XM9']['self'][0].source_drains[0]
b = t['children']['XM9']['self'][1].source_drains[1]
c = t['children']['XM8']['self'][0].source_drains[0]
d = t['children']['XM8']['self'][1].source_drains[1]
e = t['children']['XM10']['self'][0].source_drains[0]
f = t['children']['XM10']['self'][1].source_drains[1]
g = t['children']['XM11']['self'][1].source_drains[1]
h = t['children']['XM11']['self'][0].source_drains[0]
 
 
m1w = 80

r.begin(prt[0], prt[1], 'metal1')
r.route('n', 280, m1w)
r.routeTo('e', a[0], m1w)
r.push()
r.routeTo('s', a[1], m1w)
r.pop()
r.routeTo('e', b[0], m1w)
r.push()
r.routeTo('s', b[1], m1w)
r.pop()
r.routeTo('e', c[0], m1w)
r.push()
r.routeTo('s', c[1], m1w)
r.pop()
r.routeTo('e', d[0], m1w)
r.push()
r.routeTo('s', d[1], m1w)
r.pop()
r.routeTo('e', e[0], m1w)
r.push()
r.routeTo('s', e[1], m1w)
r.pop()
r.routeTo('e', f[0], m1w)
r.push()
r.routeTo('s', f[1], m1w)
r.pop()
r.routeTo('e', g[0], m1w)
r.push()
r.routeTo('s', g[1], m1w)
r.pop()
r.routeTo('e', h[0], m1w)
r.push()
r.routeTo('s', h[1], m1w)
r.pop()



for x in np.linspace(a[0], h[0], 8):
    print(x)
    r.begin(x, prt[1] + 280, 'metal1')
    r.via('locali', 50, 50)
        


# Route VSS

prt = p['self']['VSS'].centroid()
a = t['children']['XM3']['self'][0].source_drains[1]

r.begin(prt[0], prt[1], 'metal1')
r.push()
r.route('n', 170, 100)
r.via('locali', 50, 50)
r.pop()

r.routeTo('n', a[1], 100)

# 1004, -3320 ), (  3282, -3062

top.addRect('locali', 1000, -3320, 3280, -3060)

#1756, -500  ), (  2416,  208 
top.addRect('locali', 1756, -500, 2416, 208)

top.addRect('locali', 906,  180, 3258,  374)

# Route VINP

tr = [('VINP', 'XM1'), ('VINN', 'XM2')]

for pp, tt in tr:

    prt = p['self'][pp].centroid()
    a = t['children'][tt]['self'][0].gates[0]
    b = t['children'][tt]['self'][1].gates[0]

    m1w = 150

    r.begin(prt[0], prt[1], 'metal1')
    r.routeTo('n', a[1] - 150, m1w)
    r.push()
    r.routeTo('e', a[0], m1w)
    r.routeTo('n', a[1], m1w)
    r.pop()
    r.routeTo('w', b[0], m1w)
    r.routeTo('n', b[1], m1w)

# Route drain of XM3 to source of XM1

a = t['children']['XM1']['self'][0].source_drains[1]
b = t['children']['XM3']['self'][0].source_drains[0]

mw1 = 100

r.begin(a[0], a[1], 'metal1')
r.route('n', 650, mw1)
r.routeTo('e', b[0] - 100, mw1)
r.route('s', 260, mw1)
r.routeTo('e', b[0], mw1)
r.routeTo('s', b[1], mw1)

# Route drain of XM3 to source of XM2

a = t['children']['XM2']['self'][0].source_drains[1]
b = t['children']['XM3']['self'][1].source_drains[1]

mw1 = 100

r.begin(a[0], a[1], 'metal1')
r.route('n', 650, mw1)
r.routeTo('w', b[0] + 100, mw1)
r.route('s', 260, mw1)
r.routeTo('w', b[0], mw1)
r.routeTo('s', b[1], mw1)

# Route drains of XM1 and XM2 together

tr = ['XM1', 'XM2']

for tt in tr:
    a = t['children'][tt]['self'][0].source_drains[0]
    b = t['children'][tt]['self'][1].source_drains[1]

    mw1 = 80
    mw2 = 100
    h = 650

    r.begin(a[0], a[1], 'metal1')
    r.route('n', 0, mw1)
    r.via('metal2', 60, 60)
    r.route('n', h, mw2)
    r.routeTo('e', b[0], mw2)
    r.route('s', h, mw2)
    r.via('metal1', 60, 60)
    r.route('s', 0, mw1)

top.dump()

# Route drains of XM1 and XM2 to source of XM4 and XM5

tr = [('XM1', 'XM4', 0, 50), ('XM2', 'XM5', 1, -50)]

for tt, tt2, i, pp in tr:

    h = 650
    mw1 = 80
    mw2 = 100

    a = t['children'][tt]['self'][0].source_drains[0]
    b = t['children'][tt]['self'][1].source_drains[1]
    c = t['children'][tt2]['self'][0].source_drains[i]
 
    r.begin((a[0]+b[0])/2, a[1] + h, 'metal2')
    r.route('n', 250, mw2)
    r.via('metal1', 60, 60)
    r.routeTo('n', c[1], mw1)
    r.routeTo('w', c[0] - pp, mw1)

# Route gate of XM4 to drain of XM5

a   = t['children']['XM4']['self'][0].gates[0]
b   = t['children']['XM5']['self'][0].source_drains[0]
prt = p['self']['VOUT_MINUS'].centroid()

mw1 = 60

r.begin(a[0], a[1] - 40, 'metal1')
r.route('s', 120, mw1)
r.routeTo('e', b[0], mw1)
#r.route('n', 20, mw1)
r.push()
r.routeTo('n', b[1], mw1)
r.pop()
r.route('e', 170, mw1)
r.route('n', 130, mw1)
r.routeTo('e', prt[0] - 40, mw1)
r.routeTo('n', prt[1], mw1)

top.writeMagFile(db, "strong-arm/strong_arm_latch_routed.mag")

