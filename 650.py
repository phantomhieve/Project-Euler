#   #   #   #   #   #   #
#  Author phantomhive   #
#      29-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from time import time
from prime import prime_factorization, generate_prime
from combinatorics import choose
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
START = time()
MOD = 10**9 + 7
LIMIT = 20000

def times(my_counter, time):
    new_counter = Counter(my_counter)
    for prime in new_counter:
        new_counter[prime]*=time
    return new_counter

f_f = [0 for i in xrange(LIMIT+1)]
f_f[0] = Counter()
for i in xrange(1, LIMIT+1):
    f_f[i] = prime_factorization(i) + f_f[i-1]

denominator = [0]*(LIMIT+1)
denominator[0] = Counter()
for i in xrange(1, LIMIT+1):
    denominator[i] = denominator[i-1] +  times(f_f[i], 2)

cout('Done preprocessing\n')
def d_of_n(num):
    numerator = times(f_f[num], num+1)
    my_number = numerator - denominator[num]
    d_of_n_ = 1
    for prime, count in my_number.items():
        num = (pow(prime, count+1, MOD) - 1 +MOD)%MOD
        prime_pow_sum =  (num* pow(prime-1, MOD-2, MOD))%MOD
        d_of_n_ = (prime_pow_sum * d_of_n_)%MOD
    return d_of_n_

def s_of_n(num):
    s_of_n_ = 0
    for i in xrange(1, num+1):
        s_of_n_ = (s_of_n_ + d_of_n(i))%MOD
    return s_of_n_
    
ans  = s_of_n(LIMIT)

cout('S of n : %d\n'%ans)
# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))