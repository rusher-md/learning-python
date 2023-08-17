# create_file(filename)
# read_file(filename)
# append_file(filename, "This is some additional text.\n")
# rename_file(filename, new_filename)
# read_new_file(new_filename)
# delete_file(new_filename)
# Use docstrings for every function definition



def handling():
    '''This Function create read append and rename the handling '''
    with open('handling.txt', 'a') as file:
        data = file.write('append data')

    file = open('handling.txt', 'a')
    file.write('added new data')
    file.close()


handling()
print(handling.__doc__)








