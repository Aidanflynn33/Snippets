# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

start = 600851475143
divider = 2
listOfDividers = []
while start > 1.0:
	if (divider % 2 == 0 or start % divider != 0):
		divider += 1
	else:
		start = start / divider
		listOfDividers.append(divider)

print(listOfDividers)
