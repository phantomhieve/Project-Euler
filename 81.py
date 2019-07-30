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
def find_path(data, i=0, j=0, end=80):
    if (i, j) in store: return store[(i, j)]
    if i==end-1 and j==end-1:
        return data[end-1][end-1]
    if i>=end or j>=end:
        return float('inf') 
    ans = min(
        find_path(data, i+1, j, end) + data[i][j],
        find_path(data, i, j+1, end) + data[i][j], 
    )
    store[(i, j)] = ans
    return ans




with open('input81.txt') as my_file:
        data = [ list(map(int, line.split(',')))
            for line in my_file
        ]

print find_path(data)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
