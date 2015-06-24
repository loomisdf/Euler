def isPrime(n):
	if(n % 2 == 0 or n % 5 == 0):
		return False
	for i in range(3, int(n/2)):
		if(n % i == 0):
			return False
	return True

n = 600851475143
largest = 1
for i in range(1,int(n/2)):
	if(n % i == 0 and isPrime(i)):
		print(i)
		largest = i
print(largest)
