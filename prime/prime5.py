# Write a function prime that takes in a number and returns a boolean, 
# indicating whether the number is prime. 
# A prime number is only divisible by 1 and itself.

def prime(num):
  if num <= 1:
    return False
  if num == 2:
    return True
  for i in range(2, num / 2+1):
    if num % i == 0:
      return False
    
  return True


print(prime(2))  # True
print(prime(3))  # True
print(prime(5))  # True
print(prime(11)) # True
print(prime(4))  # False
print(prime(9))  # False
print(prime(-5)) # False