"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
# create an array for s

# if len(s) is not the same as len of s array:
# return false

# empty dict
# for loop of a pattern:
#   for ch in pattern:
#     1. check if ch is noy in dict:
#       add the key-value pair
#     2. it is in dict: check if value-key matches the existicing record.
#       if yes: continue
#       if not: return False

# return True
def match(pattern, s):
  arr = s.split(' ')

  if len(arr) != len(pattern):
    return False
  
  hash = {}

  for i, ch in enumerate(pattern):
    if arr[i] in hash.values():
      for key in hash:
        if hash[key] == arr[i]:
          if key != ch:
            return False
    if ch not in hash and arr[i] not in hash.values():
      hash[ch] = arr[i]
    else:
      if hash[ch] != arr[i]:
        # print("ch: ", ch, "index: ", i)
        return False
  return True

# print(match('abba', "dog cat cat dog"))
print(match('abba', "dog dog dog dog"))
