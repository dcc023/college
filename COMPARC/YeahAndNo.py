#registers in this:
#r5: Original Base
#r6: What will bit shift to be added to answer
#r7: Our 'bit mask'
#r8: Counts up to 15
#r9: Where the And gets put. Changing. After the and, use to check counter.
#r10: Holds what we end up adding, 0 or r6
#r11: Final answer to return
#r12: Holds jump value

#NOTE: r13 is the Base of the exponential. We copy it into r5 every time, so r13 is free to grow, and can come back bigger every time we do this.

Set(r11, 0) #initialize r11 as 0.
Move(r5, r13) #Copy r13 (The Copy Base), whatever it may be.
Move(r6, r5) #Copy r5 into r6. r6 will recursively bit shift.
Set(r7, 1) #put 1 into r7 for bitch shifting.
Set(r8, 0) #Counter

And(r9, r5, r7) #check first bit.
Move(r10, r6) #Assuming r9 != 0, copy r6 into r10.
Movez(r10, r9, r9) #If r9 is zero...put r9 into r10...which is 0 if r9 is 0. HAHA.
Add(r11, r11, r10) #Whatever is in r10, slap it in r11.
Add(r6, r6, r6) #Bit shift r6.
Add(r7, r7, r7) #Bit shit bitch mask
Addi(r8, r8, 1) #add one to r8

Set(r14, 16) #Set it in there. 16 

Sub(r9, r14, r8) #Check if counter's done

Subi(r12, pc, 9) #Set up jump back in 12

Movex(pc, r12, r9) #if r9, the checker, is NOT zero, take your happy ass back up.

Move(r13, r11) #Now r13 changes, so it may be used again, incrementally


*******************************************************************************************

Move(r5, r13) #r1*r2=r0
Move(r6, r1)
Set(r13, 0) #Set this to zero so it can take its new value
Set(r7,0b001) #Bitmask
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
