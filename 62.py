#   #   #   #   #   #   #
#  Author phantomhive   #
#      20-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write

# Start time
START = time()

def my_hash(num):
    hash_ = [0]*10
    while num:
        key = num%10
        hash_[key]+=1
        num/=10
    return tuple(hash_)

LIMIT = 10**4
store = defaultdict(lambda : list())

for i in xrange(1,LIMIT):
    value = pow(i, 3)
    key = my_hash(value)
    store[key].append(i)

five_cube = list()

for key, value in store.items():
    if len(value)>=5:
        five_cube.append(value)

value = min([min(array) for array in five_cube])
print pow(value, 3)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))