#Write a function consonant_cancel that takes in a sentence and 
# returns a new sentence where every word begins with it's first vowel.
def consonant_cancel(sentence):
    arr = sentence.split(' ')
    words = list(map(lambda word: consonant_cancel_word(word), arr))
    
    return ' '.join(words)
      
def consonant_cancel_word(word):
    vowels = 'aeiou'
    for i, ch in enumerate(word):
        if ch in vowels:
            return word[i:len(word)]
    return None       
          

print(consonant_cancel("down the rabbit hole")) # "own e abbit ole"
print(consonant_cancel("writing code is challenging")) # "iting ode is allenging"
# print(consonant_cancel_word('dowm'))
# print(consonant_cancel_word('iiiowm'))
# print(consonant_cancel_word('huhuowm'))