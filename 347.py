#   #   #   #   #   #   #
#  Author phantomhive   #
#      02-08-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from prime import generate_prime, prime_factorization
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()

LIMIT = 10**7

def fix_a_b(prime1, prime2):
    size1, size2 = int(log(LIMIT, prime1)), int(log(LIMIT, prime2))
    ans = 0
    for i in xrange(1, size1+1):
        for j in xrange(1, size2+1):
            value = pow(prime1, i)*pow(prime2,j)
            if value > LIMIT: break
            ans = max(ans, value)
    return ans

primes = list(generate_prime(LIMIT=LIMIT))
ans = 0
for i in xrange(len(primes)):
    last = bisect(primes, LIMIT/primes[i])
    for j in xrange(i+1, last):
        if primes[i]!=primes[j]:
            ans+=fix_a_b(primes[i], primes[j])

cout('The sum is : %d\n'%(ans))
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
