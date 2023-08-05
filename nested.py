li = [{1:'2', 2:'3' }, [1,24], [12,3,4], 'adnan', {1:'2', 2:'3' }]
# li.remove({1:'2', 2:'3' })
# sliced_li = li[1].insert(2, 43)
# print(li)

# d = {'key1': 'R7' , 'key2': 'is', 'key3': 'better', 'key4': 'in', 'key5': 'madrid','key6': 'not', 'key7': 'in', 'key8': 'manchester', 'key9': 'the', 'key10': 'goat'}
# a = d.popitem()
# print(a)
# print(d)

new_dict = li[0]
# print(new_dict)

# for value in new_dict:
    # print(value, new_dict[value])

new_save = li[2]
li.pop(2)
print(li)

NewSave = new_save[::-1]
li.insert(2, NewSave)
print(li)

new_Dict = li[0]
print(new_Dict)

res = dict(reversed(list(new_Dict.items())))
print("the reversed order dictionary : " + str(res))

li.pop(0)
print(li)

li.insert(0, res)
print(li)

removeDict = li[4]
print(removeDict)

t = list(removeDict.items())
print(t)
# [(1, '2'), (2, '3')]
print(f"{t[0][0]}:{t[0][1]},{t[1][0]}:{t[1][1]}")
