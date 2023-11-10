import math
def triunghi(l1,l2,l3):
    val=[l1,l2,l3]
    val.sort()
    return(l3<l1+l2)
def dreptu(l1,l2,l3):
    val=[l1,l2,l3]
    val.sort()
    return(l3==math.sqrt(l2**2+l1**2))
print(triunghi(3, 4, 5))
print(dreptu(3, 4, 5))
