from bcpu import *




eightbitleftrotation = """

#bitwise left rotation
#only shifts by 1 bit.
#8 bit size only
Set(r1,110) #Arbitrary number.
Set(r2,255) #This is a whole string of /8/ 1s. You and this with any result and it'll make any hanging uglies fuck off (ie a ninth bit that
		#we WILL have by the end of this shabang.)
Set(r3,0b10000000) #8 bits currently. Changes depending on most significant bit.
Set(r4,0b00000001) #8 bits currently. Changes depending on least significant bit.
And(r5,r1,r3) #Find out if the leftmost bit is a 0 or 1.

#left bit shift. Shimmy it over.
Add(r1,r1,r1) #by won.

#after the left shift
#if Left most bit is 1, Right most bit becomes 1
Addi(r7,pc,4) #throw a jump right in that slut.
Movez(pc,r7,r5) #Skip to Move(r1, r1) if r5 is zero, meaning the leftmost bit is 0. Since, you know, the 9th bit will be zero anyway.
Addi(r1,r1,1) #set right most bit to 1
And(r8,r1,r2) #zero out left most bit


#else, right most bit becomes 0.
Move(r1,r1) #Skip over here if leftmost bit is 0.

#Basically:
#10010110
#Do regular shift
#100101100
#^SHIT. One bit too many,
#AND 100101100 with 11111111. Slices off the last bit, making 00101100
#Then toss a one at the end: 00101101
#Buuuut, if our original, 10010110 was instead 00010110...
#Then a bit-shift will just be:
#001011000
#The last bit is 0 anyway...so skip all that 'slice off one and add 1 to the end' shite.

"""



eightbitrightrotation = """

#bitwise right rotation
#only shifts by 1 bit.
#8 bit size only
Set(r1,22)
Set(r2,254) #Basically 11111110! If you AND that with a number, it'll slice off the rightmost bit, which we want sometimes.
Seth(r2,1) #sets r2 to 0b111111110
Set(r3,0b10000000) #8 bits currently. Changes depending on most significant bit
Set(r4,0b00000001) #8 bits currently. Changes depending on least significant bit
And(r5,r1,r4) #Find out if rightmost bit is a 0 or 1. Dat rightmost doe.



#right bit shift
Set(r9,0) #counter for division
Move(r10,r1) #copy over that there r1.
Subi(r10,r10,2) #We're dividing by 2. Remember? Minus 2 until we get a negative. OR ZERO. Which is more ideal.
Addi(r9,r9,1) #i = i + 1. Okaie dokes, that's one down. Or, if you're here again, that's another.
Addi(r11,pc,5) #skip to end of bit shift if not evenly divisible. 
Addi(r12,pc,6) #skip to end of bit shift if evenly divisble.
Moven(pc,r11,r10) #This means we hit a negative. Fuck it, we're done.
Movez(pc,r12,r10) #This means we hit zero. Rejoice! Let's get out of here. r12
Subi(pc,pc,6)	#If both the moven AND movez failed, we're taking our happy asses back up 6 instructions.

#if not evenly divisible by 2
Subi(r1,r9,1) #We hit a negative, yeah? Well...that sort of half-counted one we need to take off from r9, the counter. Slap it in r1.
Addi(pc,pc,2) #Aaaaand skip that whole 'divisible by 2' thing.

#if evenly divisible by 2
Move(r1,r9) #A zero! Hooray! Just put r9 straight into r1. Nufin' else.
#end of right bit shift


#after the right shift
#if right most bit is 1, left most bit becomes 1
Addi(r7,pc,5) #Set up a five-line skip from here...
Movez(pc,r7,r5) #Is that left-most bit 0? If so, skip this shit.
Set(r14,128) #because BCPU Addi won't go higher than 15...Oh no no no...I'm too tired to go higher than 15 right now. Goodbye.
Add(r1,r1,r14) #set left most bit to 1 (8bits). Right, that's...done by adding 128 to r1. Hey, it ain't imperical science, I'm a simple man.
And(r1,r1,r2) #zero out right most bit. Aha! You'll skip this if rightmost is 0. Because...whatever/


#else, left most bit becomes 0.
Move(r1,r1) #Here ye are.

"""

load(eightbitrightrotation)
run()

