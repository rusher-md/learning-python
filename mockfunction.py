# Write a program to reverse an integer in Python.
# Python Program to find the Smallest number among three.
# Python Program to calculate the square of a given number.


# Write a program to reverse an integer in Python.

def reverse(rev1234):
    my_reverse = str(rev1234)
    print(str(my_reverse)[::-1])

#

# Python Program to find the Smallest number among three.

def find_smallest(a, b, c):
    return min(a, b, c)

num1 = (input("Enter the first number: "))
num2 = (input("Enter the second number: "))
num3 = (input("Enter the third number: "))

smallest = find_smallest(num1, num2, num3)
print("The smallest number among", num1, ",", num2, "and", num3, "is", smallest)

find_smallest(3, 2, 1)
#

# Python Program to calculate the square of a given number.

def calculate_square(number):
    square = number ** 2
    return square


input_number = float(input("Enter a number: "))

result = calculate_square(input_number)
print(f"The square of {input_number} is {result}")



def call():
    reverse(1234)
    find_smallest(5, 6, 9)
    calculate_square(9)


call()


