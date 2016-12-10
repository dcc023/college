from bcpu import *




eightbitleftrotation = """

#bitwise left rotation
#only shifts by 1 bit.
#8 bit size only
Set(r1,110)
Set(r2,255) #9 bits for after the shift. Can be adjusted depending on bit length. Meant to zero out the left most bit after shifting is done
Set(r3,0b10000000) #8 bits currently. Changes depending on most significant bit
Set(r4,0b00000001) #8 bits currently. Changes depending on least significant bit
And(r5,r1,r3) #Find out if most significant bit is a 0 or 1

#left bit shift
Add(r1,r1,r1)

#after the left shift
#if Left most bit is 1, Right most bit becomes 1
Addi(r7,pc,4)
Movez(pc,r7,r5)
Addi(r1,r1,1) #set right most bit to 1
And(r8,r1,r2) #zero out left most bit


#else, right most bit becomes 0.
Move(r1,r1)

"""



eightbitrightrotation = """

#bitwise right rotation
#only shifts by 1 bit.
#8 bit size only
Set(r1,22)
Set(r2,254) #9 bits for after the shift. Can be adjusted depending on bit length. Meant to zero out the right most bit after shifting is done
Seth(r2,1) #sets r2 to 0b111111110
Set(r3,0b10000000) #8 bits currently. Changes depending on most significant bit
Set(r4,0b00000001
) #8 bits currently. Changes depending on least significant bit
And(r5,r1,r4) #Find out if most significant bit is a 0 or 1



#right bit shift
Set(r9,0) #counter for division
Move(r10,r1)
Subi(r10,r10,2)
Addi(r9,r9,1) #i = i + 1
Addi(r11,pc,5) #skip to end of bit shift if not evenly divisible
Addi(r12,pc,6) #skip to end of bit shift if evenly divisble
Moven(pc,r11,r10)
Movez(pc,r12,r10)
Subi(pc,pc,6)
#if not evenly divisible by 2
Subi(r1,r9,1)
Addi(pc,pc,2)
#if evenly divisible by 2
Move(r1,r9)
#end of right bit shift


#after the right shift
#if right most bit is 1, left most bit becomes 1
Addi(r7,pc,5)
Movez(pc,r7,r5)
Set(r14,128) #because BCPU Addi won't go higher than 15...
Add(r1,r1,r14) #set left most bit to 1 (8bits)
And(r1,r1,r2) #zero out right most bit


#else, left most bit becomes 0.
Move(r1,r1)

"""

load(eightbitrightrotation)
run()

