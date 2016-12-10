# BCPU testing

from BCPU import *

testpc = """

Set(r1,1) #200
Set(pc, 203) #201 goto 203
Set(r2, 2) #202
Set(r3, 3) #203

"""

load(testpc, 200)
run(200)

# testing process

print("...Loading asm program into memory...")
load(testpc)
printm()


print("...Running test program...")
run()
printr()
