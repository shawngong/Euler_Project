#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 22
# Purpose:
#
# Author:      Shawn Gong
#
# Created:     18/12/2014
# Copyright:   (c) Shawn Gong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

in_file = open('C:\Users\Shawn Gong\Documents\coding\Eulers Project\p022_names.txt')


def totalscore():
    sum = 0
    my_list = in_file.read().replace("\"",'').split(",")
    for x in sorted(my_list):
        sum = sum + score(x) * (my_list.index(x) + 1)
    return sum


def score (x):
    scoretotal = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z"]
    for i in x:
        scoretotal = scoretotal + alphabet.index(i) + 1
    return scoretotal

print totalscore()


