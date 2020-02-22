#!/usr/bin/python

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = self.fname + self.lname + '@gmail.com'
        self.pay = pay
        self.raise_amt = 1.04

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
        return self.pay

class Developer(Employee):
    pass


if __name__ == "__main__":
    emp1 = Employee("Joe", "Smith", 50000)
    emp2 = Employee("Black", "Pony", 80000)

    print(emp1.email)
    print(emp2.full_name())
    print(emp2.apply_raise())