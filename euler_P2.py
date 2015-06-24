import math

Phi = (1 + math.sqrt(5)) / 2
phi = 1/Phi

def fib(n):
	return round((Phi**n / math.sqrt(5)) - (-phi**n / math.sqrt(5)))

n = 1
sum = 0
while fib(n) < 4000000:
	if(fib(n) % 2 == 0):
		sum += fib(n)
	n += 1
print(sum)
