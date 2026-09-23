import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("post-amp/post_amplifier.mag", db)

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('post_amplifier')

#print(t)

p = db.getCellPins('post_amplifier')

#print(p)

#print(p['self']['VDD'].centroid())

top = db.getCell('post_amplifier')


# Route design

# Route inputs

routes_inp = [('XM1', 'VLAT_PLUS'), ('XM2', 'VLAT_MINUS')]

for tr, prt in routes_inp:

    a = t['children'][tr]['self'][0].gates[0]
    b = p['self'][prt].centroid()

    print(a)
    print(b)

    r = Router.Router(db, "post_amplifier")

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('s', b[1], 40)
    r.routeTo('w', b[0],  40)

    top.addRect('metal1', p['self'][prt].r.xbot, p['self'][prt].r.ybot, p['self'][prt].r.xtop, p['self'][prt].r.ytop)

# Route gates of XM7 and XM8 together

a = t['children']['XM7']['self'][0].gates[0]
b = t['children']['XM8']['self'][0].gates[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('n', b[1], 40)




top.dump()

top.writeMagFile(db, "post-amp/post_amplifier_routed.mag")

