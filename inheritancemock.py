# Constructor with 3 instance attributes
# 2 instance methods Display() and getSum()
# getSum() will return the sum of two floating numbers
# Display() will display the result of the sum of two floating numbers
# Create a child of Operation() with name as Calc()
# Create a function subs() inside Calc() that will subtract 10 from a given value.

class Operation(object):

    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

    def Display(self):
        print(self.name)

    def getsum(self, num1, num2):
        sum1 = num1 + num2
        return sum1


class Calc(Operation):

    def subs(self, value):
        print(value-10)


obj1 = Operation('name', 'address', 'location')
obj2 = Calc('name', 'address', 'location')

print(obj2.getsum(2.0, 3.0))
obj2.subs(90)




