# runtime , memory 
def longestCommonPrefix(strs):
      sort = sorted(strs)
      first = sort[0]
      last = sort[-1]
      prefix = ''

      for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                  return prefix
            else:
                  prefix += first[i]
      return prefix
print(longestCommonPrefix(["abca","aba","aaab"])) # 'a'
print(longestCommonPrefix(["flower","flower","flower","flower"])) # 'flower'