#Write a function consonant_cancel that takes in a sentence and 
# returns a new sentence where every word begins with it's first vowel.
def consonant_cancel(sentence):
  arr = sentence.split(' ')
  res = [word_changer(x) for x in arr]
  return ' '.join(res)

def word_changer(word):
  vowels = 'aeiou'
  for i in range(len(word)):
    if word[i] in vowels:
      return word[i:]
    else:
      i += 1
  return ''

          

print(consonant_cancel("down the rabbit hole")) # "own e abbit ole"
print(consonant_cancel("writing code is challenging")) # "iting ode is allenging"