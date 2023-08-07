# Write a function greatest_factor_list that takes in a list of numbers 
# and returns a new list where every even number is replaced with it's greatest factor. 
# A greatest factor is the largest number that divides another with no remainder. 
# For example, the greatest factor of 16 is 8. 
# (For the purpose of this problem we won't say the greatest factor of 16 is 16, 
# because that would be too easy).

def greatest_factor_list(num_list):
    
print(greatest_factor_list([16, 7, 9, 14])) # [8, 7, 9, 7]
print(greatest_factor_list([30, 3, 24, 21, 10])) # [15, 3, 12, 21, 5]