# Write a function anagrams that takes in two words and 
# returns a boolean indicating whether or not the words are anagrams. 
# Anagrams are words that contain the same characters but not necessarily in the same order. 
# Solve this without using .sort().

def anagrams(word1, word2):
    hash1 = {}
    hash2 = {}
    for i,ch in enumerate(word1):
        hash1[ch] = hash1.get(ch,0) + 1
    for i,ch in enumerate(word2):
        hash2[ch] = hash2.get(ch,0) + 1
    print(hash1)
    print(hash2)
    return hash1 == hash2
  
  
print(anagrams("cat", "act"))          # True
print(anagrams("restful", "fluster"))  # True
print(anagrams("cat", "dog"))          # False
print(anagrams("boot", "bootcamp"))    # False