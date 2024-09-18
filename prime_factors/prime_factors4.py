import math

def prime_factors(n):
    factors = []
    for x in range(2, math.isqrt(n) + 1):
        while prime(x) and n % x == 0:
            factors.append(x)
            n //= x
    if n > 1:
        factors.append(n)
    return factors

def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, math.isqrt(num) + 1, 2):
        if num % n == 0:
            return False
    return True
