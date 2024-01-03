# Write a method, digital_root(num). It should sum the digits of a positive integer. If it is greater than or equal to 10, sum the digits of the resulting number. Keep repeating until there is only one digit in the result, called the "digital root". Do not use string conversion within your method.

def digital_root(num):
  # print("num: ", num)
  if num < 10:
    return num
  # print((num % 10) + (num // 10))
  return digital_root((num % 10) + (num // 10)) 
  

print(digital_root(123)) # 6
print(digital_root(1234)) # 10 -> 1 
# print(123 % 10)
# print(123 / 10)