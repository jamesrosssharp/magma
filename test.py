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

print(t)

cx = t['children']['fet_0']['fet'][0].gates[1][0]
cy = t['children']['fet_0']['fet'][0].gates[1][1]

dx = t['children']['fet_1']['fet'][0].gates[1][0]
dy = t['children']['fet_1']['fet'][0].gates[1][1]

cx2 = t['children']['fet_0']['fet'][0].gates[0][0]
cy2 = t['children']['fet_0']['fet'][0].gates[0][1]

dx2 = t['children']['fet_1']['fet'][0].gates[0][0]
dy2 = t['children']['fet_1']['fet'][0].gates[0][1]

sx = t['children']['fet_0']['fet'][0].source_drains[0][0]
sy = t['children']['fet_0']['fet'][0].source_drains[0][1]

sx2 = t['children']['fet_1']['fet'][0].source_drains[1][0]
sy2 = t['children']['fet_1']['fet'][0].source_drains[1][1]



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

r.begin(sx - 40, sy, 'metal1')
r.route('w', 80, 80)
r.via('metal2', 60, 60)
r.route('s', 200, 100)
r.route('e', 644, 100)
r.route('n', 200, 100)
r.via('metal1', 60, 60)
r.routeTo('w', sx2 + 40, 80)

top.dump()

top.writeMagFile(db, "magic/top_routed.mag")


