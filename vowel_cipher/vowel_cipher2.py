# Write a function vowel_cipher that takes in a string and 
# returns a new string where every vowel becomes the next vowel in the alphabet.

def vowel_cipher(string):
    arr = list(string)
    res = [cipher(x) for x in arr]
    return ''.join(res)

def cipher(ch):
    vowels = 'aeiou'
    arr_vow = list(vowels)
    if ch not in vowels:
        return ch
    else:
        return vowels[(vowels.index(ch) + 1) % 5]
    
    
   
    
print(vowel_cipher("bootcamp")) # "buutcemp"
print(vowel_cipher("paper cup")) # "pepir cap"