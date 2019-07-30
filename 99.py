#   #   #   #   #   #   #
#  Author phantomhive   #
#      24-07-2019       #
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

with open('input99.txt', 'r') as my_file:
    data = [ map(int, line.split(',')) for line in my_file]

for list_ in data:
    key = log(list_[0])*list_[1]
    list_.append(key)
ans = max(data, key=lambda item: item[2])
cout("Base -> %d, Exp -> %d\n"%(ans[0], ans[1]))
line = data.index(ans) +1
cout("Line -> %d\n"%(line))

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))