# seqSearch v2

def seqSearch(key,L):
  if key in L:
    ans = L.index(key)
  else:
    ans = -1
  return ans

# testing
L = [1,3,5,7,9,11]
key = 7

print(seqSearch(key,L))
