def a_split(start,end,arr):
    list_1=[]
    for x in range(start,end):
        list_1.append(arr[x])
    return list_1
arr = list(input(" Enter array list = "))
start = int(input("Start Index = "))
end = int(input("End Index ="))
list_1=a_split(start,end,arr)
print(list_1)