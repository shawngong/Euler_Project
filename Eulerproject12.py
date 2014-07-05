#Project Euler Problem 12
#Shawn Gong


def triangle_number(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

def factors(r):
    result = []
    for i in range(1,r+1):
        if r % i == 0:
            result.append(i)
    return len(result)

print factors(triangle_number(7))

def solution(x):
    a = 1
    while (factors(triangle_number(a))) <= x:
        a += 1
    else:
        return triangle_number(a)

print solution(500)


