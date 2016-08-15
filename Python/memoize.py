# Memoisation
# https://de.wikipedia.org/wiki/Memoisation
import time

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


start_time = time.time()
for i in range(25, 45):
    print("%d %d" % (i, fib(i)))
print("--- %s seconds ---" % (time.time() - start_time))


memo = dict()
def fib_memoize(n):
    if n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib_memoize(n-1) + fib_memoize(n-2)
        return memo[n]


start_time = time.time()
for i in range(25, 45):
    print("%d %d" % (i, fib_memoize(i)))
print("--- %s seconds ---" % (time.time() - start_time))
