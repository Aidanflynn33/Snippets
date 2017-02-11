# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest3DigitNumber = 999
factor1 = largest3DigitNumber
factor2 = largest3DigitNumber
product = 0
textual = ""

while factor1 > 0:
	while factor2 > 0:
		tmp = factor1 * factor2
		if (str(tmp) == str(tmp)[::-1] and tmp > product):
			product = tmp
			textual = ("%d * %d = %d" % (factor1, factor2, product))
		factor2 -= 1
	factor1 -= 1
	factor2 = largest3DigitNumber

print(textual)
