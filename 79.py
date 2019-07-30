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
from itertools import product
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write

# Start time
START = time()

def check(code, possible_key):
    index, size = -1, len(possible_key)
    for c in code:
        for i in xrange(index+1, size):
            if possible_key[i]==c:
                index = i
                break
        else:
            return False
    return True

def generate(digit_count):
    return product(range(0, 10), repeat=digit_count)

with open('input79.txt', 'r') as my_file:
    keys = [ map(int, list(key.strip('\n'))) for key in my_file]

def check_all(possible_key):
    for code in keys:
        if not check(code, possible_key):
            return None
    return int(''.join(str(num) for num in possible_key))

satisfy = list()

# for size 8
possible_keys = generate(8)
for possible_key in possible_keys:
    ans = check_all(possible_key)
    if ans is not None: satisfy.append(ans)
print min(satisfy)

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
