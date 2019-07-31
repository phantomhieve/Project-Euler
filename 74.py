#   #   #   #   #   #   #
#  Author phantomhive   #
#      31-07-2019       #
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
LIMIT = 10**6
fact = [factorial(i) for i in xrange(10)]


def find_chain_count(num):
    num_found, count = set(), 0
    while num not in num_found:
        num_found.add(num)
        num = sum([ fact[int(i)] for i in str(num)])
        count+=1
        if count > 60: return float('inf')
    return len(num_found)

count = 0
for i in xrange(LIMIT):
    if find_chain_count(i)==60:
        count+=1

cout("Total count is: %d\n"%(count))




# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))

