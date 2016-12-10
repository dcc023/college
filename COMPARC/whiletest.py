from bcpu import *

#while test

#"Why are we still here? Just to suffer?" ~ This class
#"The net is vast and infinite" ~ Vuchanae
#"Janus, I'm already a demon."

s2=0

s1=9

while s1 != 0:
	s2 = s2 + s1
	s1 = s1 - 1

print(s2)

whiletest = """

Set(r2,0)
Set(r1,9)

#while
Addi(r10,pc,5)
Movez(pc,r10,r1)
#body
Add(r2,r2,r1)
Subi(r1,r1,1)
Subi(pc,pc,3)
#done
Move(rout0,r2)

"""

whiletest2 = """

Set(r2,0)
Set(r1,9)

#while
Addi(r10,pc,6)
Addi(r11,pc,1)
Movez(pc,r10,r1)
#body
Add(r2,r2,r1)
Subi(r1,r1,1)
Move(pc,r11)
#done
Move(rout0,r2)

"""


load(whiletest2)
run()
