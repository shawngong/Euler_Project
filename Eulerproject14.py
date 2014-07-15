#Project Euler Problem 14
#Shawn Gong

def collatz(n):
    count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count


def max():
    greatest = 1
    for i in xrange(1000000):
        length = collatz(i)
        if length > greatest:
            greatest = length
    return greatest

def solution():
    for i in xrange(1000000):
        if collatz(i) == 525:  #found using a print max()
            return i

print solution()




