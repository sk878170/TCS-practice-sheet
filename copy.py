l=[1,2,3,4,5]
l1=l
print("l:",l)
print("l1:",l1)

l.append(6)
print("l:",l)
print("l1:",l1)

l2=l.copy()
l.append(7)
print("l:",l)
print("l2:",l2)

import copy
l3=[[1,2,3],[4,5,6]]
l4=copy.deepcopy(l3)
l3[0][0]=100
print("l3:",l3)
print("l4:",l4)

