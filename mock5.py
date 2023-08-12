def one_function(my1, my2, my3):
    print("inside one_function\n", my1, my2, my3)
    print(my1 + sec_function(my2, my3))

def sec_function(my2, my3):
    print("inside sec_function\n", my2, my3)
    sec_value = my2 + third_function(my3)
    return sec_value



def third_function(my3):
    print("inside third_function\n", my3)
    return my3


my3 = 'juventus'
my1 = 'portugal'
my2 = 'real madrid'
one_function(my1, my2, my3)
















