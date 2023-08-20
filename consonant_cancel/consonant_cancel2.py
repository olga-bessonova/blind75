# Write a function consonant_cancel that takes in a sentence and 
# returns a new sentence where every word begins with it's first vowel.
def consonant_cancel(sentence):
    arr = sentence.split(' ')
    # for i, word in enumerate(arr):
    #     arr[i] = remove_consonant(word)
    # print(arr)
    res = list(map(lambda word: remove_consonant(word), arr))
    return ' '.join(res)
        

def remove_consonant(word):
    vowels = 'aeiou'
    arr = list(word)
    res = []
    for i, ch in enumerate(arr):
        if ch in vowels:
            res = arr[i:]
            return ''.join(res)
        
          

print(consonant_cancel("down the rabbit hole")) # "own e abbit ole"
print(consonant_cancel("writing code is challenging")) # "iting ode is allenging"