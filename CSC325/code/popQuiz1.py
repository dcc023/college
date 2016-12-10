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

# Print every item from list ONLY using these funcs

def printL(al):

    while not al.nil:

        print(al.first())

        al = al.rest()

#reverse intList

def reverseL(al):

    revList = IntList()

    while not al.nil:
        revList = revList.cons(al.first())
        al = al.rest()

    return revList




#testing
printL(reverseL(al))



