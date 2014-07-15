#Project Euler Problem 15
#Shawn Gong
#Idea for code from Jason B.Hill

def route(square):
    n = [1]*square  #creating a new list of "1"s equal to one length of square
    for i in range(square):
        for j in range(i):
            n[j] += n[j-1]
        n[i] = 2*n[i-1] #both these uses mathematical assumptions that are proven
    return n[square - 1]

print route(20)