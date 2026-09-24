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

rwidth_metal1 = 40

# Route inputs

routes_inp = [('XM1', 'VLAT_PLUS'), ('XM2', 'VLAT_MINUS')]

for tr, prt in routes_inp:

    a = t['children'][tr]['self'][0].gates[0]
    b = p['self'][prt].centroid()

    print(a)
    print(b)

    r = Router.Router(db, "post_amplifier")

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('s', b[1], rwidth_metal1)
    r.routeTo('w', b[0],  rwidth_metal1)

    top.addRect('metal1', p['self'][prt].r.xbot, p['self'][prt].r.ybot, p['self'][prt].r.xtop, p['self'][prt].r.ytop)

# Route gates of XM7 and XM8 together

a = t['children']['XM7']['self'][0].gates[0]
b = t['children']['XM8']['self'][0].gates[0]

r.begin(a[0], a[1], 'metal1')
r.routeTo('n', b[1], rwidth_metal1)

# Route drain of XM8 and drain of XM7 to pin VOUT

a = t['children']['XM7']['self'][0].source_drains[1]
b = t['children']['XM8']['self'][0].source_drains[1]
c = p['self']['VOUT'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 80, rwidth_metal1)
r.routeTo('s', c[1], rwidth_metal1)
r.push()
r.routeTo('e', c[0], rwidth_metal1)
r.pop()
r.routeTo('s', b[1], rwidth_metal1)
r.routeTo('w', b[0], rwidth_metal1)

# Route drains of XM5 and XM2 to gates of XM8 and XM7

a = t['children']['XM7']['self'][0].gates[0]
b = t['children']['XM8']['self'][0].gates[0]
c = t['children']['XM5']['self'][0].source_drains[1]
d = t['children']['XM2']['self'][0].source_drains[1]

r.begin(c[0], c[1], 'metal1')
r.route('e', 80, rwidth_metal1)
r.routeTo('s', (c[1] + d[1]) // 2, rwidth_metal1)
r.push()
r.routeTo('e', a[0], rwidth_metal1)
r.pop()
r.routeTo('s', d[1], rwidth_metal1)
r.routeTo('w', d[0], rwidth_metal1)

# Connect gates of XM5,XM2 and XM4,XM1 together

tr = [('XM5', 'XM2'), ('XM4', 'XM1')]

for ta, tb in tr:
    a = t['children'][ta]['self'][0].gates[0]
    b = t['children'][tb]['self'][0].gates[0]

    r.begin(a[0], a[1] - 40, 'metal1')
    r.route('s', 80, 80)
    r.via('metal2', 60, 60)
    r.routeTo('s', b[1] - 80, 100)
    r.via('metal1', 60, 60)
    r.routeTo('n', b[1] - 40, 80) 


# Add pad to label
prt = 'VOUT'
top.addRect('metal1', p['self'][prt].r.xbot, p['self'][prt].r.ybot, p['self'][prt].r.xtop, p['self'][prt].r.ytop)

top.dump()

top.writeMagFile(db, "post-amp/post_amplifier_routed.mag")

