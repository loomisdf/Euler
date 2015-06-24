def isDivisible(number, upper_limit):
	for i in range(1, upper_limit):
		if(i % number != 0):
			return False
i = 1
while(True):
	if(isDivisible(i, 20)):
		print(i)
		break
	i = i + 1
