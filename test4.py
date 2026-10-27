import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("high_speed_comp/high_speed_comp_top.mag", db)

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('high_speed_comp_top')

print(t)

p = db.getCellPins('high_speed_comp_top')

print(p)

top = db.getCell('high_speed_comp_top')

r = Router.Router(db, "high_speed_comp_top")

top.writeMagFile(db, "high_speed_comp/high_speed_comp_top_routed.mag")

