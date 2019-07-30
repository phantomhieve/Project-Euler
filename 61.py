#   #   #   #   #   #   #
#  Author phantomhive   #
#      19-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from itertools import permutations
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write

# Start time
START = time()

def generate(function, LIMIT = 10**4, DOWN  = 10**3):
    num, index = function(1), 1
    while num < LIMIT:
        if num>= DOWN: yield num
        index += 1
        num = function(index)

all_generators = [
    list(generate(lambda num: num*(num+1)/2)), # triangle
    list(generate(lambda num: num*num)), # square 
    list(generate(lambda num: num*(3*num-1)/2)), # pentagonal
    list(generate(lambda num: num*(2*num-1))), # hexagonal
    list(generate(lambda num: num*(5*num-3)/2)), # heptagonal
    list(generate(lambda num: num*(3*num-2)))# octagonal 
]

cyclic_numbes = list()

def check_cycle(num1, num2):
    str1 = str(num1)[2:]
    str2 = str(num2)[:2]
    return str1 == str2

def iterate_levels(levels, level = 0, previous = [], depth = 5):
    if level> depth : 
        return 
    for num in all_generators[levels[level]]:
        if len(previous) and check_cycle(previous[-1], num):
            if level ==depth and check_cycle(num, previous[0]):
                cyclic_numbes.append(previous+[num])
            else:
                iterate_levels(levels, level+1, previous + [num], depth)
        elif level==0:
            iterate_levels(levels, level+1, [num], depth)

def all_iterate(size =6):
    permutes = permutations(range(6), 6)
    for permute in permutes:
        iterate_levels(permute)

all_iterate()
print sum(cyclic_numbes[0])

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))