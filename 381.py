#   #   #   #   #   #   #
#  Author phantomhive   #
#      05-08-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from prime import generate_prime_sieve
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
LIMIT = 10**8

sieve = generate_prime_sieve(LIMIT = LIMIT)
cout('Done preprocessing\n')
def s_of_p(p):
    # Wilson's Theorem
    denominator, value = 1, 0
    for i in xrange(1, 6):
        new_value = (-1 * pow(denominator, p-2, p))%p
        value = (value + new_value)%p
        denominator = (denominator * (p-i))%p
    return value

ans = 0
for num in xrange(5, LIMIT+1):
    if sieve[num]: ans+= s_of_p(num)

cout('Sum is: %d\n'%ans)
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))