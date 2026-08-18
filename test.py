import MagParser
import MagDatabase

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("magic/fet.mag", db)
