# convert list to tuple, duct
my_list = ['practice ',  'makes', 'you perfect']
print(type(my_list))

my_tup = tuple(my_list)
print(my_tup, type(my_tup))

#     #tuple into dict
#
# inputTuple = [("god", "is", "one")]
# print(type(inputTuple))
#
# myDictionary = dict(inputTuple())
# print(myDictionary,type(myDictionary))
#

# convert dict to list, tuple

mydict = {'key1': 'R7', 'key2': 'is', 'key3': 'better'}
print(mydict)

my_list2 = list(mydict)
print(my_list2)

myTup2 = tuple(mydict)
print(myTup2)

# convert tuple to list, dict


var = ("Good", "for", "Good")
print(var)

mylist3 = list(var)
print(mylist3)

# mydict9 = dict(var)
# print(mydict9)

# print all elements for list, tuple and dict

for ele in my_list:
    print(ele)

for red in my_list2:
    print(red)

for my in mylist3:
    print(my)

for t in my_tup:
    print(t)

for y in myTup2:
    print(y)

for u in var:
    print(u)

# print middle element for list, tuple and dict
mydict = {'key1': 'R7', 'key2': 'is', 'key3': 'better'}
first_key = mydict['key2']
print(first_key)

# var = ("Good", "for", "Good")

# reverse dict, tuple, list

my_list = ['practice ',  'makes', 'you perfect']
print(my_list)
lst = my_list[::-1]
print(lst)



mydict = {'key1':'R7','key2':'is','key3':'better'}
print("The original dictionary : " + str(mydict))
res = dict(reversed(list(mydict.items())))
print("The reversed order dictionary : " + str(res))

#
# def reverse(var):
#     new_tup = var[::-1]
#     return new_tup
#
#
#
# var = ("Good", "for", "Good")
# print(var)
















    
    
    
    










