#Shawn Gong
#Project Euler Solution 6

def sum_of_squares(value):
    total = 0
    for number in xrange(value + 1):
        total += number ** 2
    return total

print sum_of_squares(10)

def square_of_sum(value):
    total = 0
    for number in xrange(value + 1):
        total += number
    return total**2

print square_of_sum(10)

def difference(value):
    return square_of_sum(value) - sum_of_squares(value)

print difference(10)

#double checking the functions with example value of 10

print difference(100)


