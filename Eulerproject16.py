#Project Euler Problem 16
#Shawn Gong

def exponent_of_two(n):
    return 2**n

def sum_of_digits(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

print sum_of_digits(exponent_of_two(1000))
