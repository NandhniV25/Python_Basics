t=int(input())
for x in range(t):
    a=int(input())
    aa=set(input().split())
    b=int(input())
    bb=set(input().split())
    print(aa.issubset(bb))