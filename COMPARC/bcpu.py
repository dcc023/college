# BCPU â“’ Dr Ben Choi
#http://www2.latech.edu/~choi/pub/bcpu.py
#http://www2.latech.edu/~choi/pub/bcpueg.py
#COME ON GUYS
#OK GUYS
# v2.1

# constains
H = 0b1111111111111111  # 16 bits
B15 = 0b1000000000000000
Err = -1

# register address
R0 = r0 = 0
R1 = r1 = 1
R2 = r2 = 2
R3 = r3 = 3
R4 = r4 = 4
R5 = r5 = 5
R6 = r6 = 6
R7 = r7 = 7
R8 = r8 = 8
R9 = r9 = 9
R10 = r10 = 10
R11 = r11 = 11
R12 = r12 = 12
R13 = r13 = 13
R14 = r14 = 14
PC = Pc = pc = 15

# data storage I/O address
Di0 = di0 = 200
Di1 = di1 = 201
Di2 = di2 = 202
Di3 = di3 = 203

Do0 = do0 = 210
Do1 = do1 = 211
Do2 = do2 = 212
Do3 = do3 = 213


# registers
R = [0 for _ in range(2**4)]

# data storage
D = [0 for _ in range(2**8)]

# instruction memory
M = [0 for _ in range(2**16)]


# printing interger + - number
def printi(d,a='',b=''):
  if d&B15: d = -(-d&H)
  if (a != '') and a&B15: a = -(-a&H)
  if (b != '') and b&B15: b = -(-b&H)
  print(d,a,b)
  

# instruction def

def Move(Rd,Ra):
  vRa = R[Ra]
  R[Rd] = R[Ra]
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa)

def Not(Rd,Ra):
  vRa = R[Ra]
  R[Rd] = (~R[Ra])&H
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa)
  
def And(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  R[Rd] = R[Ra] & R[Rb]
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Or(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  R[Rd] = R[Ra] | R[Rb]
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Add(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  R[Rd] = (R[Ra] + R[Rb])&H
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Sub(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  R[Rd] = (R[Ra] + (-R[Rb])&H)&H
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Addi(Rd,Ra,v):
  if not (v>=0 and v<=15):
    print("Value should be 0...15")
    return Err
  vRa = R[Ra]
  R[Rd] = (R[Ra] + v)&H
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, v)
  
def Subi(Rd,Ra,v):
  if not (v>=0 and v<=15):
    print("Value should be 0...15")
    return Err
  vRa = R[Ra]
  R[Rd] = (R[Ra] - v)&H
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa, v)
  
def Set(Rd,v):
  if not (v>=0 and v<=255):
    print("Value should be 0...255")
    return Err
  R[Rd] = v
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], v)
  
def Seth(Rd,v):
  if not (v>=0 and v<=255):
    print("Value should be 0...255")
    return Err
  R[Rd] = v*256 + R[Rd]%256
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], v)

def Store(Rd,Ra):
  a = R[Rd]%256
  D[a] = R[Ra]
  R[Pc] += 1
  printi(R[Rd],R[Ra])

def Load(Rd,Ra):
  vRa = R[Ra]
  a = R[Ra]%256
  R[Rd] = D[a]
  if Rd != Pc: R[Pc] += 1
  printi(R[Rd], vRa)
  
def Movez(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  if R[Rb] == 0:
    R[Rd] = R[Ra]
    if Rd != Pc: R[Pc] += 1
  else: 
    R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Movex(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  if R[Rb] != 0:
    R[Rd] = R[Ra]
    if Rd != Pc: R[Pc] += 1
  else: 
    R[Pc] += 1
  printi(R[Rd], vRa, vRb)

def Movep(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  if R[Rb]&B15 == 0:
    R[Rd] = R[Ra]
    if Rd != Pc: R[Pc] += 1
  else: 
    R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  
def Moven(Rd,Ra,Rb):
  vRa, vRb = R[Ra], R[Rb]
  if R[Rb]&B15:
    R[Rd] = R[Ra]
    if Rd != Pc: R[Pc] += 1
  else: 
    R[Pc] += 1
  printi(R[Rd], vRa, vRb)
  

# process

def printr():
  for i in range(15):
    n = R[i]
    if n&B15: n= -(-n&H)
    print('R'+str(i)+':',n)
  print('PC:', R[pc])
 
def printd(a=0, z=256):
  print('D:', end=' ')
  for n in D[a:z]:
    if n&B15: n= -(-n&H)
    print(n, end=', ')
  print()
 

def printm(a=100):
  while M[a] != 0: # 0 no instuction
    print(M[a], '['+str(a)+']')
    a += 1

def do(a=100):
  """ Execute one instruction """
  R[Pc] = a
  if M[a] != 0: # 0 no instuction
    print(M[a], '['+str(a)+']')
    eval(M[a])
  
def run(a=100):
  """ Run program """
  R[Pc] = a
  while M[a] != 0: # 0 no instuction
    print(M[a], '['+str(a)+']')
    ret = eval(M[a])
    if ret == Err:
      print("*** Run stopped due to above error ***")
      break
    a = R[Pc]

def load(ps, a=100):
  """ Load program into memory """
  pl = ps.splitlines()
  pl = [s.strip() for s in pl]
  pl = [s for s in pl if s[:2].istitle()]
  for s in pl:
    M[a] = s
    a += 1
  M[a] = 0 # end

# ready 
print("*** BCPU startup completed ***")



# testing 

testprog = """

Set(R1,7)

# logical operation
Move(R2, R1)  # R2=R1
Not(R3, R2) # R3=NOT(R2)
And(R4, R1, R1) # R4= R1 AND R1
Or(R5, R3, R4) # R5 = R3 OR R4

  # arithmetic operation
  Add(R7, R1, R1) # R7=R1+R1
  Sub(R8, R7, R2) # R8 = R7 - R2
  Addi(R9, R8, 2) # R9=R8+2
  Subi(R10, R9, 0x3) # 0x hex no.

Set(R11, 42)  # R11=42
Seth(R12, 0b1111) # 0b bin no.

  Store(R1, R11) # R1 is address to store data in R11
  Load(R6,R1) # R6 is data load from address R1
  
# conditional operation
Movez(R13, R2, R0) # R12=R2 if R0 = 0
Movex(R13, R3, R1) # R13=R3 if R1 != 0
Movep(R14, R3, R1) # R14=R3 if R1>=0
Moven(R10, PC, R3) # R10 = PC if R3<0

"""

# testing process
"""
print("...Loading asm program into memory...")
load(testprog)
printm()

print("...Execute one instruction...")
do()
printr()

print("...Runing test program...")
run()
printr()
printd()

"""

