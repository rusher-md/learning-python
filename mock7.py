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
    new_list = first_list()
    new_tuple = my_tuple()
    new_string = my_string()
    if len(new_list) > 10 and len(new_tuple) > 10 and len(new_string) > 10:
        converted_list = tuple(new_list)
        converted_string = list([new_string])
        converted_tuple = str(new_tuple)
        print(converted_list, converted_string, converted_tuple)
    else:
        my_print(new_list, new_string, new_tuple)



call()











