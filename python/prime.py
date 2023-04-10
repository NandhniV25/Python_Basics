n = 55
if (n==1):
	print(n, " is neither Prime nor Composite number")
elif (n>1):
	for x in range(2,n):
		if ( n % x == 0 ):
			print("not prime", n)
			print( x, " X ",n//x," = ", n) # n//x ==quotient 
			break
	else:
		print("prime",n)
else:
	print(n, " is not a prime number")
    
 """   
def prime(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True
n=11
a=prime(n)
print(a)"""
    