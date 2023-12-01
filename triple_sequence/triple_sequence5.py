# Write a function triple_sequence that takes in two numbers, start and
# length. The function should return a list representing a sequence that begins
# with start and is length elements long. In the sequence, every element
# should be 3 times the previous element. Assume that the length is at least 1.
def triple_sequence(start, length): 
  count = length
  res = [start]
  while count > 1:
    res.append(res[-1] * 3)
    count -= 1
  return res


print(triple_sequence(2, 4)) # [2, 6, 18, 54]
print(triple_sequence(4, 5)) # [4, 12, 36, 108, 324]