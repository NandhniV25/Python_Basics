def ismonotonic(a):
    x=[]
    y=[]
    x.extend(a)
    y.extend(a)
    x.sort()
    y.sort(reverse=True)
    if x==a or y==a:
        return True
    return False
a = [6,5,4,3]
b = ismonotonic(a)
print(b)