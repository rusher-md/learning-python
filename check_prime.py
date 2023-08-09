# check prime number

def check_prime(num):
    # declare a variable that stores no of factors
    factors = 0

    # run a loop from 1 to the number and check if the number is divisible by the temp variable inside loop
    for i in range(1, num+1):
        if num % i == 0:
            factors +=1
    # print if the factors are less than or equal to 2 
    if factors <= 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

check_prime(7)
