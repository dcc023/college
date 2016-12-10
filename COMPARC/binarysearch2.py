#Array

from bcpu import *


array = """

Set(r10,10) #start of our array
Set(r1,10) #data

Store(r10,r1)
Addi(r10,r10,1)
Addi(r1,r1,1)
Subi(r13,pc,3)
Set(r2,20)
Sub(r2,r1,r2) #array size 10
Moven(pc,r13,r2)

"""

#set specific bits to a 0 or 

#seq search
#search a number call key in an array
#if found, return index, else return -1

#assign r1 == key, r3 == answer

#test
Set(r1,4)

#begin
search = """

Set(r3,0)
Subi(r3,r3,1) #setting r3 = -1
Set(r11,0) #index


Set(r10,10) #start of array
Load(r2,r10) #loop here
Sub(r5,r2,r1) #compare
Addi(r13,pc,7)
Movez(pc,r13,r5) #break goto found

Addi(r10,r10,1) #address
Addi(r11,r11,1) #index
Subi(r12,r11,10) #size array 10
Subi(r14,pc,7)
Moven(pc,r14,r12)

#check found
Movez(r3,r11,r5)




"""

key = 7
ans = -1

L = [n for n in range(10)]


first = 0
last = 9
done = False

while not done:
	mid = last - first
	if mid < 0:	
		done = True
		break

	mid = mid//2
	mid = mid + first

	print("first, last",first,last)
	print("mid",mid)
	
	test = key - L[mid]

	if test == 0:
		ans = mid
		done = True
		break

	if test > 0:
		first = mid + 1

	if test < 0:
		last = mid - 1

print(ans)

binarysearch = """

Set(r1,10) #key

Set(r3,0) 
Subi(r3,r3,1) #ans = -1

Set(r4,10) #array start
Set(r5,19) #array end

Move(r6,r4) #first
Move(r7,r5) #last

Addi(r13,pc,1) #start while label

Sub(r10,r7,r6) #mid = last - first

Set(r12,20)
Add(r12,pc,r12) #done addr
Moven(pc,r12,r10) #goto done

#mid // 2
Set(r9,0)
	Subi(r10,r10,2)
Addi(r11,pc,4) #skip to end of //
Moven(pc,r11,r10)
	Addi(r9,r9,1)
Subi(pc,pc,4)
#end of div

Add(r10,r6,r9) #mid = first + mid//2

Load(r2,r10)
Sub(r8,r1,r2) #test = key - L[mid]

Sub(r9,r10,r4) #index of mid
Movez(r3,r9,r8) #? == 
Addi(r12,pc,7) #done addr
Movez(pc,r12,r8) #goto done

Addi(r9,r10,1)
Movep(r6,r0,r8) #test > 0

Subi(r0,r10,1)
Moven(r7,r0,r8) #test < 0

Move(pc,r13) #loop back to start of while

Move(r3,r3)

"""

load(array)
run()
printd()
load(binarysearch,200)
run(200)
