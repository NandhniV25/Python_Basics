def mylist(n):
	list = []	
	for x in range(n):
		val = str(x)
		if x%3==0 and x%5==0:
			val+="venkat"
		elif x%5 ==0:
			val+="nandhu"
		elif x%3==0:
			val+="vn"
		list.append(val)
	return list
	
num = mylist(10)
print(num)