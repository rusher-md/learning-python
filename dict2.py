my_dict = {'key1': 'R7', 'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in',
           'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
last_keys = my_dict.keys()
list_format = list(last_keys)
print(list_format, type(list_format))

first_keys = list_format[2]
print(first_keys)

last_value = my_dict[first_keys]
print(f"{first_keys}:{last_value}")

for l in my_dict:

    print(l, my_dict[l])

for g in last_value:
    print(g)




