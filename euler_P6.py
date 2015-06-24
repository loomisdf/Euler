def sum_of_squares(rng):
	return sum([x**2 for x in range(rng)])

def square_of_sum(rng):
	return sum(range(rng))**2

print(square_of_sum(101) - sum_of_squares(101))
