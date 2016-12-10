from bcpu import *

#test for loop

s2 = 0
for s1 in range(10): #s1 = 0,1,2,3,...9
	s2 = s2 + s1
print(s2)

#"The net is vast and infinite" ~ Vouchinae
#"Guys?" ~ Ben Choi A.K.A. "Big Ben" A.K.A. "Choi of the East"

fortest = """

Set(r2,0)

Set(r1,0) #i=0
#begin loop
Add(r2,r2,r1)

Addi(r1,r1,1) #i++
Subi(r3,r1,10)
Subi(r10,pc,3)
Moven(pc,r10,r3) 

Move(rout0,r2)


"""



load(fortest)
run()
