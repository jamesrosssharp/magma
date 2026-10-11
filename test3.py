import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router

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
g = t['children']['XM11']['self'][0].source_drains[0]
h = t['children']['XM11']['self'][1].source_drains[1]
 
 
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

# Route VSS

prt = p['self']['VSS'].centroid()
a = t['children']['XM3']['self'][0].source_drains[1]

r.begin(prt[0], prt[1], 'metal1')
r.push()
r.route('n', 170, 100)
r.via('locali', 60, 60)
r.pop()

r.routeTo('n', a[1], 100)

# 1004, -3320 ), (  3282, -3062

top.addRect('locali', 1000, -3320, 3280, -3060)

#1756, -500  ), (  2416,  208 
top.addRect('locali', 1756, -500, 2416, 208)

top.addRect('locali', 906,  180, 3258,  374)

top.dump()

top.writeMagFile(db, "strong-arm/strong_arm_latch_routed.mag")

