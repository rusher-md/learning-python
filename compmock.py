# Create a list using comp that has all the even numbers up to 30
# Create a dict using comp that takes values from the below list as keys and values as its upper case.
# l = ['x', 'f', 'g', 'h', 'w', 'm']
# and = {'x': 'X', 'f':'F', 'g':'G', ..... }


my_list = [i for i in range(30) if i % 2 == 0]
print(my_list)

# Create a dict using comp that takes values from the below list as keys and values as its upper case.

l = ['x', 'f', 'g', 'h', 'w', 'm']

my_dict = {key: key.upper() for key in l}
print(my_dict)
