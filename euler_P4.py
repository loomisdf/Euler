def isPalindromic(n):
	string = str(n)
	return string[::-1] == str(n)
largest = 0
print(isPalindromic(909))
for i in range(100,999):
	for j in range(100,999):
		if(isPalindromic(i*j) and i*j > largest):
			largest = i * j

print(largest)
