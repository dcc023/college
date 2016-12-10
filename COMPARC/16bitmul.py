from bcpu import *

mul = """

#setup
Set(r1,100) #r1*r2=r0
Set(r2,100)
Set(r3,0b001) #Bitmask
Set(r10,0) #i=0, iterate 16 times.
#begin loop
Addi(r10,r10,1) #i = i + 1
Subi(r11,r10,15) #test if i-16 = 0
Subi(r12,pc,2) #pc 2 instructions back
And(r4,r2,r3)
Add(r3,r3,r3)
Movex(r13,r1,r4)
Add(r0,r0,r13)
Add(r1,r1,r1)
Set(r13,0)
Moven(pc,r12,r11)
printm(0)
#end loop



"""




load(mul)
run()
