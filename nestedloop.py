#
# Add a list at the last index of the given nested list
#
# Delete the middle element of the nested list
#
# Print all element of the last added nested list
#
# add an element of integer type to the end of the nested list
#
# reverse the nested list
#
# add a dict with 3 key value pairs to the start of the nested list
#
# find the length of the nested list

nested_List = [{1: '2', 2: '3'}, [1, 24], [12, 3, 4], 'adnan']

# Add a list at the last index of the given nested list

nested_List.append('mustang')
print(nested_List)
# Delete the middle element of the nested list
nested_List2 = len(nested_List)
print(nested_List2)

nested_List3 = nested_List2 // 2
print(nested_List3, 'jkjkjk')

nested_List.pop(nested_List3)
print(nested_List3)

# add an element of integer type to the end of the nested list

nested_List.append(8)
print(nested_List)

# reverse the nested list
nested_List.reverse()
print(nested_List)

# add a dict with 3 key value pairs to the start of the nested list
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict)

nested_List.insert(0, my_dict)
print(nested_List)

# find the length of the nested list
my_length = len(nested_List)
print(my_length)


# Print all elements of the last added nested list

new_dict2 = nested_List.insert(6, 'new element')
print(nested_List)

new_dict3 = nested_List[-1]
print(new_dict3)

for element in new_dict3:
    print(element)




