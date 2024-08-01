# Write a function vowel_cipher that takes in a string and 
# returns a new string where every vowel becomes the next vowel in the alphabet.

def vowel_cipher(string):
  arr = list(string)
  res = [vowel_update(ch) for ch in arr]
  return ''.join(res)

def vowel_update(ch):
  alpha = 'aeiou'
  if ch in alpha:
    return alpha[(alpha.index(ch) + 1) % 5]
  else:
    return ch
   
    
print(vowel_cipher("bootcamp")) # "buutcemp"
print(vowel_cipher("paper cup")) # "pepir cap"