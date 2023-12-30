# runtime O(n), memory O(1)
def longestCommonPrefix(strs):
      prefix = strs[0]
      r = len(prefix)

      for i in range(1,len(strs)):

          while r > 0:
              # print("i, r, prefix: ", i, r, prefix)
              if prefix[0:r] == strs[i][0:min(len(strs[i]), r)]:
                  prefix = prefix[0:r]
                  break
              else:
                  r -= 1
          prefix = prefix[0:r]
          if prefix == '':
              return prefix
      return prefix
# print(longestCommonPrefix(["abca","aba","aaab"])) # 'a'
# print(longestCommonPrefix(["flower","flower","flower","flower"])) # 'flower'
# a = ["abca","aba","aaab"]
# print(sorted(a))
print(9//2)