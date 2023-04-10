num = "10110001"
num_len = len(num)
print(num_len)
count_e = 0
count_o = 0
for x in range(num_len):
	if ( num[x] == "1" and x%2 == 0 ):
		count_e+=1
	elif ( num[x] == "1" and x%2 != 0 ):
		count_o+=1
print("odd position = ", count_o)
print("even position = ", count_e)
	