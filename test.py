import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("magic/top.mag", db)

#db.dump()

db.findAllTransistors()

db.dumpCellTransistors('top')
