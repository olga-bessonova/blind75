# Write a function pyramid_sum that takes in a list of numbers 
# representing the base of a pyramid. 
# The function should return a 2D list representing a complete pyramid with the given base. 
# To construct a level of the pyramid, we take the sum of adjacent elements of the level below.
def pyramid_sum(base):


print(pyramid_sum([1, 4, 6])) # [[15], [5, 10], [1, 4, 6]]
print(pyramid_sum([3, 7, 2, 11])) # [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]