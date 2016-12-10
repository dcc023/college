from bcpu import *

ifelse = """

Set(r1,2)


#if
Addi(r10,pc,5) #Setup goto addr
Movez(pc,r10,r1) #If not goto else
#then
Set(r2,1)
Set(r3,3)
Addi(pc,pc,3) #Skip over else
#else
Set(r2,0)
Set(r4,4)

Move(rout0,r3)
Move(rout0,r4)

"""

load(ifelse)
run()
