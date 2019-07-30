from math import sqrt
from collections import Counter

def generate_prime_sieve(LIMIT = 10**8):
    sieve = [True for i in xrange(LIMIT+1)]
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(LIMIT))+1):
        if sieve[i]:
            for j in xrange(i*i, LIMIT+1, i):
                sieve[j] = False
    return sieve

def generate_prime(LIMIT = 10**8):
    sieve = generate_prime_sieve(LIMIT)
    prime = list()
    for i in range(LIMIT+1):
        if sieve[i]:
            yield i

def is_prime(num):
    if num <=1 : return False
    for i in xrange(2, int(sqrt(num))+1):
        if num%i==0: return False
    return True

def prime_factorization(num):
    factors = Counter()
    while num%2==0:
        factors[2]+=1
        num/=2
    for i in xrange(3, int(sqrt(num))+1, 2):
        count = 0
        while num%i==0:
            factors[i]+=1
            num/=i
    if num > 2:
        factors[num]+=1
    return factors
