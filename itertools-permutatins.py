from itertools import permutations
s=input().split()
p=list(permutations(s[0],int(s[1])))
p.sort()
for x in p:
    print("".join(x))