# create_file(filename)
# read_file(filename)
# append_file(filename, "This is some additional text.\n")
# rename_file(filename, new_filename)
# read_new_file(new_filename)
# delete_file(new_filename)
# Use docstrings for every function definition

import os


def handling():
    '''This Function create read append and rename the handling '''
    with open('handling.txt', 'r') as file:
        data = file.read()
        print(data)


    os.rename('filehandling.py', 'newfilehandling.py')

    os.remove('handling.txt')  # working properly

    file = open('handling.txt', 'a')
    file.write('added new data')
    file.close()
    os.rename('handling.txt', 'newhandling.txt')


handling()
print(handling.__doc__)







