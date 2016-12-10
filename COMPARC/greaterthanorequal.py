# BCPU testing

from bcpu import *

#r0 is 1 if r2 >= r3 is TRUE
#r0 is 0 if r2 >= r3 is FALSE


myprog = """
Set(r0,0)
Set(r1,1)
Set(r2,7)
Set(r3,8)
Sub(r4,r2,r3)
Movep(r0,r1,r4)

"""

# testing process

print("...Loading asm program into memory...")
load(myprog)
printm()


print("...Runing test program...")
run()
printr()






