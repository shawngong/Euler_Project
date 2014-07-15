#Project Euler Problem 17
#Shawn Gong
#Idea for code from Jason B. Hill

def total_letters():
    Ones_to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    Twenty_and_up = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6,]
    hundred = 7
    thousand = 8

    total = 0
    for i in xrange(1,1000,1):
        ones = i % 10
        tens = ((i % 100) - ones)/10
        hundreds = ((i%1000) - tens * 10 - ones)/100
        if hundreds != 0:
            total += Ones_to_nineteen[hundreds] + hundred
            if tens != 0 or ones != 0:
                total += 3
        if tens == 0 or tens == 1:
            total += Ones_to_nineteen[tens * 10 + ones]
        else:
            total += Twenty_and_up[tens] + Ones_to_nineteen[ones]
    total += 11
    return total

print total_letters()

#misspelled forty as "fourty" by accident resulting in problems with earlier solution
