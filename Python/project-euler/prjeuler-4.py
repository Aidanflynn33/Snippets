# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest3DigitNumber = 999
factor = largest3DigitNumber
product = 0

while True:
	product = largest3DigitNumber * factor
	if (str(product) == str(product)[::-1]):
		print("%i * %i = %i" % (largest3DigitNumber, factor, product))
		quit()
	factor = factor - 1
