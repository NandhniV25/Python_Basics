n = 5
for x in range(n+1):
	for y in range(n-x):
		print(" ",end="")
	for z in range(x):
		print("*",end="")
	for v in range(x+1):
		print("*",end="")
	print("")