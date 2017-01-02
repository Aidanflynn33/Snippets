# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math
import sympy

def sumOfPrimesBelow(maxNumber):
	adder = 0
	for i in range(2, maxNumber):
		if sympy.isprime(i):
			adder += i
	return adder


# Try Lambda
def sumOfPrimesBelowUsingLambda(maxNumber):
	return sum(list(filter(lambda x: sympy.isprime(x), list(range(0, maxNumber)))))


print(sumOfPrimesBelow(20))
print(sumOfPrimesBelow(2000000))

print(sumOfPrimesBelowUsingLambda(20))
print(sumOfPrimesBelowUsingLambda(2000000))