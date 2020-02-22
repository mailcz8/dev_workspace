from factory import ShapeFactory

f = ShapeFactory()
s = f.getShape('Square')
print(s, s.draw())

from command import Screen, ScreenInvoker, CutCommand, PasteCommand
test_data = "Hello world"
x = Screen(test_data)
re = x.__str__()
# print(re)

cut = CutCommand(x, start=5, end=11)
client = ScreenInvoker()
client.store_and_execute(cut)
re = x.__str__()
print(re)

from observer import Obserable, AmericanStockMarket, EuropeanStockMarket
really_big_company = Obserable()
american_observer = AmericanStockMarket()
really_big_company.register(american_observer)
european_observer = EuropeanStockMarket()
really_big_company.register(european_observer)
really_big_company.update_observers('important_update', msg='CEO unexpectedly resigns!')