def search_range(nums, target):
    res = [-1, -1]

    for i, n in enumerate(nums):
        if n == target:
            if res[0] == -1:
                res[0] = i
            res[1] = i
        elif n > target:
            break

    return res

# Test cases
print(search_range([5, 7, 7, 8, 8, 10], target=8))  # [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], target=6))  # [-1, -1]
print(search_range([], target=6))  # [-1, -1]
