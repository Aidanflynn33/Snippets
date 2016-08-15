#!/usr/bin/env python3
# https://de.wikipedia.org/wiki/Fibonacci-Folge


# f_1 = f_2 = 1                     Anfangswerte
# f_n = f_(n-1) + f_(n-2)           n > 2
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 50):
    print("fibonacci of %d is %d" % (i, fib(i)))
