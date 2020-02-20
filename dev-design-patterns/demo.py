from factory import ShapeFactory

f = ShapeFactory()
s = f.getShape('Square')
print(s)
print(s.draw())

