# Write a function pick_primes that takes in a list of numbers 
# and returns a new list containing only the prime numbers.

def pick_primes(number_list):
  res = [x for x in number_list if prime(x) == True] 
  return res

def prime(num):
  if num == 2:
    return True
  for i in range(2, num//2):
    if num % i == 0:
      return False
  return True    

print(pick_primes([2, 3, 4, 5, 6])) # [2, 3, 5]
print(pick_primes([101, 20, 103, 2017])) # [101, 103, 2017]