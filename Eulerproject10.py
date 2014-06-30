#Project Euler solution 10
#Shawn Gong

def prime(value):
    for i in xrange(2,int(value**0.5) + 1):
        if value%i == 0:
            return False
    return True

#from solution 7

def summation(n):
    total = 0
    for number in xrange(2,n + 1):
        if prime(number) == True:
            total += number
    return total

print summation(2000000)