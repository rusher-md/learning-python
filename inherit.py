# blueprint or object factory that can be used to create many objects with same definitions(properties and functions) 
class Vehicle(object):
    # constructor 
    def __init__(self, name):
        self.name = name
    
    # instance method
    def Display(self):
        print(self.name, "inside vehicle class")


# create vehicle class objects
vehicle1 = Vehicle('vehicle1 name')
vehicle2 = Vehicle('vehicle2 name')

# use instance methods of the class
vehicle1.Display()
vehicle2.Display()

# create child class from Vehicle (parent)
class Car(Vehicle):
    #instance method
    def Display(self):
        print(self.name, "inside car class")

class Bike(Vehicle):
    #instance method
    def Display(self):
        print(self.name, "inside bike class")


# create objects of child classes
car1 = Car('car1')
bike1 = Bike('bike1')

#call child class instance methods
car1.Display()
bike1.Display()
