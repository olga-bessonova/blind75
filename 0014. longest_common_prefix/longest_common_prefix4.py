def longestCommonPrefix(strs):
  prefix = ''

  for i in range(len(strs[0])):
    for s in strs:
      print("i, s, prefix: ", i, s, prefix)
      if len(s) == i or s[i] != strs[0][i]:
        print("hit me!")
        return prefix
    prefix += strs[0][i]
  return prefix
# print(longestCommonPrefix(["abca","aba","aaab"])) # 'a'
# print(longestCommonPrefix(["flower","flower","flower","flower"])) # 'flower'
print(longestCommonPrefix(["flower","flow","flight"])) # 'fl'
