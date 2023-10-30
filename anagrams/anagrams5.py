# Write a function anagrams that takes in two words and 
# returns a boolean indicating whether or not the words are anagrams. 
# Anagrams are words that contain the same characters but not necessarily in the same order. 
# Solve this without using .sort().

def anagrams(word1, word2):
  hash1 = {}
  for i in word1:
    if i in hash1:
      hash1[i] += 1
    else:
      hash1[i] = 1
  hash2 = {}
  for i in word2:
    if i in hash2:
      hash2[i] += 1
    else:
      hash2[i] = 1
  return hash1 == hash2
  
  
print(anagrams("cat", "act"))          # True
print(anagrams("restful", "fluster"))  # True
print(anagrams("cat", "dog"))          # False
print(anagrams("boot", "bootcamp"))    # False