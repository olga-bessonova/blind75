def isPalindrome(x):
  if x < 0:
      return False
  
  div = 1
  while x >= 10 * div:
      div *= 10

  print(div)
  print(x // div)
  print(x % 10)

  while x:
      if x // div != x % 10: return False
      x = (x % div) // 10
      print("new x: ", x)
      div = div / 100
      print("new div: ", div)
  return True


print(isPalindrome(123454321))