name = "venkat"
reverse = ""
i = 0
while i < len(name):
	#print(reverse)
	reverse = name[i] + reverse
	i+=1
print (reverse)

reverse2 = "" 
for x in name:
	reverse2 = x + reverse2
print(reverse2)

reverse3 = ""
for x in range(0,len(name)):
	reverse3 = name[x] + reverse3
print(reverse3)