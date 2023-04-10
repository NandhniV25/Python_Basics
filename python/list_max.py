a = list(input("enter array number list ="))
print(a)
a_len=len(a)
print(a_len)
max = int(a[0])
for x in range(1,a_len):
    if int(a[x]) > max:
        max = int (a[x])
print("max = ",max)