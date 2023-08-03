# values should be taken as input from the terminal
# do maths addition of the values and print the result
# convert the result into a list
# convert the inputs into a tuple
# delete the last and middle value of the list
# check if the entered values are numeric type else display error

print('a', 'b', 'c')

a = '123'
b = '321'
c = '543'

new_a = int(a)
new_b = int(b)
new_c = int(c)
print(new_a + new_b + new_c)
new_str = str(new_a)
new_str2 = str(new_b)
new_str3 = str(new_c)
print(new_str, type(new_str), type(new_str2), type(new_str3))

new_lst1 = list(a)
print(new_lst1)

new_lst2 = list(b)
print(new_lst2)

new_lst3 = list(c)
print(new_lst3)

new_tup = tuple(a)
print(new_tup)

new_tup2 = tuple(b)
print(new_tup2)

new_tup3 = tuple(c)
print(new_tup3)
print(type(new_tup), type(new_tup2), type(new_tup3))

new_lst1 = ['1', '2', '3']
new_lst1.pop(0)
print(new_lst1)

new_lst2 = ['3', '2', '1']
new_lst2.pop(1)
print(new_lst2)























