import math

def perfect_square(num):
    if num < 0:
        return False  
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num
