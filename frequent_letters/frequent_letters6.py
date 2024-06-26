# Write a function frequent_letters that takes in a string and 
# returns a list containing the characters that appeared more than twice in a string.

def frequent_letters(string):
  hash = {}
  for i in range(len(string)):
    if string[i] in hash:
      hash[string[i]] += 1
    else:
      hash[string[i]] = 1
  return [x  for x in hash if hash[x] > 2]

print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]