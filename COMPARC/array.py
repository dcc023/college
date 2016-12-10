#Array

from bcpu import *


array = """

Set(r10,10) #start of our array
Set(r1,0) #data

Store(r10,r1)
Addi(r10,r10,1)
Addi(r1,r1,1)
Subi(r13,pc,3)
Subi(r2,r1,10) #array size 10
Moven(pc,r13,r2)

"""

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


load(array)
run()

#test
Set(r1,4)
Load(search,200)
run(200)
