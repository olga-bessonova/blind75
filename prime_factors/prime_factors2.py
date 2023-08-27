# Write a function prime_factors that takes in a number and 
# returns a list containing all of the prime factors of the given number.

def prime_factors(n):
    return [x for x in range(2,n+1) if prime(x) and n % x == 0]
        
    
def prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2,num):
            if num % n == 0:
                return False
    return True
    
  
print(prime_factors(24)) # [2, 3]
print(prime_factors(60)) # [2, 3, 5]
print(prime_factors(195)) # [3,5,13]
print(prime_factors(199)) # [199]