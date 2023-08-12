# Write a program to reverse an integer in Python.
# Python Program to find the Smallest number among three.z
# Python Program to calculate the square of a given number.


# Write a program to reverse an integer in Python.

def reverse(rev1234):
    print("inside reverse\n", rev1234)
    my_reverse = str(rev1234)
    my_reverse2 = (my_reverse[::-1])
    return my_reverse2

#

# Python Program to find the Smallest number among three.

def find_smallest():
    print("inside find_smallest\n")

    num1 = (input("Enter the first number: "))
    num2 = (input("Enter the second number: "))
    num3 = (input("Enter the third number: "))
    return min(num1, num2, num3)






# Python Program to calculate the square of a given number.

def calculate_square():
    print("inside calculate_square\n")

    number = int(input("Enter a number: "))
    result = number * number
    print(f"The square of {number} is {result}")

def convert_list(value):
    print("inside value\n", value)

    my_list = list(value)
    print(my_list)


def call():
    print("inside call\n")
    reversed_value = reverse('asmdnasldnk')
    print(reversed_value)
    convert_list(reversed_value)
    find_smallest2 = find_smallest()
    print("find the smallest number", find_smallest2)
    calculate_square()


call()




