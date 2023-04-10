a = list(input("Enter array list ="))
print(a)
a_len = len(a)
print(a_len)
sum = 0
for x in range(a_len):
    sum = int(a[x]) + sum
print ("array sum =",sum)