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
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
LIMIT = 10**12
LIMIT_= int(ceil(sqrt(LIMIT))) 

all_values = set()
for base in xrange(2, LIMIT_+1):
    value, count = 0, 0
    while value < LIMIT:
        value+= pow(base, count)
        count+=1
        if abs(value-base) != 1 and value < LIMIT:
            all_values.add(value)
ans = sum(all_values)
cout('The sum is : %d\n'%ans)
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))