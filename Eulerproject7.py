#Project Euler Solution 7
#Shawn Gong

def prime(value):
    for i in xrange(2,int(value**0.5) + 1):
        if value%i == 0:
            return False
    return True


def order_of_prime(n):
    solution = []
    for i in xrange(2,999999):
        if prime(i) == True:
            solution.append(i)
    return solution[n-1]

print order_of_prime(10001)