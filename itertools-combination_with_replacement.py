from itertools import combinations_with_replacement
s = input().split()
l=list(combinations_with_replacement(s[0],int(s[1])))
li=[]
for x in range(len(l)):
        st=l[x]
        ls=list(st)
        ls.sort()
        li.append("".join(ls))
li.sort()
for y in li:
    print(y)