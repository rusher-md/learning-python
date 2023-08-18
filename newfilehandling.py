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
    whandling.txt', 'a') as file:
        data = file.write('append data')
    )
    file.close()

    file.write('added new data')
    # os.rename('handling.txt', 'newhandling.txt') cant change the name of txt file but .py name is changing succesfully
#     os.rename('filehandling.py', 'newfilehandling.py') working properly
ith
open('
    # os.remove('handling.txt')  # working properly

    file = open('handling.txt', 'a'

handling()
print(handling.__doc__)







