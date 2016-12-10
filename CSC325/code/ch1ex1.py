#GENERAL PYTHON

# L = [1,2,3,4,5] #Initializing a list

# L[1] #search for specific value in list, starting from 0.

# for i in L: #for each i in L, a for loop in python
#   print(i)  #prints all values in list L

# list(range(5)) #will print example array up to 5-1. (n-1)

# len(L) #will print out the length of list L

# for i in range(len(L)): #does the same as (for i in L)
#   print(L[i])

# First In Class Example, searching unordered list for K.
#-------------------------------------------------------

#input data
L = [2,3,5,6,7] #array to be searched
key = 5 #desired value

#steps
ans = -1 #default to failure
for i in range(len(L)):  #search through every value in L
  if L[i] == key:  #compare each value to the value of key
    ans = i	#set ans to index then break free, as to not waste
    break
print(ans) #print the ans

# Create In Function Form
#---------------------------------------------------------

def seqSearch(key, L):
  ans = -1 
  for i in range(len(L)):  
    if L[i] == key:  
      ans = i	
      break
  return ans 

print(seqSearch(key, L))


