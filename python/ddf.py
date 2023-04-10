def fact(a):
	if(a>=1):
		factorial = a * fact(a-1)
		return factorial
	else:
		print("num less than 1")

d = fact(3)
print("factorial of", n,"=" , d)