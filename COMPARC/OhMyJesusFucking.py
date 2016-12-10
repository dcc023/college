
from bcpu import *

sweetjesus = """
#r3 = r1^r2

#registers:
#r1: Base
#r2: Power
#r3: Final Answer
#r4: Multiplier Counter
#r5: TEMP Comparioson 0 for Power and Counter
#r6: TEMP value holder for pc jump
#r13: Base copy
#r14: general use skipper

#while r 4(counter) aint equaling r 2
Set(r1, 3) #Base
Set(r2, 3) #Power
Set(r3, 1) #Final answer initialized as zero in case of power of zero
Set(r4, 0) #Counter starts at 0
Move(r13, r1) #copy r1 into r13 because I DUNNO LOL
Set(r14, 17)
Add(pc, pc, r14) #Skip the multiplication shit for now

#multiply
#multiply
#multiply
#multiply

#registers in this:
#r5: Original Base copy
#r6: Copy of original original base
#r7: Our 'bit mask'
#r8: Counts up to 15
#r9: Where the And gets put. Changing.
#r10: Holds what we end up adding, 0 or r6
#r11: Holds counter to check if we've gone 16 bits
#r12: Holds jump value


Move(r5, r13) #r1*r2=r0
Move(r6, r1)
Set(r13, 0) #Set this to zero so it can take its new value
Set(r7,1) #Bitmask
Set(r8,0) #i=0, iterate 16 times.

#begin loop
Addi(r8,r8,1) #i = i + 1
Subi(r11,r8,15) #test if i-16 = 0
Subi(r12,pc,2) #pc 2 instructions back

#multiplication begins
And(r9,r6,r7) #Into r9, r6 AND r7
Add(r7,r7,r7) #Move bit mask
Movex(r10,r5,r9) #If r9 is NOT zero, put r5 into r10
Add(r13,r13,r10) #Add r10 to r13, final result
Add(r5,r5,r5) #Shift r5
Set(r10,0) #reset r10, the r5 copy, for new value
Moven(pc,r12,r11)
Addi(pc, pc, 3) #We're done, skip shit


#multiply
#multiply
#multiply
#multiply

#okay, we can send in r13, compare r2, the exponent, and r4, the counter. If r2 = 0, skip. r3 is 1.

Addi(r14, pc, 8) #If this is zero
Movez(pc, r14, r2)

Addi(r2, r2, 1) #add the power by 1 because....fuck itttt?

Addi(r4, r4, 1)
Sub(r5, r4, r2)
Set(r14, 22)
Sub(r14, pc, r14) #Relative to pc
Moven(pc, r14, r5) #if r5 is negative, go up.

Move(r13, r3) #Puss final wee-zult

Move(r3, r3) #Done!

"""

load(sweetjesus)
run()
