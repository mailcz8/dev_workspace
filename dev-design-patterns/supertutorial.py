#!/usr/bin/python

class Base:
    def __init__(self):
        self.base = 'Base'
        print('{}.__init__'.format(self.base))


class Child1(Base):
    def __init__(self):
        self.cur_child_info = 'Child1'
        Base.__init__(self)
        print('{}.__init__'.format(self.cur_child_info))


class Child2(Base):
    def __init__(self):
        self.cur_child_info = 'Child2'
        Base.__init__(self)
        print('{}.__init__'.format(self.cur_child_info))


class Child3(Child1, Child2):
    def __init__(self):
        Child1.__init__(self)
        Child2.__init__(self)
        print('Child3.__init__')


class Child4(Base):
    def __init__(self):
        super().__init__()
        print('Child4.__init__')


class Child5(Base):
    def __init__(self):
        super().__init__()
        print('Child5.__init__')


class Child6(Child4, Child5):
    def __init__(self):
        self.cur_child_info = 'Child6'
        super().__init__()
        print('{}.__init__'.format(self.cur_child_info))


class Ten:
    def adder(self, *args):
        print(sum(args) + 10)
        super().adder()


class Hundred:
    def adder(self, *args):
        print(sum(args) + 100)
        # super().adder()


class Experiment(Ten, Hundred):
    pass


if __name__ == "__main__":
    c3 = Child3()

    c6 = Child6()
    print(Child6.__mro__)

    e = Experiment()
    e.adder(1, 2, 3)
    print(Experiment.__mro__)