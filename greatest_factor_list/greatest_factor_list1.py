# Write a function greatest_factor_list that takes in a list of numbers 
# and returns a new list where every even number is replaced with it's greatest factor. 
# A greatest factor is the largest number that divides another with no remainder. 
# For example, the greatest factor of 16 is 8. 
# (For the purpose of this problem we won't say the greatest factor of 16 is 16, 
# because that would be too easy).

def greatest_factor_list(num_list):
    res = []
    for i, num in enumerate(num_list):
        if num % 2 == 0:
            res.append(greatest_factor(num))
        else:
            res.append(num)           
    return res

def greatest_factor(num):
    for i in reversed(range(1,num)):
        if num % i == 0:
            return i

    
print(greatest_factor_list([16, 7, 9, 14])) # [8, 7, 9, 7]
print(greatest_factor_list([30, 3, 24, 21, 10])) # [15, 3, 12, 21, 5]

#better solution:
# def greatest_factor_list(num_list):
#     # your code here
#     for index, i in enumerate(num_list):
#       if i % 2 == 0:
#         num_list[index] = int(i/2)
#     return num_list