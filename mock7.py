def first_list():
    print("inside first_list\n")
    my_list = list(["apple", "banana", "cherry"])
    return my_list



def my_string():
    print("inside my_string\n")
    my_string2 = str('nvidia')
    return my_string2

def my_tuple():
    print("inside my_tuple\n")
    my_tuple3 = tuple(("Geeks", "for", "Geeks"))
    return my_tuple3


def my_print(new_list, new_string, new_tuple):
    print("inside my_print\n", new_list, new_string, new_tuple)

    print(new_list, new_string, new_tuple)



def call():
    new_list = tuple(first_list())

    new_string = list([my_string()])

    new_tuple = str(my_tuple())

    my_print(new_list, new_string, new_tuple)


call()











