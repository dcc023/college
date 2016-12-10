#test program counter

from bcpu import * 

testpc = """"

Aboslute addressing
Set(r1,1) #200
Set(pc,203) #201, goto 203 (absolute addressing)
Set(r2,2) #202
Set(r3,3) #203

#Relative addressing
Set(r1,1)
Set(pc,pc,2) #skip next instruction (relative addressing)  
Set(r2,2) 
Set(r3,3) 

#
Set(r1,1)
Addi(r10,pc,3)
Movex(pc,r10,r13) #skip next instruction if r1 != 0  
Set(r2,2) 
Set(r3,3) 


"""

load(testpc,500)
run(500)
