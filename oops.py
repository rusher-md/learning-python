# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction

# Class is a collection of Objects

# Objects (real-world entities) 
# 1. functions/methods/behavior 2. Properties (color/speed/look)state 3. Identity is a unique name

# class

# Python3 program to
# demonstrate defining
# a class

class Car:
    def my_car(self):
        pass
    

car1 = Car()

s = str('sajhdb')

# print(type(car1))



# The Python self
# Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.

# The Python __init__ Method


class Dog:
    # class attribute
    attr1 = 'mammal'

    # instance attribute
    def __init__(self, name):
        self.name = name
    
    # instance fn or method 
    def speak(self):
        print(f"my name is {self.name}")


dog1 = Dog('tommy')
dog2 = Dog('tom')

dog1.speak()
dog2.speak()


class Subject:

    # instance attribute
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

obj = Subject('maths', 'science')
print(obj.attr1, obj.attr2)


# What is self

class check:
    
    def __init__(self):
        print("address of self :", id(self))
    
obj = check()
obj1 = check()
print(f"address of obj {id(obj)}")
print(f"address of obj {id(obj1)}")
