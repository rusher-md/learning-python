# What is self
# Difference between instance attribute and class attribute
# Difference between class method and instance method
# What is super() function
# How to call one class inside another class

# Self

# Self represents the instance of the class.
# By using the “self”  we can access the attributes and methods of the class in Python.
# It binds the attributes with the given arguments.
# The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes
# Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically,
# But not received automatically: the first parameter of methods is the instance the method is called on

class Mynumber:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


obj1 = Mynumber(17)
obj1.print_value()

# Difference between instance attribute and class attribute

# class Attribute

# Unlike class attributes, instance attributes are not shared by objects.
# Every object has its own copy of the instance attribute (In case of class attributes all object refer to single copy).
#  vars()– This function displays the attribute of an instance in the form of an dictionary.
# dir()– This function displays more attributes than vars function,as it is not limited to instance


class Emp:
    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000

    def show(self):
        print(self.name)
        print(self.salary)


e1 = Emp()
print("Dictionary form :", vars(e1))
print(dir(e1))

# Difference between class method and instance method
# A class method is a method that is bound to a class rather than its object.
# It doesn't require creation of a class instance


class MyClass(object):
    @staticmethod
    def class_method(cls):
        return 'class method called', cls

    def my_display(self):
        print(self)

    def sum_num(self, num1, num2):
        print(num1 + num2)


myClass2 = MyClass()
myClass2.my_display()
myClass2.sum_num(1, 2)
# instance method
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by its class) for modifying its state.


class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Hamza')
p.say_hi()

# What is super() function
# In Python, the super() function is used to refer to the parent class or superclass
# It allows you to call methods defined in the superclass from the subclass
# Enabling you to extend and customize the functionality inherited from the parent class.


class Empty(object):
    def __init__(self, number, name, add):
        self.number = number
        self.name = name
        self.add = add


class Full(Empty):
    def __init__(self, number, name, add, emails):
        super().__init__(number, name, add)
        self.emails = emails


Empty1 = Full(773, 'Hamza', 'Lucknow', 'mh896299@gamil.com')
print('The number is:', Empty1.number)
print('The Name is:', Empty1.name)
print('The Address is:', Empty1.add)
print('The Emails is:', Empty1.emails)

# How to call one class inside another class


class InnerClass(object):
    def _init_(self):
        self.inner_var = 10


class OuterClass():
    def _init_(self, outer_var):
        self.outer_var = outer_var
        self.inner_instance = InnerClass()

    def display(self):
        print("Outer variable:", self.outer_var)
        print("Inner variable from inner instance:", self.inner_instance.inner_var)


outer_instance = OuterClass()
outer_instance.display()
