# Write a function last_index that takes in a string and a character. 
# The function should return the last index where the character can be found in the string.

def last_index(arr, ch):

  for i in reversed(range(len(arr))):
    # print(i)
    if arr[i] == ch:
      return i

print(last_index("abca", "a"))        # 3
print(last_index("mississipi", "i"))  # 9
print(last_index("octagon", "o"))     # 5
print(last_index("programming", "m")) # 7
print(last_index("programming", "u")) # 
