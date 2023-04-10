def get_min(arr):
    a_l=len(arr)
    prev=arr[0]
    for x in range(a_l-1):
        if prev>arr[x+1]:
            prev=arr[x+1]
    return prev
def form_num(a,a1):
    if a<a1:
        return a*10+a1
    else:
        return a1*10+a
arr=[5,4,3,2,7]
arr1=[5,4,3,7]
a=get_min(arr)
print(a)
a1=get_min(arr1)
print(a1)
b=form_num(a,a1)
print(b)