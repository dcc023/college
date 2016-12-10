def binarySearch(array, key): #initially called func, so we can save a temp value without worries of it getting reassigned during recursion.
  temp = None
  return binSearch(array, key, temp) #call our recursive func
def binSearch(array, key, temp):
  print('step')
  ind = int(len(array)/2)
  if (ind+1) > len(array): #if out of range
    return -1
  elif array[ind] == key: #if our indexed value is equal to the key
    if temp == None: #to make sure we dont add a nonetype to an int
      temp = 0
    return temp + ind #return index
  elif ind == 0: #if the array is empty
    return -1
  else:
    if array[ind] < key:#if the indexed value is less than the key
      if temp == None:
        temp = 0
      temp += + ind + 1 #to hold the original index for later use
      array = array[(ind + 1):] #chop off first half of array
      return binSearch(array, key, temp) #call itself
    else: #if indexed value is greater than the key
      array = array[:ind] #chop off latter half of array
      return binSearch(array, key, temp) #call itself

# testing

L = [ n for n in range(100)]
key = 0
print('input = ',L , key)
print(binarySearch(L,key)) 
