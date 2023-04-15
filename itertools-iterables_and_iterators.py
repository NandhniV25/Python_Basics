from itertools import combinations
n=int(input())
s=list(input().split())
k=int(input())
l=list(combinations(s,k))
#print(l)
count=0
for x in l:
    if 'a' in x:
        count+=1
#print(count)
print(format(count/len(l),".3f"))
