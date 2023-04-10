num = "11111"
length = len(num)
decimal = 0
for x in num:
	#print(x, pow(2,(length - 1)))
	if ( x =="1"):
		#print(x, pow(2,(length -1)))
		decimal = int(pow(2,length-1)) + decimal
	length -= 1
print ("decimal=", decimal)