#Stack

from bcpu import *

stack = """

Set(r10,10) #start addr of my stack

#push 7
Addi(r10,r10,1)
Set(r1,7)
Store(r10,r1)

#push 12
Addi(r10,r10,1)
Set(r1,12)
Store(r10,r1)

#pop into r2
Load(r2,r10)
Subi(r10,r10,1)

#pop into r3
Load(r3,r10)
Subi(r10,r10,1)

#check empty
Subi(r6,r10,10)
#check if r6 == 0


"""


load(stack)
run()
printd()
