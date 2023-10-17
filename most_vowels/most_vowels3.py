# Write a function most_vowels that takes in a sentence 
# string and returns the word of the sentence that contains the most vowels.
def most_vowels(sentence):
  arr = sentence.split(' ')
  arr_count = [vowels_count(word) for word in arr]
  return arr[arr_count.index(max(arr_count))]

def vowels_count(word):
  vowels = 'aeiou'
  count = 0
  for i, ch in enumerate(word):
    if ch in vowels:
      count += 1
  return count

print(most_vowels("what a wonderful life")) # "wonderful"
print(most_vowels("what a wonderful lifeeeeeeeee")) # "lifeeeeeeeee"