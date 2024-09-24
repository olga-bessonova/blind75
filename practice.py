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


# use a stack for this
# and create a string we'll call res

# loop over our char
#   we'll have three cases for any char in our str
#   either: 1, its an opener, 2, its a closer, and 3, its just a letter

#   1. append res to our stack
#       res = ''

#   2. reverse what we have in res, and append what is on the top of the stack to our res

#   3. add char to res

# loop is done, return our res

def robin(s):
    stack = list()
    res = ''
    
    for char in s:
        if char == '(':
            stack.append(res)
            res = ''
            
        elif char == ')':
            res = res[::-1]
            res = stack.pop() + res
        
        else:
            res += char
            
    return res