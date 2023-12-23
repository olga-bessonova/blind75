def searchInsert(nums, target):
    found = False
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)

    while not found:
        i = len(nums) // 2 
        if nums[i] == target:
            found = True
            return i
        elif nums[i] < target:
            if nums[i] < target and target < nums[i+1]:
                return i+1
            else: 
              nums = nums[i:]
        else:
            if nums[i] > target and target > nums[i-1]:
                return i
            else: 
                nums = nums[:i]

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6], 2))
    
