# Write a function all_else_equal that takes in a list of numbers. 
# The function should return the element of the list that is equal 
# to half of the sum of all elements of the list. 
# If there is no such element, the method should return None.
def all_else_equal(num_list):
  half_sum = sum(num_list) / 2
  for i in range(len(num_list)):
    if num_list[i] == half_sum:
      return num_list[i]
  return None

print(all_else_equal([2, 4, 3, 10, 1])) # 10
print(all_else_equal([6, 3, 5, -9, 1])) # 3
print(all_else_equal([1, 2, 3, 4]))     # None
