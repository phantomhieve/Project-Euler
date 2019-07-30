#   #   #   #   #   #   #
#  Author phantomhive   #
#      24-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from time import time
from prime import generate_prime_sieve
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
LIMIT = 10**8
prime_sieve = generate_prime_sieve(LIMIT = LIMIT*2)
divisor_prime_sieve = [True]*(LIMIT+1)

for d_ in xrange(1, LIMIT+1):
    for num in xrange(d, LIMIT+1, d):
        value = d+ num/d
        if not prime_sieve[value]:
            divisor_prime_sieve[num] = 0

ans = 0
for i in xrange(LIMIT):
    if divisor_prime_sieve[i]: ans+=i
cout('Total count -> %d\n'%(ans))
# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))