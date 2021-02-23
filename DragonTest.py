from DragonGame import Dragon
x = Dragon("Grzegorz")
assert x.level == 0
assert x.level != 1
assert x.name == "Grzegorz" 
assert x.name != "Stefan"
assert str(x) == "name: Grzegorz, level: 0"
x.feed()
Dragon.feed(x)
assert x.level != 0
assert x.level == 2
x.save("Grzegorz.sv")
y = Dragon.load("Grzegorz.sv")
assert isinstance(y, Dragon)
assert y.name == "Grzegorz"
assert y.level == 2
