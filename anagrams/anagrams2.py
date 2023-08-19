# Write a function anagrams that takes in two words and 
# returns a boolean indicating whether or not the words are anagrams. 
# Anagrams are words that contain the same characters but not necessarily in the same order. 
# Solve this without using .sort().

def anagrams(word1, word2):
    hash = {}
    for l in word1
  
  
print(anagrams("cat", "act"))          # True
print(anagrams("restful", "fluster"))  # True
print(anagrams("cat", "dog"))          # False
print(anagrams("boot", "bootcamp"))    # False