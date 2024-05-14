# Write a function that takes an array of integers and returns their sum. Use recursion.
def sum_rec(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  else:
    arr[1] = arr[1] + arr[0]
    arr.pop(0)
    return sum_rec(arr)


print(sum_rec([1,2,3,4,5,6,10]))
print(sum([1,2,3,4,5,6,10]))
print(sum_rec([1,2,3]))