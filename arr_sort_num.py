from functools import cmp_to_key

def cmp(x,y):
    l1=len(str(x))
    l2=len(str(y))
    if l1>l2:
        return -1
    elif l2>l1:
        return 1
    #return cmp_As(x,y)
    if x<y:
        return -1
    else:
        return 1
def cmp_As(x,y):
        if x<y:
            return -1
        else:
            return 1
def cmp_Des(x,y):
        if x>y:
            return -1
        else:
            return 1
            
a=[1,2,3,4,11,123,12,121]
a1=sorted(a, key=cmp_to_key(cmp))
a2=sorted(a, key=cmp_to_key(cmp_As))
a3=sorted(a, key=cmp_to_key(cmp_Des))
print(a1)
print(a2)
print(a3)
