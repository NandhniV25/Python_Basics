def mul_str(string,len):
    s=""
    for x in range(len):
        s+=string
    return s
def upper(n,m):
    for x in range(n//2):
        print(mul_str(".|.",2*x+1).center(m,'-'))
def middle(n,m):
    s="WELCOME"
    for x in range(n//2,n//2+1):
        print(s.center(m,'-'))
def lower(n,m):
    for x in range(n//2,0,-1):
        print(mul_str(".|.",2*x-1).center(m,'-'))
l=input()
l1=l.split(" ")
n=int(l1[0])
m=int(l1[1])
upper(n,m)
middle(n,m)
lower(n,m)