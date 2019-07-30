#   #   #   #   #   #   #
#  Author phantomhive   #
#      26-07-2019       #
#   #   #   #   #   #   #

from collections import Counter, deque, defaultdict
from math import ceil, floor, sqrt, log, factorial
from fractions import Fraction, gcd
from sys import stdin, stdout
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from time import time
from prime import is_prime
def lcm(a,b): return (a*b) / gcd(a,b)
cin, cout = stdin.readline, stdout.write
# Start time
START = time()
check_harshad = lambda num_list: not(int(''.join(str(num) for num in num_list)) %sum(num_list))

def gen_primes(num_list):
    value_ = ''.join(str(num) for num in num_list)
    last_ = ['1', '3', '7', '9']
    prime = int(value_)/sum(num_list)
    if is_prime(prime):
        for last in last_:
            value = int(value_+last)
            if is_prime(value):
                yield value

ans  = list()
def find_all(gen_num = [] , size=0, digits = 3):
    global ans
    if size > digits-1: return 
    nums = range(int(not size), 10)
    for digit in nums:
        new_gen_num = gen_num + [digit]
        if check_harshad(new_gen_num):
            primes = list(gen_primes(new_gen_num)) 
            ans += primes
            find_all(new_gen_num, size+1, digits)    
find_all(digits=13)
cout('Total count: %d\n'%(len(ans)))
cout('Total sum: %d\n'%(sum(ans)))

# End Time
END = time()
seconds = END - START
print("Total time %d minutes %d seconds"%(seconds/60, seconds%60))
