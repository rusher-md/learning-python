

#Write a program to reverse an integer in Python.

a = 585787837457
print(type(a))

print(str(a)[::-1])
reversed_num = 0
while a != 0:
    digit = a % 10
    reversed_num = reversed_num * 10 + digit #75
    a //= 10

print(reversed_num)
