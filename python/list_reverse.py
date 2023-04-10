a = list(input("enter array number list ="))
print(a)
reverse= []
a_len=len(a)
print(a_len)
for x in range(a_len-1,-1,-1):
    reverse.append(a[x])
print("reverse= ",reverse)