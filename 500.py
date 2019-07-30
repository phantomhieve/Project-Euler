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
from time import time
from prime import generate_prime
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()

MOD = 500500507
primes = list(generate_prime(LIMIT=10**7))
heapify(primes)
iteration, ans = 500500, 1
for i in xrange(iteration):
    value = heappop(primes)
    ans = (ans*value)%MOD
    heappush(primes, value*value)
cout("The numbes is: %d\n"%(ans))

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))


