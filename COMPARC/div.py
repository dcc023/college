#Division
#r3 =r2//r1 integer part
#r4=r2*r1 remainder part
#if r1 == 0, r3 = r4 == -1

from bcpu import *

div = """

Set(r3,0)
Subi(r3,r3,1) # r3 = -1
Move(r4,r3)
Addi(r10,pc,11)
Movez(pc,r10,r1) # > end
#check r2 == 0
Set(r3,0)
Set(r4,0)
Movez(pc,r10,r2) # > end

Addi(r11,pc,6) # addr of done

	Set(r3,0)
	Sub(r2,r2,r1) # < start
	Moven(pc,r11,r2)
	Addi(r3,r3,1)
	Subi(pc,pc,3) # > start

#done
Add(r4,r2,r1) # < done

Move(r3,r3)
Move(r4,r4)


"""

Set(r2,7)
Set(r1,2)
load(div)
run()
