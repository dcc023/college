# Design an algorithm that is able to min/max comparison with
# (3n/2) - 2 comparisons.
# Can use list, python. Need to set a performance counter to
# count how many comparisons you do. So that at the end we can
# check if we are meeting our comparison goal of 3n/2 - 2.
#
# import random : imports a library that lets you use random numbers
# random.randrange(n): chooses "random" number from 0 to n.
# L = [random.randrange(100) for _ in range(100)]: creates array
# filled with integers from 0 to 100 scrambled in the array.

findMinMax(al):
    max = al[0]
    min = al[1]

    for i in al:
        if al[i] > max:
            max = al[i]
        if al[i] < min:
            min = al[i]
    
    return("max:"max "min:"min)


#-------------------------------------------------------------------------
#INCLASS CODE
def findMinMaxClass(L):
    if len(L)%2 != 0: #odd number get one
        c = 0
        minv = maxv = L[0]
    else: #even get two
        c = 1
        (minv, maxv) = (L[0], L[1]) if L[0] <= L[1] else (L[1], L[0])
        i=2
    for n in range(i, len(L), 2):
        c = c+3
        if L[n] <= L[n+1]:
            minv = minv if minv <= L[n] else L[n]
            maxv = maxv if maxv >= L[n+1] else L[n+1]
        else:
            minv = minv if minv <= L[n+1] else L[n+1]
            maxv = maxv if maxv >= L[n] else L[n]
    print(c, 1.5*len(L))
    return minv, maxv

#testing
from random import randrange as rand
L = [rand(80) for x in range(193)]
print(L, len(L))
print(findMinMaxClass(L))
