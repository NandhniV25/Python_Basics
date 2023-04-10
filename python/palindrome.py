def pali(string):
    len1=int(len(string)/2)
    for x in range(len1):
        if string[x] != string[len(string)-x-1]:
            return False
    return True
string = input("enter String = ")
a=pali(string)
print(a)