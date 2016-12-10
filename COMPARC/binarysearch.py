#binary search

from bcpu import *

binarysearch = """

Set(r9,0) #Final result [100]
Subi(r9,r9,1) #[101]

#build the array
Set(r10,0) #start of our array at position 0 [102]
Set(r1,13) #data starts at 13 [103]
Set(r14,0) #Counter, because I'm shite, Azzy [104]
Store(r10,r1)  #[105]
Addi(r10,r10,1) #[106]
Addi(r1,r1,5) #incriments by 5 [107]
Addi(r14,r14,1) #[108]
Subi(r13,pc,4) #[109]
Subi(r2,r14,10) #array size 10, going off counter r15. r15 starts at 0, increments by one every cycle. If r15 - 10 is negative, put r13 (pc-4) into pc and do anuvva. [110]
Moven(pc,r13,r2) #[111]
#array is built

#set up search stuff
Move(r3,r2) #Left side of array (L) [112]
Move(r4,r10) #Right side of array (R) [113]
Set(r5,0) #Array position being searched [114]
#clear registers not being used at the moment
Set(r1,0) #[115]
Set(r2,0) #[116]
Set(r10,0) #[117]
Set(r13,0) #[118]
Set(r14,0) #[119]

#r3 is L and r4 is R

#find the middle of the array
Move(r5,r4) #[120]
Move(r6,r3) #[121]
Subi(r5,r5,1) #[122]
Addi(r6,r6,1) #[123]
Sub(r7,r6,r5) #test to see if the middle is found [124]
Subi(r8,pc,3) #[125]
Moven(pc,r8,r7) #goto beginning of loop (line 122) if r3-r4 is negative [126]
Move(r0,r5) #r0 now holds the middle value [127]

#clear registers
Set(r5,0) #[128]
Set(r6,0) #[129]
Set(r8,0) #[130]

#check if value at middle index == target value
Load(r5,r0) #load value at index r0 and store in r5 [131]
Sub(r6,r5,r12) #[132]
Movez(r9,r0,r6) #[133]

#using that check...

#if middle value < target value
Addi(r7,r0,1) #[134]
Moven(r3,r7,r6) #If m > target, then set L=m+1 #[135]
Set(r7,0) #clear register [136]
Set(r8,18) #temporary fix for goto instruction [137]
Sub(r7,pc,r8) #[138]
Set(r8,0) #clear register [139]
Moven(pc,r7,r6) #[140] goto instruction at line 120

#clear registers
Set(r6,0) #[141]
Set(r7,0) #[142]

#if middle value > target value
Sub(r6,r12,r5) #[143]
Subi(r7,r0,1) #If target > m, then set R=m-1 [144] obsolete line
Moven(r4,r0,r6) #[145]
Set(r7,0) #clear register [146]
Set(r8,28) #[147]
Sub(r7,pc,r8) #[148]
Set(r8,0) #[149]
Moven(pc,r7,r6) #[150]






"""

Set(r12,23)
load(binarysearch)
run()
printd()
printr()
