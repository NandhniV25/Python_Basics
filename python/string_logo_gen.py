def mul_str(str,n):
    s=""
    for x in range(n):
        s+=str
    return s
def top_tri(n):
    for x in range(n):
        print(mul_str("H",2*x+1).center(2*n-1))
def bottom_tri(n):
    for x in range(n-1,-1,-1):
        print(mul_str(" ",4*n)+mul_str("H",2*x+1).center(2*n-1))
def upper(n):
    v=n+1
    for x in range(v):
        print(mul_str(" ",(n-1)//2)+mul_str("H",n)+mul_str(" ",3*n)+mul_str("H",n))
def middle(n):
    for x in range(n//2+1):
        print(mul_str(" ",(n-1)//2)+mul_str("H",5*n))      

n=int(input())
top_tri(n)
upper(n)
middle(n)
upper(n)
bottom_tri(n)                  