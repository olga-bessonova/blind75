# Write a function adjacent_sum that takes in a list of numbers 
# and returns a new list containing the sums of adjacent numbers 
# in the original list. See the examples.

def adjacent_sum(num_list):
    res = []
    for i in range(0, len(num_list)-1):
        res.append(num_list[i] + num_list[i+1])
    return res
   
  
print(adjacent_sum([3, 7, 2, 11])) # [10, 9, 13], because [ 3+7, 7+2, 2+11 ]
print(adjacent_sum([2, 5, 1, 9, 2, 4])) # [7, 6, 10, 11, 6], because [2+5, 5+1, 1+9, 9+2, 2+4]