#   #   #   #   #   #   #
#  Author phantomhive   #
#      30-07-2019       #
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
START = time()
all_fractions, LIMIT = set(), 12001

down = Fraction(1, 3)
for i in xrange(LIMIT):
    for j in xrange(i*2+1, LIMIT):
        value = Fraction(i, j)
        if value <= down: break
        all_fractions.add(value)
    #print i
print len(all_fractions)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
