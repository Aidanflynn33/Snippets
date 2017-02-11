# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Brute Force Method
def smallestMultiple(min, max):
	if min < 0 or max < min:
		return

	number = 0
	while True:
		number += 1
		found = []
		for i in range(min, max):
			if number % (i+1) == 0:
				found.append(True)
		if len(found) == (max - min):
			break
	
	print(number)

smallestMultiple(0, 5)
smallestMultiple(0, 10)
smallestMultiple(0, 15)
smallestMultiple(0, 20)
smallestMultiple(0, 100)


# Mathematical Method
# Least Common Multiple: https://en.wikipedia.org/wiki/Least_common_multiple
from itertools import chain

def factorizePrimes(n):
    primes = []
    if n <= 2:
        return primes
    for i in chain([2], range(3, n//2 + 1, 2)):
        while n % i == 0:
            primes.append(i)
            n = n // i
        if i > n:
            break
    if len(primes) == 0:
        primes.append(n)
    return primes

def LCM(min, max):
	primesDict = {}
	for i in range(min, max):
		primes = factorizePrimes(i+1)
		for value in set(primes):
			if value not in primesDict:
				primesDict[value] = primes.count(value)
			else:
				if primesDict[value] < primes.count(value):
					primesDict[value] = primes.count(value)

	result = 1;
	for key, value in primesDict.items():
		result *= key**value
	
	print(result)

LCM(0, 5)
LCM(0, 10)
LCM(0, 15)
LCM(0, 20)
LCM(0, 100)
