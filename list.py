#list

mylist = ['intel core', 'nvidia', 'red', 'gear', 'bella', 'ciao']
print(type(mylist))

# prints all elements in a list

for elements in mylist:
    print(elements)

# add element in list

mylist.insert(3, 'oneplus')
print(mylist)
print(mylist[::-1])
print(mylist)

hh = mylist.copy()
print(hh)

mylist.sort(reverse=True)
print(mylist)

myCount = mylist.count('red')
print(myCount)

my_List = ['oneplus']
mylist.append(mylist)

mylist.remove('red')
print(mylist)

mylist.pop(-2)
print(mylist)


