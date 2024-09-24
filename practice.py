# You are given a string s that consists of lower case English letters and
# brackets.
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# Your result should not contain any parentheses.
# Input: s = ")abcd("
# Input: s = "(abcd)"
# Output: "dcba"
# Input: s = "(n(a(mt)a)b)"
# "(n(atma)b)"
# "(namtab)"
# Output: "batman"


# Input: s = "(n(a)(mt)ab)"
# s = "(na(mt)ab)"
# s = "(natmab)"
# bamtan

# while '(' in arr:
# arr = array of string
# index_par = [-1,-1]
# for ch in s:
#  if ch == '(' record i index_par[0] = i
# for ch in s:
#  if ch == ')  record i index_par[1] = i
# temp_arr = arr[index_par[0] + 1, index_par[1]]

# for i in temp_arr:
# arr[index_par[0] + 1 + i] = temp_arr[-i] # "(n(a(tm)a)b)"
# remove  arr[index_par[1]] and remove arr[index_par[0]] # "(n(atma)b)"

# return string of arr

def batman(s):
  arr = list(s)
  index_par = [-1,-1]

  while '(' in arr:
    for i, ch in enumerate(arr):
      # print("i, ch: ", i, ch)
      if ch == '(':
        index_par[0] = i
      if ch == ')':
        index_par[1] = i
        break
    
    temp_arr = arr[index_par[0] + 1 : index_par[1]]
    # print("temp_arr: ", temp_arr)
    for i in range(len(temp_arr)):
      arr[index_par[0] + 1 + i] = temp_arr[-i-1] 
      # print('arr: ', arr)

    # remove parantheses:
    arr.pop(index_par[1])
    arr.pop(index_par[0])
  return ''.join(arr)

print(batman("(abcd)"))
print(batman("(n(a(mt)a)b)"))


