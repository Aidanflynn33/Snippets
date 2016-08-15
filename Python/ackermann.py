#!/usr/bin/env python3
# https://de.wikipedia.org/wiki/Ackermannfunktion


# definition by Ackermann:
# alpha(a, n) = 0, if n = 0
#               1, if n = 1
#               a, if n > 1
def alpha(a, n):
    if n is 0:
        return 0
    elif n is 1:
        return 1
    elif a > n:
        return a


# phi(a, b, 0)     = a + b
# phi(a, 0, n + 1) = alpha(a, n)
# phi(a, b+1, n+1) = phi(a, phi(a, b, n + 1), n)
def phi(a, b, n):
    if n is 0:
        return a + b
    elif b is 0:
        return alpha(a, n - 1)
    else:
        return phi(a, phi(a, b - 1, n), n - 1)

print(phi(4, 3, 0))
print(phi(4, 0, 2))
print(phi(4, 1, 2))
print("-"*80)


# Definition by Peter
# a(0, m)          = m + 1
# a(n + 1, 0)      = a(n, 1)
# a(n + 1, m + 1)  = a(n, a(n + 1, m))
def a(n, m):
    if n is 0:
        return m + 1
    elif m is 0:
        return a(n - 1, 1)
    else:
        return a(n - 1, a(n, m - 1))


print(a(0, 2))
print(a(1, 0))
print(a(3, 2))
print("-"*80)
