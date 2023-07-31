str1 = "Hello world"
print(type(str1))

str2 = list(str1)
print(str2)

str3 = str1[:5]
print(str3)

str4 = str1[6:]
print(str4)

dic = {}
print(dict)

dic = str3[:5]
print(dic)

dic = {1: "Hello", 2: "world", '3': 6, 'yes': '9'}
print(dic)

print(type(dic.keys()))

for v in dic:
    print(v)

i = 0
for j in str2:
    print(i, j)
    i += 1

li =[10, 20, 30]
n = len(li)
print("the length of list is: ", n)




















