from functools import cmp_to_key

def cmp_As_De(x,y):
    x1=len(x)
    y1=len(y)
    if x1%2==0 and y1%2==0:
        return cmp_Des(x1,y1)
    elif x1%2!=0 and y1%2!=0:
        return cmp_As(x1,y1)
    elif x1%2==0 and y1%2!=0:
        return 1
    elif x1%2!=0 and y1%2==0:
        return -1  
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
            
a=[[1,2,3],[4,5,6],[7,8,9,10],[11],[12],[13,14]]
#print odd len first in AO and even len last in DO
a1=sorted(a, key=cmp_to_key(cmp_As_De))
print(a1)