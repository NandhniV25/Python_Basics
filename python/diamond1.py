n = 5
for x in range(n):
	for y in range(n-x):
		print("*", end="")
	for z in range(x):
		print(" ",end="")
	for z in range(x):
		print(" ",end="")
	for y in range(n-x):
		print("*", end="")
	print("")
for x in range(n):
	for y in range(x+1):
		print("*", end="")
	for z in range(n-x-1):
		print(" ",end="")
	for y in range(n-x-1):
		print(" ",end="")
	for z in range(x+1):
		print("*",end="")
	print("")
n = 5
def dia(char,num):
	for x in range(num):
		print(char,end="")
for x in range(n):
	dia("*",n-x)
	dia(" ",2*x)
	#dia(" ",x)
	dia("*",n-x)
	print("")
for x in range(n):
	dia("*",x+1)
	dia(" ",2*(n-x-1))
	#dia(" ",n-x-1)
	dia("*",x+1)
	print("")
