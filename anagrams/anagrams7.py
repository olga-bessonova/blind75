# Write a function anagrams that takes in two words and 
# returns a boolean indicating whether or not the words are anagrams. 
# Anagrams are words that contain the same characters but not necessarily in the same order. 
# Solve this without using .sort().

def anagrams(word1, word2):
    hash1 = {}
    for ch in word1:
        hash1[ch] = hash1.get(ch, 0) + 1
    for ch in word2:
        if ch in hash1.keys():
            hash1[ch] -= 1
        else:
            return False
    return all(value == 0 for value in hash1.values())
  
  
print(anagrams("cat", "act"))          # True
print(anagrams("restful", "fluster"))  # True
print(anagrams("cat", "dog"))          # False
print(anagrams("boot", "bootcamp"))    # False
print(anagrams("boot", "bootboot"))    # False