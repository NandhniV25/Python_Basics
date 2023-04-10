e=int(input())
arr=set(map(int,input().split()))
f=int(input())
arr1=set(map(int,input().split()))
arr2=arr.union(arr1)
count=0
for x in arr2:
    count+=1
print(count)


=================
e=int(input())
arr=set(map(int,input().split()))
f=int(input())
arr1=set(map(int,input().split()))
arr2=arr.intersection(arr1)
count=0
for x in arr2:
    count+=1
print(count)


=================
e=int(input())
arr=set(map(int,input().split()))
f=int(input())
arr1=set(map(int,input().split()))
arr2=arr.difference(arr1)
count=0
for x in arr2:
    count+=1
print(count)


==================
e=int(input())
arr=set(map(int,input().split()))
f=int(input())
arr1=set(map(int,input().split()))
arr2=arr.symmetric_difference(arr1)
#print(arr2)
count=0
for x in arr2:
    count+=1
print(count)


===========================

n=int(input())
arr=set(map(int,input().split()))
m=int(input())
sum=0
for x in range(m):
    s=input().split()
    #print(s[0],s[1])
    if s[0]=="intersection_update":
        s1=set(map(int,input().split()))
        arr.intersection_update(s1)
        #print(arr)
    elif s[0]=="update":
        s1=set(map(int,input().split()))
        arr.update(s1)
        #print(arr)
    elif s[0]=="symmetric_difference_update":
        s1=set(map(int,input().split()))
        arr.symmetric_difference_update(s1)
        #print(arr)
    elif s[0]=="difference_update":
        s1=set(map(int,input().split()))
        arr.difference_update(s1)
        #print(arr)
for x in arr:
    sum+=x
print(sum)