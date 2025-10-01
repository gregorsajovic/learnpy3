# Prime Nubmer: Only divisible by itself and 1
# (2, 3, 5, 7, 11, 13, 17, 19, ...)

# Composite Number: Can be factored into smaller integers
# (4 = 2 x x, 6 = 2 x 3, 8 = 2 x 2 x 2, 9 = 3 x 3, ...)

# Unit: 1

# V1) Test all divisors from 2 trough n-1 (skip 1 and n)

import math
import time

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime 
    
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


# ======= Test Function =======
# t0 = time.time()
# for n in range (1, 100000):
#     # print(n, is_prime_v1(n))
#     is_prime_v1(n)
# t1 = time.time()
# print("Time required: ", t1 - t0)

# Next step: Reduce number of divisors we check

# V2) Test all divisors from 2 through sqrt(N)
def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


t2 = time.time()
for n in range(1, 100000):
    #print(n, is_prime_v2(n))
    is_prime_v2(n)
t3 = time.time()
print(t3-t2)


# V3) 
def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime
    
    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
        return True


# ===== Test Function =====
t4 = time.time()
for n in range(1, 10000000):
    # print(n, is_prime_v3(n))
    is_prime_v3(n)
t5 = time.time()
print(t5-t4)

