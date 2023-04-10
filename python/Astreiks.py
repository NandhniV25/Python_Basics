n = 5
for x in range(n):
	for y in range(n-x):
		print("*",end="")
	for z in range(n-x):
		print(" ",end="")
	print("")
for x in range(n):
	for y in range(x+1):
		print("*",end="")
	print("")