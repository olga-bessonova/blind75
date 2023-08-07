# Write a function prime_factors that takes in a number and 
# returns a list containing all of the prime factors of the given number.

def prime_factors(n):
    res = []

    for i in range(2,n+1):
        if prime(i) and n % i == 0:
            res.append(i)
    return res
    
def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
    return True
  
print(prime_factors(24)) # [2, 3]
print(prime_factors(60)) # [2, 3, 5]
print(prime_factors(195)) # [3,5,13]
print(prime_factors(199)) # [199]