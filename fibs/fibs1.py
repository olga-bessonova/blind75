# Write a function, fibs(num) which returns the first n elements from the fibonnacci sequence, given n.
# 0 1 1 2 3 5 8 13
# 1 2 3 4 5 6 7 8
def fibs(num):
  if num == 0:
    return []
  elif num == 1:
    return [0]
  elif num == 2:
    return [0, 1]
  else:
    arr = fibs(num-1)
    arr.append(arr[-1] + arr[-2])
    return  arr
  
print(fibs(2))
print(fibs(5))
