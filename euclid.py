'''
    Implementation from geeksforgeeks :-
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
'''
def extended_euclid(a, b, x, y):
    if a==0:
        x, y = 0, 1
        return b
    x1 = y1 = 1
    gcd = extended_euclid(b%a, a, x1, y1)
    x = y1 - (b/a) * x1 
    y = x1
    return gcd

def mod_inverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        q = a // m 
  
        t = m 
   
        m = a % m 
        a = t 
        t = y 
  
        y = x - q * y 
        x = t 

    if (x < 0) : 
        x = x + m0 
  
    return x 

 