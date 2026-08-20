import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("magic/fet.mag", db)

db.dump()

db.findAllTransistors()
