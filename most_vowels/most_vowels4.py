# Write a function most_vowels that takes in a sentence 
# string and returns the word of the sentence that contains the most vowels.
def most_vowels(sentence):
  arr = sentence.split()
  # print(arr)
  newarr = [vow(x) for x in arr]
  # print(newarr)
  # print(max(newarr))
  # print(newarr.index(max(newarr)))
  # print(arr[newarr.index(max(newarr))])
  # print(newarr[max(newarr)])
  # print(arr.index([newarr[max(newarr)]]))
  # indexof = newarr.max()
  return arr[newarr.index(max(newarr))]
    
def vow(word):
  vowels = 'aeiou'
  res = 0
  for i in range(len(word)):
    if word[i] in vowels:
      res += 1
  return res

print(most_vowels("what a wonderful life")) # "wonderful"
print(most_vowels("what a wonderful lifeeeeeeeee")) # "lifeeeeeeeee"

# arr = [1,2,5,8,90,1]
# print(arr.max())
# print(arr.index(max(arr)))