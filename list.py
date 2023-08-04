#list

mylist = ['intel core', 'nvidia', 'red', 'gear', 'bella', 'ciao']
print(type(mylist))


# prints all elements in a list

for elements in mylist:
    print(elements)

# add key value pair in list

mylist.insert(6, 'oneplus')
print(mylist)

my_List = ['oneplus']
mylist.append(mylist)

mylist.remove('red')
print(mylist)

mylist.pop(-2)
print(mylist)


