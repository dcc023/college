
def hashCode(k):
    return (5*k) % 8

#testing
for k in [1055, 1492, 1776, 1812, 1945]:
    print(hashCode(k))

print(hashCode(1492))
print(hashCode(1812)) #COLLISION, these two equal the same and 
#will be stored in the same spot. We are doing sequential search
#when we get to the "4" slot. 
