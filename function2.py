def first_name():
    user_input = input('first name ')
    return user_input


def last_name():
    user_input = input('last name ')
    return user_input


def full_name():
    first = first_name()
    last = last_name()
    full = f"{first} {last}"
    var_type = check_type(full)
    print(full)
    print(var_type)


def check_type(variable):
    type_of_value = type(variable)
    return type_of_value


full_name()

