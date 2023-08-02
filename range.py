
my_dict = { 1: 'red', 2: 'gear'}
all_keys = my_dict.keys()
list_format = list(all_keys)
print(list_format, type(list_format))

first_key = list_format[0]
print(first_key)

first_value = my_dict[first_key]
print(f"{first_key}:{first_value}")

all_values = my_dict.values()

print(all_values)






