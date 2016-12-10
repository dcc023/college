# BCPU testing

from bcpu import *

#If r1 > r2, jump to the instruction that turns r0 to 1.

#r1 and r2 are the test parameters
#r6 and r7 are to check for the conditional jump

#Have r1 and r2. 
#Perform r2 - r1 = r3.
#Add pc+2 to the r10 register
#If r2-r1 = negative value, then It means that r2 is a greater value than r1, since it means that r2 is neither less than or equal to.
#So, if r2-r1 = negative, then skip 2 instructions and add registers r6 + r7 to r0 to produce 10.
#Else, It adds 1 to r6 and r7, then adds r6+r7 to produce 12. 

myprog = """

Set(r6,5) #100
Set(r7,5) #101


Set(r1,3) #102
Set(r2,1) #103


Sub(r3,r2,r1) #104 
Addi(r10,pc,4) #105
Moven(pc,r10,r3) #106
Addi(r6,r6,1) #107
Addi(r7,r7,1) #108
Add(r0,r6,r7) #109

 



"""

# testing process

load(myprog,100)
run(100)



