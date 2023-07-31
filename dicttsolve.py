#wap to create a dictionary find the lngth of the dctnry nd perform below operations
# Length of the dictionary should be 10
# Add a key\value pair
# Remove first element
# add element in the middle of dict
# print all elements of the dictionary
# print all keys of the dictionary
# print all values of the dict and convert them into a list
# reverse the above list


# Python program to add a key:value pair to dictionary
#key value pair added

dict = {'key1':'ronaldo', 'key2':'is'}
print("Current Dict is: ", dict)

dict['key3'] = 'better'
dict['key4'] = 'in'
dict['key5'] = 'madrid'
dict['key6'] = 'not'
dict['key7'] = 'in'
dict['key8'] = 'manchester'
dict['key9'] = 'the'
dict['key10'] = 'goat'
print("Updated Dict is: ", dict)

#first element remove

del dict['key1']
print(dict)

#add element in the middle of dict

dict = {'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}

print("The original dictionary is : " + str(dict))
dict = {"key1": 4, "key12": 8}
dict.update(dict)
print("The required dictionary : " + str(dict))

#print all elements of the dictionary


dict = {'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
print(dict.values())

#print all keys of the dictionary

dict = {'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
print(dict.keys())

# print all values of the dict and convert them into a list
dict = {'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
my_list = list(dict.values())
print(my_list)
print(type(my_list))

#reverse the above list

dict = {'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
print("the original dictionary ", dict)
dict2 = {}
for key in reversed(dict):
    dict2[key] = dict[key]
print("The reversed order dictionary ", dict2)




