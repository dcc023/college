#Create a seqSearch that utilizes recursion. Practice of changing for loop
# to a recursive "loop" HOMWOK

def seqSearch(E, num, k):
    seqSearchRec(E, 0, num, k)
def seqSearchRec(E, index, num, k):
    if index >= num:
        ans = -1
    elif E[index] == k:
        ans = index
    else:
        ans = seqSearchRec(E, index + 1, num, k)
    return ans

# testing

E = [1,2,3,4,5,6,7]
print(E)
print(seqSearch(E, 10, 2))
print(len(E))
