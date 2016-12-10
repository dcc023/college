from bcpu import *

operand = """


Set(r0,0)
Set(r9,1)

#r1 == r2
Set(r1,2)
Set(r2,2)
Sub(r3,r2,r1)
Movez(r0,r9,r3)

Set(r0,0)
Set(r9,1)

#r1 != r2
Set(r1,2)
Set(r2,3)
Sub(r3,r1,r2)
Movex(r0,r9,r3)

Set(r0,0)
Set(r9,1)

#r1 >= r2
Set(r1,3)
Set(r2,2)
Sub(r3,r1,r2)
Movep(r0,r9,r3)

Set(r0,0)
Set(r9,1)

#r1 <= r2
Set(r1,1)
Set(r2,3)
Sub(r3,r2,r1)
Movep(r0,r9,r3)

Set(r0,0)
Set(r9,1)

#r1 > r2
Set(r1,3)
Set(r2,2)
Sub(r3,r2,r1)
Moven(r0,r9,r3)

Set(r0,0)
Set(r9,1)

#r1 < r2
Set(r1,1)
Set(r2,3)
Sub(r3,r1,r2)
Moven(r0,r9,r3)

"""

mul = """

#r3=r1*r2
Set(r0,0) # i = 0
Set(r1,3)
Set(r2,4)
Set(r4,1)#And bit
And(r5,r2,r4)#And r2 bit
Movex(r6,r1,r5)
Add(r3,r3,r6)
Add(r1,r1,r1)
Add(r4,r4,r4)
Addi(r0,r0,1)
Subi(r7,r0,15) #16 iterations
Subi(r8,pc,7)
Set(r6,0)
Moven(pc,r8,r7)

"""


array = """

Set(r10,0) #index
Set(r1,0) #beginning number in array
Set(r2,0) #i
Store(r10,r1)
Addi(r10,r10,1)
Addi(r1,r1,1)
Addi(r2,r2,1)
Subi(r7,pc,4)
Subi(r6,r2,10) #10 iterations
Moven(pc,r7,r6)

"""

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
printr()
printd()
