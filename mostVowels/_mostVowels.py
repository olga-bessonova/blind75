# Write a function most_vowels that takes in a sentence 
# string and returns the word of the sentence that contains the most vowels.
def most_vowels(sentence):
  arr = sentence.split(' ')
  max_vowels = 0
  res = ''

  for w in arr:
    count = vowel_count(w)
    if count >= max_vowels:
      max_vowels = count
      res = w
  return res

def vowel_count(word):
  alpha = 'aeiou'
  count = 0

  for ch in word:
    if ch in alpha:
      count += 1
  return count

print(most_vowels("what a wonderful life")) # "wonderful"
print(most_vowels("what a wonderful lifeeeeeeeee")) # "lifeeeeeeeee"