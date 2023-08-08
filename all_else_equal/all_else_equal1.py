# Write a function all_else_equal that takes in a list of numbers. 
# The function should return the element of the list that is equal 
# to half of the sum of all elements of the list. 
# If there is no such element, the method should return None.
def all_else_equal(num_list):
  half_sum = sum(num_list) / 2
  return half_sum if half_sum in num_list else None

print(all_else_equal([2, 4, 3, 10, 1])) # 10
print(all_else_equal([6, 3, 5, -9, 1])) # 3
print(all_else_equal([1, 2, 3, 4]))     # None

# arr = [1,2,3,4]
# print(sum(arr))
# print(10/3)

# print(arr.index(4))
# print(arr.index(5))
