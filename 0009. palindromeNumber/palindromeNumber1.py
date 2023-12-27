def isPalindrome(x):
  arr = list( str(x))
  print(arr)
  for i in range(len(arr) // 2 + 1):
    print(arr[i], arr[-i-1])
    print(i)
    if arr[i] != arr[-1-i]:
      return False
  return True

# print(isPalindrome(121)) # True
print(isPalindrome(-121)) # False