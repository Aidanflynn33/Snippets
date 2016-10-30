# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 386 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def diffSumOfSquaresAndSquareOfSums(number):
	sum_of_squares = 0
	sum_of_n = 0

	for i in range(0, number):
		sum_of_squares += (i+1)**2
		sum_of_n += (i+1)

	square_of_sum_n = sum_of_n**2
	result = square_of_sum_n - sum_of_squares
	print(result)

diffSumOfSquaresAndSquareOfSums(10)
diffSumOfSquaresAndSquareOfSums(10000000)


# Mathematical Method
# http://www.trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
#
#          n(n+1)(2n+1)     n^3     n^2     n
# s^2(n) = ------------ =  ----- + ----- + --- 
#              6            3       2      6
#
def sum_of_squares(n):
	return (n*(n+1)*(2*n+1))/6

# https://cseweb.ucsd.edu/groups/tatami/kumo/exs/sum/
#
#                  n(n+1)
# 1+ 2+ ... + n = --------
#                    2
#
def sum_of_n(n):
	return n*(n+1)/2

def sum_square_difference(n):
	return sum_of_n(n)**2 - sum_of_squares(n)

print(sum_square_difference(10))
print(sum_square_difference(10000000))
