n = 5
for x in range(n):
	for y in range(n-x):
		print("*", end="")
	for z in range(y):
		print(" ",end="")
	print("")
for x in range(n):
	for y in range(x+1):
		print("*", end="")
	for z in range(y):
		print(" ",end="")
	print("")
print("--")
for x in range(n):
	for z in range(x):
		print(" ",end="")
	for y in range(n-x):
		print("*", end="")
	print("")
print("===")
for x in range(n):
	for y in range(n-x):
		print(" ",end="")
	for z in range(y):
		print("*",end="")
	print("")