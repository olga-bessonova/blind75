def search_insert(nums, target):
    # Initialize pointers
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

# Test cases
print(search_insert([1, 2, 3, 5, 6], 5))  # Output: 3
print(search_insert([1, 2, 3, 5, 6], 4))  # Output: 3
