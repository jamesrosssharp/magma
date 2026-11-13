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

print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('1bit_am')

print(cap)

p = db.getCellPins('1bit_am')

#print(p)

top = db.getCell('1bit_am')

r = Router.Router(db, "1bit_am")

top.writeMagFile(db, "1bit_am/1bit_am_routed.mag")
