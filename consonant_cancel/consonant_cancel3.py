#Write a function consonant_cancel that takes in a sentence and 
# returns a new sentence where every word begins with it's first vowel.
def consonant_cancel(sentence):
  arr = sentence.split(' ')
  res = [consonant_remove(word) for word in arr]
  return ' '.join(res)

def consonant_remove(word):
  arr = list(word)
  vowels = 'aeiou'
  ch = arr[0]
  while ch not in vowels:
    arr = arr[1:]
    ch = arr[0]
  # print(''.join(arr))
  return ''.join(arr)
          

print(consonant_cancel("down the rabbit hole")) # "own e abbit ole"
print(consonant_cancel("writing code is challenging")) # "iting ode is allenging"