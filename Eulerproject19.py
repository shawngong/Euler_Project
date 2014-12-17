#-------------------------------------------------------------------------------
# Name:        Euler Project 19
# Purpose:
#
# Author:      Shawn Gong
#
# Created:     16/12/2014
# Copyright:   (c) Shawn Gong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#in a year there are how many number of days:

sum = 0

def numberofdays ():
    sum = 0
    leapyears = []
    first = []
    for i in range (1901, 2001):
            if i == 1901:
                sum = sum + 1
                first.append (sum)
                for x in range(1, 12):
                    if x == 1:
                        sum = sum + 28
                        first.append (sum)
                    elif x in [3, 5, 8, 10]:
                        sum = sum + 30
                        first.append (sum)
                    else:
                        sum = sum + 31
                        first.append (sum)
            if i%4 == 0:
                leapyears.append (i)
                for x in range (1, 13):
                    if x == 2:
                        sum = sum + 29
                        first.append (sum)
                    elif x in[4, 6, 9, 11]:
                        sum = sum + 30
                        first.append (sum)
                    else:
                        sum = sum + 31
                        first.append (sum)
            else:
                for x in range (1, 13):
                    if x == 2:
                        sum = sum + 28
                        first.append (sum)
                    elif x in[4, 6, 9, 11]:
                        sum = sum + 30
                        first.append (sum)
                    else:
                        sum = sum + 31
                        first.append (sum)

    return sum, first

#print numberofdays()


#by calculation Jan 1st 1901 is a Tuesday.
def date (number):
    if number%7 == 0:
        return "Monday"
    if number%7 == 1:
        return "Tuesday"
    if number%7 == 2:
        return "Wednesday"
    if number%7 == 3:
        return "Thursday"
    if number%7 == 4:
        return "Friday"
    if number%7 == 5:
        return "Saturday"
    if number%7 == 6:
        return "Sunday"

def listofsundays ():
    list1 = []
    for i in range (numberofdays()[0] + 1):
        if date (i) == "Sunday":
            list1.append (i)
    return list1

#print listofsundays ()

def solution ():
    solution = []
    for x in numberofdays()[1]:
        if x in listofsundays ():
            solution.append (x)
    return len(solution)

print solution()







