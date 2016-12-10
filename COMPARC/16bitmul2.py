#mul 16 bit bitwise r3 = r2*r1

from bcpu import *

mul = """

	Set(r0,1)
	Set(r3,0)

	And(r4,r1,r0) #test k bit
	Addi(r5,pc,3) #setting jump addr
	Movez(pc,r5,r4) #skip for not add
	Add(r3,r3,r2)
	
	Add(r2,r2,r2) #shift left
	Add(r0,r0,r0)
	Subi(r5,pc,6) #setting addr for loop back
	Movep(pc,r5,r0)

	Move(r3,r3)



"""

#testing
Set(r2,6)
Set(r1,7)

load(mul)
run()
