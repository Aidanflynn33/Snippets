# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
		return False
    return True

def getPrimeNumber(position):
	numbers = []
	number = 0
	while len(numbers) < position:
		
		if is_prime_number(number):
			numbers.append(number)

		number += 1

	print("Prime number on position %d is %d." % (position, numbers[position-1]))

getPrimeNumber(6)
getPrimeNumber(10001)
