from functools import cmp_to_key

def cmp_As_De(x,y):
    if x[0]!="a" and y[0]!="a":
        return cmp_As(x,y)
    elif x[0]=="a" and y[0]=="a":
        return cmp_Des(x,y)
    elif x[0]!="a" and y[0]=="a":
        return -1
    elif x[0]=="a" and y[0]!="a":
        return 1
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
            
a=['asd','venkat','nivi','nandhu','viyan','love','app','apple']
#strings without starting with 'A' in A.O but ending A(remaining) with D.O
a1=sorted(a, key=cmp_to_key(cmp_As_De))
a2=sorted(a, key=cmp_to_key(cmp_As))
a3=sorted(a, key=cmp_to_key(cmp_Des))
print(a1)
print(a2)
print(a3)
