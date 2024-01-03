# Write a method, digital_root(num). It should sum the digits of a positive integer. If it is greater than or equal to 10, sum the digits of the resulting number. Keep repeating until there is only one digit in the result, called the "digital root". Do not use string conversion within your method.

def digital_root(num):
  arr = list(int(x) for x in str(num))
  # print(arr)
  res = sum(arr)
  while res >= 10:
    temp = list(int(x) for x in str(res))
    res = sum(temp)
  return res

print(digital_root(123)) # 6
print(digital_root(1234)) # 10 -> 1 