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
from combinatorics import choose
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
LIMIT, COUNT = 5000, 2000000
n_, m_, abs_diff = 0, 0, COUNT
for n in xrange(LIMIT):
    for m in xrange(LIMIT):
        count = choose(n+1, 2) * choose(m+1, 2)
        if abs_diff > abs(count-COUNT):
            n_, m_ = n, m
            abs_diff = abs(count-COUNT)
cout('Area of required rectangle is: %d\n'%(n_*m_))

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))


