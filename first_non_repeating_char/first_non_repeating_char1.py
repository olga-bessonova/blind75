# Write a function first_non_repeating_char(s) that takes a string s and 
# returns the index of the first non-repeating character. If every character repeats, return -1.

def first_non_repeating_char(s: str) -> int:
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    return -1
s = "leetcode"
first_non_repeating_char(s)  # Output: 0 (the first non-repeating character is 'l')

s = "loveleetcode"
first_non_repeating_char(s)  # Output: 2 (the first non-repeating character is 'v')

s = "aabb"
first_non_repeating_char(s)  # Output: -1 (no non-repeating characters)
