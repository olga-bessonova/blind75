def is_palindrome(string):
  for i in range(len(string) // 2 + 1):
    if string[i] != string[-1-i]:
      return False
    
  return True

print(is_palindrome('abcabc'))
print(is_palindrome('abccba'))
print(is_palindrome('abcba'))