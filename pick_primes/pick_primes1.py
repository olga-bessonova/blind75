# Write a function pick_primes that takes in a list of numbers 
# and returns a new list containing only the prime numbers.

def pick_primes(number_list):
    res = []

    for num in number_list:
        if prime(num):
          res.append(num)  
    return res

# Helper function that returns True if num is prime
def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
              return False
    return True
    

print(pick_primes([2, 3, 4, 5, 6])) # [2, 3, 5]
print(pick_primes([101, 20, 103, 2017])) # [101, 103, 2017]