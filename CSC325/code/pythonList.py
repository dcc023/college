# intList def

class IntList:
    def __init__(self, iL = []):
        self.aList = iL
        
    def cons(self, newElem):
        return IntList([newElem] + self.aList[:])
    
    def first(self):
        return self.aList[0]

    def rest(self):
        return IntList(self.aList[1:])

    @property
    def nil(self):
        return len(self.aList) == 0
        
    def __str__(self):
        return str(self.aList)


# def object

al = IntList()

al = al.cons(7)
al = al.cons(6)
al = al.cons(5)
al = al.cons(4)

print(al.first())
print(al.rest())
print(al.nil)

#-----------------------------------------------------------

print("Print list!!")

# Print every item from list ONLY using these funcs

def printL(al):

    while not al.nil:

        print(al.first())

        al = al.rest()

printL(al)

#-----------------------------------------------------------

#HW assuming int list, that could be empty or contian something, task is to find whether a key is in there or not. If there, return true, if not return  false.
def findKey(al, key):
    
    ans = False
    while not al.nil:
        
        if (al.first() == key):
            ans = True
            break

        al = al.rest()
    
    return ans #ONE WAY OUT

#Testing!

print(findKey(al, 5))

#-----------------------------------------------------------
#recursive keysearch
def rfindKey(al, key):
    
    if al.nil:
        ans = False
    elif al.first() == key:
        ans = True
    else:
        al = al.rest()
        ans = rfindKey(al,key)

    return ans

#testing
print(rfindKey(al, 4))
print(rfindKey(al, 9))
print(rfindKey(al, 1))
print(rfindKey(al, 7))

#thanks josh black-feathered for the code review!

#-----------------------------------------------------------

#INCLASS VERSION OF RECURSIVE CODE
def findKeyR(key,al):

    ans = False
    if not al.nil:
        if key == al.first():
            ans = True
        else:
            ans = findKeyR(key,al.rest())
    return ans

print(findKeyR(6,al))

#-----------------------------------------------------------

#HW Recursively Delete a key (just once) from the list.

#def delKey(al, key):  This delKey was pointless, Im dumb
#    temp = None
#    return delKeyRun(al,key,temp)

def delKey(al, key):
    if al.nil:
        ans = al
    elif al.first() == key:
        ans = al.rest()
    else:
        temp = delKey(al.rest(), key)
        ans = temp.cons(al.first())
    return ans

#testing
print(delKey(al, 4))
print(delKey(al, 5))
print(delKey(al, 6))
print(delKey(al, 8))
nl = delKey(al, 6)
print(nl)
nl = delKey(nl, 4)
print(nl)

#-------------------------------------------------------------
#INCLASS DELETE CODE

def delete(key, al):
    if al.nil:
        nl = IntList()
    elif key == al.first():
        nl = al.rest()
    else:
        tl = delete(key, al.rest())
        nl = tl.cons(al.first())
    return nl
    


# POP QUIZ: Define a function to return a IntList 
# that is the result of inserting a int i, before another int key
# given an original IntList called al.

def insert(i, key, al):
    if al.nil:
        nl = IntList()
    elif key == al.first():
        nl = al.cons(i)
    else:
        tl = insert(i, key, al.rest())
        nl = tl.cons(al.first())
    return nl

#testing

print(insert(2,4,al))
print(insert(5,5,al))
print(insert(8,8,al))



