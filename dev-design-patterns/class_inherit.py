#!/usr/bin/python

class Employee:
    raise_amt = 1.04
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = self.fname + self.lname + '@gmail.com'
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt
        return self.pay

class Developer(Employee):
    raise_amt = 1.5

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)

    # def apply_raise(self):
    #     raise_amt = 1.5
    #     self.pay = self.pay * raise_amt
    #     # return self.pay


if __name__ == "__main__":
    emp1 = Employee("Joe", "Smith", 50000)
    emp2 = Employee("Black", "Pony", 80000)
    print(emp1.email, emp2.full_name(), emp2.apply_raise())

    dev1 = Developer("Uno", "DevOne", 150000)
    dev2 = Developer("Toto", "DevTwo", 200000)

    emp1_pay, emp1_after_raise = emp1.pay, emp1.apply_raise()
    dev1_pay, dev1_after_raise = dev1.pay, dev1.apply_raise()
    print('emp1:', emp1_pay, emp1_after_raise, '; raise = ', abs(emp1_pay-emp1_after_raise))
    print('org: dev1: 150000 156000.0 ; raise =  6000.0')
    print('dev1:', dev1_pay, dev1_after_raise, '; raise = ', abs(dev1_pay-dev1_after_raise))