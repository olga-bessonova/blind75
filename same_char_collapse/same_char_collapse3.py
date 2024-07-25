# Write a function same_char_collapse that takes in a string and returns a collapsed version of the string. 
# To collapse the string, we repeatedly delete 2 adjacent characters 
# that are the same until there are no such adjacent characters. 
# If there are multiple pairs that can be collapsed, delete the leftmost pair. 
# For example, we take the following steps to collapse "zzzxaaxy": zzzxaaxy -> zxaaxy -> zxxy -> zy

def same_char_collapse(str):
    arr = list(str)
    i = 0
    while i < len(arr) - 1:
      if arr[i] == arr[i+1]:
          arr.pop(i+1)
          arr.pop(i)
          i = 0
      i += 1
    return ''.join(arr)    
        
  
print(same_char_collapse("zzzxaaxy"))   # "zy"
# because zzzxaaxy -> zxaaxy -> zxxy -> zy
print(same_char_collapse("uqrssrqvtt")) # "uv"
# because uqrssrqvtt -> uqrrqvtt -> uqqvtt -> uvtt -> uv