from itertools import combinations
s=input().split()
p=[]
for x in range(int(s[1])):
    q=list(combinations(s[0],x+1))
    l=[]
    for y in range(len(q)):
        st=q[y]
        ls=list(st)
        ls.sort()
        l.append("".join(ls))
    l.sort()
    p+=l
for x in p:
    c="".join(x)
    print(c)