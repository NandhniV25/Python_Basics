from collections import Counter
x=int(input())
size=Counter(map(int,input().split()))
customer=int(input())
cash=0
for x in range(customer):
    si,am=list(map(int,input().split()))
    if si in size and size[si]>0:
        cash+=am
        size[si]-=1
print(cash)

=====================

x=int(input())
s=list(map(int,input().split()))
c=int(input())
amount=0
for x in range(c):
    si,am=list(map(int,input().split()))
    if si in s:
        s.remove(si)
        amount+=am
print(amount)
    