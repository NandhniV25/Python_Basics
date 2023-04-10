n=int(input())
s=set(map(int,input().split()))
m=int(input())
sum=0
for x in range(m):
    ss=input().split()
    if ss[0]=="pop":
        l = list(s)
        s.discard(l[0])
    elif ss[0]=="remove" and int(ss[1]) in s:
        s.remove(int(ss[1]))
    elif ss[0]=="discard":
        s.discard(int(ss[1]))
for x in s:
    sum+=x
print(sum)
