from factory import ShapeFactory

f = ShapeFactory()
s = f.getShape('Square')
print(s)
print(s.draw())

from command import Screen, ScreenInvoker, CutCommand, PasteCommand
test_data = "Hello world"
x = Screen(test_data)
re = x.__str__()
print(re)

cut = CutCommand(x, start=5, end=11)
client = ScreenInvoker()
client.store_and_execute(cut)
re = x.__str__()
print(re)