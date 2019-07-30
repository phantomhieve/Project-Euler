#   #   #   #   #   #   #
#  Author phantomhive   #
#      19-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from prime import generate_prime_sieve, generate_prime, is_prime
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write

# Start time
START = time()

LIMIT = 10**8
sieve  = generate_prime_sieve(LIMIT = LIMIT)
primes = [ [prime] for prime in generate_prime(LIMIT=int(sqrt(LIMIT))) ]
cout('Done preprocessing\n')
cout('Total prime count: %d\n'%(len(list(primes))))


def is_prime_(num):
    if num >= LIMIT: return is_prime(num)
    return sieve[num]

def check(my_set):
    my_set_list = list(my_set)
    size = len(my_set_list)
    for i in xrange(size):
        for j in xrange(i+1, size):
            a = int(str(my_set_list[i])+str(my_set_list[j]))
            b = int(str(my_set_list[j])+str(my_set_list[i]))
            if not(is_prime_(a) and is_prime_(b)):
                return False
    return True


def add_level(set_1, set_2, size):
    ans = set()
    for a in set_1:
        for b in set_2:
            new_set = sorted(list( set(a) | set(b)))
            if len(new_set) == size and check(new_set):
                ans.add(tuple(new_set))
    return ans


level_2 = add_level(primes, primes, 2)
cout('Level 2 data -> %d\n'%(len(level_2)))

level_3 = add_level(level_2, primes, 3)
cout('Level 3 data -> %d\n'%(len(level_3)))

level_4 = add_level(level_3, primes, 4)
cout('Level 4 data -> %d\n'%(len(level_4)))

level_5 = add_level(level_4, primes, 5)
cout('Level 5 data -> %d\n'%(len(level_5)))

ans = min([ sum(data) for data in level_5])
cout("Sum is: %d\n"%ans)


# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))