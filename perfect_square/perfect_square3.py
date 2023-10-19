# Write a function perfect_square that takes in a number and returns a boolean
# indicating whether it is a perfect square. A perfect square is a number that
# results from multiplying a number by itself. For example, 9 is a perfect square
# because 3 x 3 = 9, and 25 is a perfect square because 5 x 5 = 25.
def perfect_square(num):
  for i in range(num // 2):
    if num == i * i:
      return True
  return False

print(perfect_square(5))   # False
print(perfect_square(12))  # False
print(perfect_square(30))  # False
print(perfect_square(9))   # True
print(perfect_square(25))  # True

# print(43 // 2)