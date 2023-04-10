string = str(input("enter string = "))
for x in range(len(string)):
    count = 0
    for y in range(0,len(string)):
        if string[x] == string[y]:
            count+=1
    print("count of character of {0} is {1} ".format(string[x],count))
	string = input("enter string = ")
print(string)
dict={}
for x in range(len(string)):
    if string[x] in dict:
        dict[string[x]] +=1
    else:
        dict[string[x]] = 1
print(dict)

str = input("enter string")
dict={}
for x in str:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
print(dict)

str1=""
str2=""
for x in dict.keys():
    if dict[x] ==1:
        str1 += x
for x in dict.keys():
    str2 += x
print(str1)
print(str2)