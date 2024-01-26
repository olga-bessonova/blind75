# Write a method caesar_cipher that takes in a string and a number. 
# The function should return a new string where every character of the original 
# is shifted num characters in the alphabet.

# Feel free to use this variable:
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(string, num):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  arr = list(string)
  for i in range(len(arr)):
    index = alphabet.index(arr[i])
    arr[i] = alphabet[(index + num) % 26]
  return ''.join(arr)    
   
# print(caesar_cipher("apple", 1))    # "bqqmf"
# print(caesar_cipher("bootcamp", 2)) # "dqqvecor"
# print(caesar_cipher("zebra", 4))    # "difve"
print(caesar_cipher("y", 3))    # "b"
# print(27 % 26)
# print((26+1) % 26)
# print("abcdefghijklmnopqrstuvwxyz".index('z'))
# alphabet[0] = 'b'
# print(alphabet)
# print('abcde f'.split(' '))