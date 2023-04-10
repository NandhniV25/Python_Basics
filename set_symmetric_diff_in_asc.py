m=int(input())
arr = set(map(int, input().split()))
n=int(input())
arr1 = set(map(int, input().split()))
result=[]
for x in arr:
    if x not in arr1:
        result.append(x)
for x in arr1:
    if x not in arr:
        result.append(x)  
result.sort()
for x in result:      
    print(x) 