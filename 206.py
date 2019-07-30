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
_ = None
missing_number = [1, _, 2, _, 3, _, 4, _, 5, _, 6, _, 7, _, 8, _, 9, _, 0]

def find_num(num):
    num1 = int(str(num) + '30')
    num2 = int(str(num) + '70')
    return (num1, num2)

def check(num, missing_number):
    check_list = [int(num_) for num_ in str(num)]
    if len(check_list)!=19: return False
    for i in xrange(0, 19, 2):
        if check_list[i]!=missing_number[i]:
            return False
    return True

start_point = 10**7
down_point  = 10**8 -1
for value in xrange(start_point, down_point):
    value1, value2 = find_num(value)
    if check(pow(value1, 2), missing_number): 
        cout('Number -> %d , Square -> %d\n'%(value1, pow(value1, 2)))
        break

    if check(pow(value2, 2), missing_number):
        cout('Number -> %d , Square -> %d\n'%(value2, pow(value2, 2))) 
        break

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))