import math

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
