#compare two numbers check ==, !=, >=, <=, >,<

#r1, r2 are the numbers.

#If true r3=1, otherwise r3=0

from bcpu import *

myprog = """

#testing
Set(r1,1)
Set(r2,2)

#check ==
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r1,r2)
Movez(r3,r10,r4)

#check !=
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r1,r2)
Movex(r3,r10,r4)

#check r1 >= r2
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r1,r2)
Movep(r3,r10,r4)

#check r1 <= r2
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r2,r1)
Movep(r3,r10,r4)

#check r1 > r2
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r2,r1)
Moven(r3,r10,r4)

#check r1 < r2
Set(r10,1)
Set(r3,0) # assume to be false
Sub(r4,r1,r2)
Moven(r3,r10,r4)

"""


# testing process

load(operand)
run()
