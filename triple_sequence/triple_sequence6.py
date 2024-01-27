def recursive_triple_sequence(start, i = 1): 
  if i==0:
     return [start]
  return recursive_triple_sequence(3*start, i-1)

print(recursive_triple_sequence(2, 4)) # [2, 6, 18, 54]
print(recursive_triple_sequence(4, 5)) # [4, 12, 36, 108, 324]