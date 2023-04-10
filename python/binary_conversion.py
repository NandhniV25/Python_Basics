n = 10
binary = ""
while n >= 1:
	binary = str(n%2) + binary
	n = n//2
    
print ("binary =" + binary)