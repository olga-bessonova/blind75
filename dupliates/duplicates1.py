def find_duplicate(nums):
    for num in nums:
        index = abs(num) - 1  # Use absolute value to find the index
        
        # Check if the value at this index is already negative
        print("num, index: ", num, index)
        if nums[index] < 0:
            print("HERE")
            return abs(num)
        
        # Negate the value at this index
        nums[index] = -nums[index]
        print("new nums:", nums)

    return -1  # Return -1 if no duplicate is found (though per problem, input should have a duplicate)

# Test cases
# print(find_duplicate([1, 2, 3, 3, 4]))  # Output: 3
print(find_duplicate([3, 1, 6, 2, 2, 5]))  # Output: 2 or 5
                    #  [-1, -2, -3, 4, 5, -6]
# print(find_duplicate([5, 1, 2, 2, 5, 5]))  # Output: 2 or 5
# print(find_duplicate([0, 1, 2]))  # Output: invalid input, we should avoid such cases
