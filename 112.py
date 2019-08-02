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
LIMIT, find = 10**7, 99
increasing = lambda num_str: all([ num_str[i]>= num_str[i-1] for i in xrange(1, len(num_str))])
decreasing = lambda num_str: all([ num_str[i]<= num_str[i-1] for i in xrange(1, len(num_str))])
is_bouncy     = lambda num: not(increasing(str(num)) or decreasing(str(num)))
def find_saturation():
    bouncy = 0
    for num in xrange(101, LIMIT):
        if is_bouncy(num): 
            bouncy+=1
        percentage = bouncy/float(num)*100
        if percentage == find: 
            return num
    return num

ans = find_saturation()
cout('For 99 percent: %d\n'%ans)
# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))