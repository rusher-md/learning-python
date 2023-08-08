# Function that takes 1 argument of string type and checks if it is a string or not.
# Function that takes 2 arguments of numeric type and converts them into float type.
# Function that takes 4 arguments of string type and concatenates all of them, then convert the final value to a list
# Function that takes a list as an input argument and displayed its length.
# Function that prints an inverted pyramid using *

# Function that takes 1 argument of string type and checks if it is a string or not.
def type_string():
    my_function = 'my function'
    print(type(my_function))


type_string()

# Function that takes 2 arguments of numeric type and converts them into float type.


def arguments(num1, num2):
    my_arguments = float(num1)
    my_arguments2 = float(num2)
    print(my_arguments, my_arguments2)


arguments(1123, 3321)

# Function that takes 4 arguments of string type and concatenates all of them, then convert the final value to a list
def my_str(str1, str2, str3, str4):
    my_str2 = str1 + str2 + str3 + str4
    print(type(my_str2))
    my_str3 = list(my_str2)
    print(my_str3)


my_str('red', 'green', 'blue', 'yellow')

# Function that prints an inverted pyramid using

def my_pyramid():
    rows = 5
    for i in range(rows,0,-1):
        for j in range(i):
            print("*", end="")

        print("\n")


my_pyramid()












