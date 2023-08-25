#
# Add 3 instance variables name, age, and balance.
# Add User() class which is child of bank class .
# Add functions to User() class.
# add money
# withdraw money
# check balance
# transfer account

class Bank(object):

    def __init__(self, name, age, balance,):
        self.name = name
        self.age = age
        self.balance = balance

    def display(self):
        print(self.name)

    def display2(self):
        print(self.age)

    def display3(self):
        print(self.balance)

    @staticmethod
    def display4(num1):
        print(num1)


class User(Bank):

    def addmoney(self):
        print(12300)

    def withdraw(self):
        print(5000)

    def check_balance(self):
        print(1000000)

    def transferaccount(self):
        print(897899)


bank1 = Bank('name', 'age', 'balance', )
bank2 = User('add money', 'withdraw money', 'check balance',)
print(bank1.name)
bank2.addmoney()

import math


class Shape(object):

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4*self.side


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def area(self):
        return 0.5 * self.side * self.height

    def perimeter(self):
        return 3 * self.side


Circle1 = Circle(12)
Square1 = Square(26)
Triangle1 = Triangle(5, 7)

print(Circle1.area(), Square1.perimeter(), Triangle1.perimeter())

Bank1 = Bank(12, 32, 44)
Bank1.display4(1)


