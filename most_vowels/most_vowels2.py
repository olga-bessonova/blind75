# Write a function most_vowels that takes in a sentence 
# string and returns the word of the sentence that contains the most vowels.
def most_vowels(sentence):
  arr = sentence.split(' ')
  res = [vowel_count(x) for x in arr]
  return arr[res.index(max(res))]

def vowel_count(word):
  vowels = 'aeiou'
  count = 0
  for ch in word:
      if ch in vowels:
        count += 1
  return count

print(most_vowels("what a wonderful life")) # "wonderful"
print(most_vowels("what a wonderful lifeeeeeeeee")) # "lifeeeeeeeee"