import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase

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

top = db.getCell('top')

top.addRect('metal1', cx - 40, cy - 100, cx + 40, cy + 40)

top.dump()

top.writeMagFile(db, "magic/top_routed.mag")
