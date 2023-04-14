from itertools import product
a=list(map(int,input().split()))
#print(a)
b=list(map(int,input().split()))
#print(b)
c=tuple(product(a,b))
for x in c:
    print(x, end=" ")
