def one_list2(l1,l2):
    ans=[]
    for x in l1:
        for y in l2:
            a=x.copy()
            a.append(y)
            ans.append(a)
    return ans
k=list(map(int,input().split()))
val=[[]]
for x in range(k[0]):
    l=list(map(int,input().split()))
    val=one_list2(val,l)
m=[]
ans = {}
for x in val:
    c=0
    for y in x:
       c+=(y**2) 
    m.append(c%k[1])
    ans[c%k[1]] = x
print(ans[max(m)])
print(max(m))
