# Write a function, longest_common_substring(str1, str2) that takes two strings and returns the longest common substring. A substring is defined as any consecutive slice of letters from another string.

# Bonus: solve it in O(m * n) using O(m * n) extra space. (Hint: the solution involves dynamic programming which will be introduced later in the course.)
def longest_common_substring(str1, str2):
  sub = ''
  l, r = 0, len(str1) - 1

  for i in range(len(str1)-1):
    for j in range(i+1, len(str1)):
      if str1[i:j] in str2:
        if len(str1[i:j]) > len(sub):
          sub = str1[i:j]

  if len(sub) == 0:
    return None
  else:
    return sub

print(longest_common_substring('abcd','abs'))
print(longest_common_substring('abcd','index'))
# a='abcd'
# b='abc'
# c='abs'
# print(b in a)
# print(c in a)