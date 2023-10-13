# Python program to illustrate functions can be treated as objects 
def shout(text): 
	return text.upper()

yell = shout 

print(yell('Hello'))

# ===============================xxxxxx======================================
# Python program to illustrate functions 
# can be passed as arguments to other functions

def add_10(num):
	return num+10

def sub_10(num):
	return num-10

def operate(func):
	operation = func(20)
	print(operation)

operate(add_10)
operate(sub_10)

# ===============================xxxxxx======================================
# Functions can return another function

def create_text_processor(text1):
	def text_processor(text2):
		return text2+text1
	
	return text_processor

add_test = create_text_processor('test')

print(add_test('new'))

# ===============================xxxxxx======================================

# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

# ===============================xxxxxx======================================
# importing libraries
import time
import math
 
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 
 
 
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
 
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
 
# calling the function.
factorial(10)

# ===============================xxxxxx======================================
# how to preserve metadata of a decorator
# import time
# from functools import wraps

from functools import wraps
from inspect import signature
import time

def calculate_chars(func):
	'''Decorator that reports the execution time.'''
	@wraps(func)
	def wrapper_fn(*args, **kwargs)-> None:
		'''It is a wrapper func inside a decorator'''
		result = func(*args, **kwargs)
		return {"Total chars":len(result), "result":result}
	
	return wrapper_fn

@calculate_chars
def print_hello(text)-> str:
	'''prints something'''
	# print('Hello worlds')
	return text
	

x = print_hello('total chars ')
print(x, type(x))
print(print_hello.__name__)
print(print_hello.__doc__)
print(print_hello.__annotations__)
print(signature(print_hello))
print_hello.__wrapped__()
print(print_hello.__module__)
# ===============================xxxxxx======================================
