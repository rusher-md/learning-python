
a = int(input("Enter the value for a :"))
b = int(input("Enter the value for b :"))
c = int(input("Enter the value for c :"))
if a <= b and a <= c:
    print("a is smallest")
elif b <= a and b <= c:
    print("b is smallest")
else:
    print("c is smallest")