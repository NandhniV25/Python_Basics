from collections import Counter
k=int(input())
arr=input().split()
a=Counter(arr)
for x in a.keys():
    if a[x]==1:
        print(x)
        break