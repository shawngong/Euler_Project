#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 20
# Purpose:
#
# Author:      Shawn Gong
#
# Created:     17/12/2014
# Copyright:   (c) Shawn Gong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

sum = 0
string = str(math.factorial(100))
list1 = []

for digit in string:
    list1.append (int (digit))

for i in list1:
    sum = sum + i

print sum



