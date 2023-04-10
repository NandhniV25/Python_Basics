def get_prefix(l1,l2):
    l3=""
    for x in range(min(len(l1),len(l2))):
        if l1[x] == l2[x]:
            l3+=l1[x]
        else:
            break
    print(l3)
s1 = str(input("Enter String1 = "))
s2 = str(input("Enter String2 = "))
get_prefix(s1,s2)