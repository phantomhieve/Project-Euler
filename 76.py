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

store = dict()
def find_all(denominations, desired_value, index=0, current_value = 0):
    if (index, current_value) in store:
        return store[(index, current_value)]
    if current_value == desired_value: 
        return 1
    elif current_value > desired_value:
        return 0
    elif index >= len(denominations):
        return 0
    ans = sum((
        find_all(denominations, desired_value, index, current_value+ denominations[index]),
        find_all(denominations, desired_value, index+1, current_value)
    ))
    store[(index, current_value)] = ans
    return ans

NUMBER = 100
denominations = range(1, NUMBER)
print find_all(denominations, NUMBER)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))