string = "venky weds apple egg rat ink"
list = []
string1=""
vowels=['a','e','i','o','u']
list =string.split(" ")
print(list)
a=len(list)
print(a)
for x in range(a):
   # print(list[x][0])
    if list[x][0] in vowels:
        list[x]=list[x][1:]+list[x][0] 
    list[x] = list[x]+"ma"
    for y in range(x+1):
        list[x] =list[x]+"a"
print(list)
string1=" ".join(list)
print(string1)