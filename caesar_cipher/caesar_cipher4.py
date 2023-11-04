# Write a method caesar_cipher that takes in a string and a number. 
# The function should return a new string where every character of the original 
# is shifted num characters in the alphabet.

# Feel free to use this variable:
# alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceasar_cipher(string, num):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  arr = list(string)
  for i,ch in enumerate(arr):
    index = alphabet.index(ch)
    arr[i] = alphabet[(index + num) % 26]

  return ''.join(arr)
   
print(ceasar_cipher("apple", 1))    # "bqqmf"
print(ceasar_cipher("bootcamp", 2)) # "dqqvecor"
print(ceasar_cipher("zebra", 4))    # "difve"