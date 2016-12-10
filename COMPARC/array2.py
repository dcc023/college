#array

from bcpu import *

array = """

Set(r10,10) #start of our array
Set(r1,0) #data

Store(r10,r1)
Addi(r10,r10,2)
Addi(r1,r1,1)
Subi(r13,pc,3)
Subi(r2,r1,10) #array size 10
Moven(pc,r13,r2)

#seq search
#search a number call key in an array
#if found, return index, else return -1

#assign r1 = key, r3 = ans

"""

load(array)
run()

