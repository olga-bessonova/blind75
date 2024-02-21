def first_consonant_cancel(sentence):
  # Split the sentence into words.
  words = sentence.split()

  # Iterate over the words in the sentence.
  for i, word in enumerate(words):
    # Find the index of the first vowel in the word.
    vowel_index = next((i for i, char in enumerate(word) if char in "aeiouAEIOU"), -1)

    # If there is a vowel in the word, remove all characters before it.
    if vowel_index != -1:
      words[i] = word[vowel_index:]
    else:
      words[i] = ''
  if '' in words:
    words = words.remove('')
  # Join the words back together into a sentence.
  new_sentence = " ".join(words)

  # Return the new sentence.
  return new_sentence

# Test the function with some example sentences.
# print(first_consonant_cancel("Hello world"))  # Output: 'ello orld'
# print(first_consonant_cancel("This is a test"))  # Output: 'is a est'
print(first_consonant_cancel("GDP ipsum dolor sit amet"))  # Output: 'orem ipsum olor it amet'