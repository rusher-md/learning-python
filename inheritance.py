class Vehicle(object):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Car(Vehicle):

    def display2(self):
        print(self.name)


class Bike(Vehicle):

    def display3(self):
        print(self.name)


Car1 = Car('toyota')
Bike1 = Bike('honda')


Car1.display()
Bike1.display()









