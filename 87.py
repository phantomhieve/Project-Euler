#   #   #   #   #   #   #
#  Author phantomhive   #
#      25-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from itertools import product
from prime import generate_prime
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write

# Start time
START = time()
LIMIT = 5*(10**7)
primes  = list(generate_prime(LIMIT = LIMIT))
numbers = set()

## need to optimize it using dp
def find_all(primes, size, iteration=0, value=0):
    if iteration==3:
        if value < LIMIT: 
            numbers.add(value)
        return 
    for i in xrange(size):
        new_value = value + pow(primes[i], iteration+2)
        if new_value < LIMIT:
            find_all(primes, size, iteration+1, new_value)
        else: break

find_all(primes, len(primes))
ans = len(numbers)
cout('Total count: %d\n'%(ans))


# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))