def isPalindrome(x):
  arr = list(ch for ch in str(x))

  for i in range(len(arr) // 2):
    if arr[i] != arr[-1-i]:
      return False 
  return True

# print(3//2)
print(isPalindrome(121)) # True
print(isPalindrome(-121)) # False