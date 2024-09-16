import math

def pick_primes(number_list):
    res = [x for x in number_list if prime(x) == True] 
    return res

def prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True    

print(pick_primes([2, 3, 4, 5, 6]))  # [2, 3, 5]
print(pick_primes([101, 20, 103, 2017]))  # [101, 103, 2017]
