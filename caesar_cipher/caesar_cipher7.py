def ceasar_cipher(string, num):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  arr = list(x for x in string)
  for i,ch in enumerate(arr):
    index = alphabet.index(ch)
    arr[i] = alphabet[(index + num) % 26]
  return ''.join(arr) 

print(ceasar_cipher("apple", 1))    # "bqqmf"
print(ceasar_cipher("bootcamp", 2)) # "dqqvecor"
print(ceasar_cipher("zebra", 4))    # "difve"