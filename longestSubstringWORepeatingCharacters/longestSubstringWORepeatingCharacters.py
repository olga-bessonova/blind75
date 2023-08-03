# def lengthOfLongestSubstring(s):
#     charSet = set()
#     l = 0
#     res = 0

#     for r in range(len(s)):
#         while s[r] in charSet:
#             charSet.remove(s[l])
#             l += 1
#         charSet.add(s[r])
#         res = max(res, len(charSet))
#     return res
    
# print(lengthOfLongestSubstring('abcabcbb'))
# print (lengthOfLongestSubstring('bbbbb'))
# print (lengthOfLongestSubstring('pwwkew'))




def lengthOfLongestSubstring(s):
  l = 0
  resultSet = set()
  result = 0

  for r in range(len(s)):
      while s[r] in resultSet:
          resultSet.remove(s[l])
          l += 1
          print(l, r)
          print(resultSet)

# if statement doesn't work for cases like 'qrsvbspk'
      # if s[r] in resultSet:
      #     resultSet.remove(s[l])
      #     l += 1
      resultSet.add(s[r])
      print(l, r)
      print(resultSet)
      result = max(result, len(resultSet))
      # print(resultSet)
  return result

print(lengthOfLongestSubstring('qrsvbspk'))



def lengthOfLongestSubstring(s):
  l = 0
  resultSet = set()
  result = 0

  for r in range(len(s)):
      while s[r] in resultSet:
          resultSet.remove(s[l])
          l += 1

      # if statement doesn't work for cases like 'qrsvbspk'
      # if s[r] in resultSet:
      #     resultSet.remove(s[l])
      #     l += 1
      resultSet.add(s[r])
      result = max(result, len(resultSet))
  return result

print(lengthOfLongestSubstring('qrsvbspk'))