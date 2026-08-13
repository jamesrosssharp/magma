from mag_parser import MagParser

parser = MagParser()

layers = parser.load("magic/top.mag")

print(layers)
