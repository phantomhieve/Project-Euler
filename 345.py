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
from scipy.optimize import linear_sum_assignment
from time import time
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()

with open('input345.txt', 'r') as my_file:
    matrix = [map(lambda num: -int(num), line.split()) for line in my_file]

'''
        Using Hungarian Algorithm
        https://en.wikipedia.org/wiki/Hungarian_algorithm
        https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html
'''
row_index, col_index =  linear_sum_assignment(matrix)
ans = abs(sum([ matrix[i][j] for i, j in zip(row_index, col_index)]))
cout('The answer is: %d\n'%ans)
# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))


