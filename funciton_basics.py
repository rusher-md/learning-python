# fuctions or methods
# waf to print name from user input
def print_name():
    user_input = input('Type your name: ')
    print(user_input)

# waf to add two numbers


def add_two_numbers(num1, num2):

    addition = num1 + num2
    print(f"Sum of two numbers is {addition}")
    print_name()

# call one fn from another


add_two_numbers(12, 13)
