# my_dict = {'key1': 'R7' , 'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid', 'key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
#
# len2 = len(my_dict)
# print(len2)
# half = len2 // 2
# print(half)
#
# dict1 = {k: v for i, (k, v) in enumerate(my_dict.items()) if i < half}
# dict2 = {k: v for i, (k, v) in enumerate(my_dict.items()) if i >= half}
# print(dict1, dict2)


list1 = [1, 2, 23, 4, 5, 6]
print(list1)

new_list = [list1[e] for e in range(5)]

print(new_list)