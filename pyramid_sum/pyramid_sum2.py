# Write a function pyramid_sum that takes in a list of numbers 
# representing the base of a pyramid. 
# The function should return a 2D list representing a complete pyramid with the given base. 
# To construct a level of the pyramid, we take the sum of adjacent elements of the level below.
# def pyramid_sum(base):
#     res = [base]
#     while len(res[0]) >1:
#         res.insert(0, reduce_function(res[0]))
#     return res

# def reduce_function(arr):
#     res = []
#     for i in range(0, len(arr)-1):
#         res.append(arr[i] + arr[i+1])
#     return res
# print(pyramid_sum([1, 4, 6])) # [[15], [5, 10], [1, 4, 6]]
# print(pyramid_sum([3, 7, 2, 11])) # [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]
# arr = [[15], [5, 10], [1, 4, 6]]
# print([arr])
# arr.insert(0,[0])
# print(arr)


# =======================================================
# recursion
def pyramid_sum(base):
    if len(base) == 1:
        return [base]
    
    # Create the next level of the pyramid
    next_level = []
    for i in range(len(base) - 1):
        next_level.append(base[i] + base[i+1])
    
    # Recursively call pyramid_sum on the next level
    lower_pyramid = pyramid_sum(next_level)
    
    # Prepend the original base to the front of the lower pyramid
    return lower_pyramid + [base] 

# Test cases
print(pyramid_sum([1, 4, 6]))  # Output: [[15], [5, 10], [1, 4, 6]]
print(pyramid_sum([3, 7, 2, 11]))  # Output: [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]
        
        