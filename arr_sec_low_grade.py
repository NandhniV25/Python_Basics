from functools import cmp_to_key
def cmp_sort_num(x,y):
    if x[1]<y[1]:
        return -1
    elif x[1]>y[1]:
        return 1
    else:
        if x[0]>y[0]:
            return 1
        else:
            return -1
    
def sec_low(l):
    temp=l[0][1]
    nl=[]
    for x in range(1,len(l)-1):
        if temp!=l[x][1]:
            temp=l[x][1]
            break
    for x in l:
        if x[1]==temp:
            nl.append(x[0])
    return nl
if __name__ == '__main__':
    n=int(input())
    l=[]
    for _ in range(n):
        name = input()
        score = float(input())
        l.append([name,score])
    #print(l)
    la=sorted(l,key= cmp_to_key(cmp_sort_num))
    #print(la)
    a=sec_low(la)
    for x in a:
        print(x)     