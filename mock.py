#make a string using strng function converted into a list print thr strng and print the list print the middle element of the list
#“Hello world”

#2- append and make the strng lenght to odd number
"Hello worlds"

#3- create a dictionary with key value pair by splitting the strng
#{1:“hello”,2:”worlds”}


# create a string using str function
str1 = str("Hello world")
print(type(str1))

# Convert it to list
str2 = list(str1)
print('converted to list >>> ',str2, type(str2))

# Check length of string
print('length of string >>> ', len(str1))

# Append and make the strng lenght to odd number
str1 += 's'
print(str1)

# Create a dictionary with key value pair by splitting the strng
my_dict = {}

my_dict[1] = str1[:5]

my_dict[2] = str1[5:]

print(my_dict)
