# Write a function anagrams that takes in two words and 
# returns a boolean indicating whether or not the words are anagrams. 
# Anagrams are words that contain the same characters but not necessarily in the same order. 
# Solve this without using .sort().

def anagrams(word1, word2):
    hash1 = {}
    hash2 = {}
    for l in word1:
        hash1[l] = hash1.get(l, 0) + 1
    for l in word2:
        hash2[l] = hash2.get(l, 0) + 1
    return hash1 == hash2
  
  
print(anagrams("cat", "act"))          # True
print(anagrams("restful", "fluster"))  # True
print(anagrams("cat", "dog"))          # False
print(anagrams("boot", "bootcamp"))    # False