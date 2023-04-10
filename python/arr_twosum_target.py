def contains(arr,target):
    b=0
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            b = arr[x] + arr[y]
            if b == target:
                return True
    return False
arr = [5,4,3,1]
target = 8
a=contains(arr,target)
print(a)

def contains(arr,target):
    set1 = set()
    for x in arr:
        c=target-x
        if c in set1:
            return True
        else:
            set1.add(x)
    return False
    
arr = [5,3,6,2]
target = 8
a=contains(arr,target)
print(a)