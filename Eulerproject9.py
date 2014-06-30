#Project Euler Problem 9
#Shawn Gong

def triplet(a,b,c):
    while int(a) < int(b) < int(c):
        if int(a) ** 2 + int(b) ** 2 == int(c) ** 2:
            return True
        return False


def Pythagorean_triplet(n):
    for a in xrange(1,n,1):
        for b in xrange(1,n-a,1):
            c = n-a-b
            if triplet(a,b,c) == True:
                return a * b * c
    return "void"

print Pythagorean_triplet(1000)


