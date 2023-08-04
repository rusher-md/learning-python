# Dictionary

d = {'key1': 'R7' , 'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid','key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}

print(d)

# prints all keys in a dictionary
print(d.keys(), type(d.keys()))

# prints all values in a dictionary
print(d.values())

# how to get value of a key in a dictionary
valueOfGivenKey  = d['key3']
print(valueOfGivenKey)

# print key value pair of a dictionary
for key in d:
    print(key, d[key])

# get all items in a dictionary
all_items = d.items()
print(all_items)
print(type(all_items))

# conversion of dict_items to list and tuple
d_list = list(all_items)
print(d_list)

d_tuple = tuple(all_items)
print(d_tuple, type(d_tuple))

# add key value pair
d['key11'] = 'new value'
print(d)

# update/change value of a key
d['key10'] = 'updated value'
print(d)
