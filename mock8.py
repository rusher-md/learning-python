# Python – Replace duplicate Occurrence in String

# Python program to accept the strings which contains all vowels

def contains_all_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowels:
        if vowel not in input_string:
            return False

    return True


input_str = input("Enter a string: ")

if contains_all_vowels(input_str):
    print("The input string contains all vowels.")
else:
    print("The input string does not contain all vowels.")