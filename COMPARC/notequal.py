# BCPU testing

from bcpu import *

#r0 is 1 if r2 != r3 is TRUE (r2!=r3)
#r0 is 0 if r2 != r3 is FALSE (r2=r3)
#r2 is subtracted by r3
#The difference is placed into r4
#If r4 is 0, then r1 is moved to r0.

myprog = """

Set(r0,1)
Set(r1,0)
Set(r2,7)
Set(r3,6)
Sub(r4,r2,r3)
Movez(r0,r1,r4)

"""

# testing process

print("...Loading asm program into memory...")
load(myprog)
printm()


print("...Runing test program...")
run()
printr()
