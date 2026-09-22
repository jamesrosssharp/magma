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

print(t)

top = db.getCell('post_amplifier')

top.dump()

top.writeMagFile(db, "post-amp/post_amplifier_routed.mag")

