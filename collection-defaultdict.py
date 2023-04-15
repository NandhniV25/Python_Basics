n,m=list(map(int,input().split()))
l1,l2=[],[]
for x in range(n):
    s1=input()
    l1.append(s1)
for x in range(m):
    s2=input()
    l2.append(s2)
#print(l1,l2)
d={}
count=1
for x in range(len(l1)):
    if l1[x] not in d:
        d[l1[x]]=[x+1]
    else:
        d[l1[x]].append(x+1)
        
#print(d)
for x in l2:
    if x in d.keys():
        for y in d[x]:
            print(y,end=" ")
        print()
    else:
        print("-1")
		
		
		================
from collections import defaultdict

n,m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1) 

for l in range(m):
    print(*d.get(input(),[-1]))