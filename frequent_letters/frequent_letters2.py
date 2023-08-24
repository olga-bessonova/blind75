# Write a function frequent_letters that takes in a string and 
# returns a list containing the characters that appeared more than twice in a string.

def frequent_letters(string):
    hash = {}
    # for ch in string:
    #     if ch in hash:
    #         hash[ch] += 1
    #     else:
    #         hash[ch] = 1
    for ch in string:
        hash[ch] = hash.get(ch,0) + 1
    return [ch for ch in hash if hash[ch] > 2]
print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]