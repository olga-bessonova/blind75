# Write a function frequent_letters that takes in a string and 
# returns a list containing the characters that appeared more than twice in a string.

def frequent_letters(string):
  for i in range(len(string) - 1):
    

print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]