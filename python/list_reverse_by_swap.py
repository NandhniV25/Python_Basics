n = list(input("Enter list items = "))
print(n)
n_len = len(n)
print(n_len)
temp = 0
for x in range(int(n_len/2)):
    temp = n[n_len-1-x]
    n[n_len-1-x] = n[x]
    n[x] = temp
print(n)

def rev(n):
    temp = 0
    n_len = len(n)
    for x in range(int(n_len/2)):
        temp = n[n_len-1-x]
        n[n_len-1-x] = n[x]
        n[x] = temp
n = list(input("Enter list items = "))
print(n)
rev(n)
print(n)