# BCPU testing

from bcpu import *

myprog = """

Set(r1,2)
Set(r2,2)
Set(r3,0)
Set(r4,0)
Set(r5,0)
Set(r6,1)
Set(r7,2)
Set(r8,4)
Set(r9,0)
Set(r10,0)
Set(r11,0)
Set(r12,0)
Set(r13,0)
And(r3,r2,r6)
And(r4,r2,r7)
And(r5,r2,r8)

Movez(r10,r9,r3)
Movex(r10,r1,r3)
Add(r13,r13,r10)

Movez(r11,r9,r4)
Movex(r11,r1,r4)
Add(r11,r11,r11)
Add(r13,r13,r11)

Movez(r12,r9,r5)
Movex(r12,r1,r5)
Add(r12,r12,r12)
Add(r12,r12,r12)
Add(r13,r13,r12)

"""

# testing process

print("...Loading asm program into memory...")
load(myprog)
printm()


print("...Runing test program...")
run()
printr()





