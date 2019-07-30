def choose(n, k):
    result = 1
    for invK in xrange(1, k+1):
        result*=n
        result/= invK
        n-=1
    return result

