#   #   #   #   #   #   #
#  Author phantomhive   #
#      23-07-2019       #
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

LIMIT = 10**7
eight_nine, store = 0, dict()
for num in xrange(1, LIMIT):
    start = num
    while start!=1 and start!=89:
        new_num = sum([pow(int(i), 2) for i in str(start)])
        start = new_num 
        if start in store: start = store[start]
    store[num] = start
    if start == 89: eight_nine+=1

cout("%d\n"%eight_nine)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))