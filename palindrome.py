# get  input from user
inp = input('enter the value: ')
# palindrome or not ?
rev = inp[::-1]
print(rev)
if rev == inp:
    print('yes')
else:
    print('no')
