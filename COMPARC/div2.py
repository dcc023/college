from bcpu import *


#division


div = """
#r3 = r1%r2
#r4=r1//r4
Set(r1,7)
Set(r2,4)
Move(r3,r1)
	#body of loop
	Set(r4,0)#Counter for division
	Sub(r3,r3,r2)
	Addi(r4,r4,1)
	Subi(r6,pc,2)#If the result is positive
	Addi(r7,pc,7)#If the result is zero
	Addi(r8,pc,4)#If the result is negative
	Movep(pc,r6,r3)
	Movez(pc,r7,r3)
	Moven(pc,r8,r3)
#if the division is out of wack
Add(r3,r3,r2)
Subi(r4,r4,1)
#if the division is even.


"""

load(div)
run()
