# double_letter_count that takes in a string and 
# returns the number of times that the same letter repeats twice in a row.

def double_letter_count(string):
  count = 0
  for i in range(len(string)-1):
    if string[i] == string[i+1]:
      count += 1
  return count
   
  
print(double_letter_count("the jeep rolled down the hill")) # 3
print(double_letter_count("bootcamp")) # 1