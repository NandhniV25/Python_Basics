n = 10
if n==1:
	print (n, "is neither prime nor composite number")
elif n>1:
	for x in range(2,n):
		if(n%x==0):
			print("not prime",n)
			break
	else
		print("prime",n)
else:
	print("n is less than 1")