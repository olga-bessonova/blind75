def isUgly(num):
  if num <= 0 or (2*3*5)**32 % num != 0:
    return False
  else:
    return True
  
print(isUgly(8))
print(isUgly(17))
print(isUgly(2))