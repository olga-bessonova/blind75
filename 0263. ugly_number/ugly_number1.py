def isUgly(n):
    factors = []
    ugly_factors = [2,3,5]
    for i in range(2, n//2+1): # 2..16
        # print("i= ", i)
        if n % i == 0 and is_prime(i): # 10
            factors.append(i)
    # print("factors: ", factors)
    if len(factors) > 0 and all(x in ugly_factors for x in factors):
        return True
    else:
        return False       

def is_prime(num):
    if num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    else: 
        for i in range(2, num//2+1):            
            if num % i == 0:
                return False
    return True

print(isUgly(1641249143)) # True
# print(5//2+5)
# print([2,3] in [2,3,5]) # True
# print(isUgly(10)) # True
# print(isUgly(15)) # True
# print(isUgly(70)) # False
# # 625 1...625 5 25
# 10 = 2 * 5
# 60: 2 3 4(2*2)
# 15: 3 5 15
# 30: true 
# 30: 2 3 5 6(2*3) 10(2 5)  

