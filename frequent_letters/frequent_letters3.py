# Write a function frequent_letters that takes in a string and 
# returns a list containing the characters that appeared more than twice in a string.

def frequent_letters(string):
  hash = {}
  for i, ch in enumerate(string):
    if ch in hash:
      hash[ch] += 1
    else:
      hash[ch] = 1
  return [x for x in hash if hash[x] > 2]


print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]