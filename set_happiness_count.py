n=input().split()
arr=input().split()
s1=set(input().split())
s2=set(input().split())
count=0
for x in arr:
    if x in s1:
        count+=1
    if x in s2:
        count-=1
print(count)