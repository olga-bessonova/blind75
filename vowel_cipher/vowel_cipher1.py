# Write a function vowel_cipher that takes in a string and 
# returns a new string where every vowel becomes the next vowel in the alphabet.

def vowel_cipher(string):
  vowels = 'aeiou'
  arr = list(string)

  for i, ch in enumerate(arr):
    if ch in vowels:
      index = vowels.index(ch)
      arr[i] = vowels[(index + 1) % 5]
  return ''.join(arr)

print(vowel_cipher("bootcamp")) # "buutcemp"
print(vowel_cipher("paper cup")) # "pepir cap"
print(vowel_cipher("hello")) # "hillu"