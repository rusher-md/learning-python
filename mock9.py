# Create a fn to check if a string contains any special character
# Create a fn to Check if a given string is binary string or not
# Convert Snake case to Pascal case


import re

def contains_special_character(input_string):
    special_characters = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')  # Add more special characters if needed
    if special_characters.search(input_string):
        print(special_characters)
        return True
    return False


contains_special_character('@#$%')


