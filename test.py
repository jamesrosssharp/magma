import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("magic/top.mag", db)

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('top')

#print(t[0])

print(t[0].gates[0])

cx = t[0].gates[1][0]
cy = t[0].gates[1][1]

dx = t[1].gates[1][0]
dy = t[1].gates[1][1]

cx2 = t[0].gates[0][0]
cy2 = t[0].gates[0][1]

dx2 = t[1].gates[0][0]
dy2 = t[1].gates[0][1]



top = db.getCell('top')

#top.addRect('metal1', cx - 40, cy - 100, cx + 40, cy + 10)

r = Router.Router(db, "top")

r.begin(cx, cy, 'metal1')
r.route('s', 100, 40)
r.route('e', dx - cx,  60)
r.route('n', 100, 40)

r.begin(cx2, cy2, 'metal1')
r.route('n', 100, 40)
r.route('e', dx2 - cx2,  60)
r.route('s', 100, 40)


top.dump()

top.writeMagFile(db, "magic/top_routed.mag")


