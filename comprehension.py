key = ['1', '2', '3', '4', '5']
value = ['red', 'blue', 'green', 'yellow', 'violet']

# comprehension

my_Dict = { k:v for (k,v) in zip(key, value)}
print(my_Dict)

l = [i for i in range(10) if i % 2 == 0]
print(l)

# nested


my_list = [[i for i in range(5)] for i in range(5)]
print(my_list)
