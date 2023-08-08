def my_print(my1):
    print(my1)

def my_list(my2):
    my_list2 = list(my2)
    return my_list2

def my_pair(key1,value,dictionary):
    dictionary[key1] = value
    print(dictionary)

def call():
    my_print(1)
    myList3 = my_list('my_list2')
    print(myList3)
    my_pair('red', 1, {})


call()





