# Mathematical Method
# Euclidean Algorithm: https://en.wikipedia.org/wiki/Euclidean_algorithm


# The euclidean algorithm can be used to find the greatest common divisor (gcd)
def gcd(a, b):
    if b == 0:
       return a; 
    else:
       return gcd(b, a % b);

# Using the gcd we can create the least common multiplier (lcm)    
#
#                 |a*b|
# lcm(a, b) = --------------
#               gcd(a, b)      
def lcm(a, b):
	return a*b / gcd(a, b)


for i in range(0, 20):
	print("a = %s, b = %s, lcm = %s, gcd = %s" % (i+1, 20, lcm(i+1, 20), gcd(i+1, 20)))
