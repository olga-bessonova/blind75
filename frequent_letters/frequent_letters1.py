# Write a function frequent_letters that takes in a string and 
# returns a list containing the characters that appeared more than twice in a string.

def frequent_letters(string):
    hash = {}
    for ch in string:
        hash[ch] = hash.get(ch,0) + 1
    return [key for key, value in hash.items() if value > 2]

print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]