# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import sys

def findBruteForce(tripletFor):
	for a in range(tripletFor):
		for b in range(a+1, tripletFor):
			for c in range(b+1, tripletFor):
				r1 = a + b + c
				r2 = a**2 + b**2
				r3 = c**2
				if r1 == tripletFor and r2 == r3:
					print("%d %d %d" % (a, b, c))
					return

findBruteForce(1000)

# Mathematical Method
# https://en.wikipedia.org/wiki/Pythagorean_triple

# Euclid's formula
# m > n > 0
# a = 2mn, b = m^2 - n^2 , c = m^2 + n^2

import math

def findViaEuclid1(tripletFor):
	for n in range(0, tripletFor):
		for m in range(n+1, tripletFor):
			for k in range(1, tripletFor):
				if math.gcd(m, n) == 1:
					a = k*(2*m*n)
					b = k*(m**2-n**2)
					c = k*(m**2+n**2)
					r = a + b + c
					if r == tripletFor and a < b and b < c:
	 					print("%d %d %d" % (a, b, c))
	 					return

findViaEuclid1(1000)
