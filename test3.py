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


top.dump()

top.writeMagFile(db, "strong-arm/strong_arm_latch_routed.mag")

