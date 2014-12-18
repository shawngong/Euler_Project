#-------------------------------------------------------------------------------
# Name:        ProjectEuler Problem 21
# Purpose:
#
# Author:      Shawn Gong
#
# Created:     17/12/2014
# Copyright:   (c) Shawn Gong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
def Divisorsbaritself(x):
    divList = [1]
    y = 2
    while y <= math.sqrt(x):
        if x % y == 0:
            if y is not int(x/y):
                divList.append(y)
                divList.append(int(x / y))
            else:
                divList.append(y)
        y += 1
    return sum(divList)

print Divisorsbaritself(36)

def amicable():
    solution = [i for i in xrange(10000) if Divisorsbaritself(i)!=i and Divisorsbaritself(Divisorsbaritself(i)) == i]
    return sum(solution)

print amicable()








