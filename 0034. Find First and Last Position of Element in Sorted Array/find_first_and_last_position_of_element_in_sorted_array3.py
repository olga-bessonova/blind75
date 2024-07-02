def searchRange(nums, target):

    # brutal force
    res = []

    for i,n in enumerate(nums):
        if n == target:
            if len(res) < 2:
                res.append(i) 
            else:
                res[-1] = i
        elif n > target:
            break
    
    if len(res) == 0:
        return [-1,-1]
    elif len(res) == 1:
        res.append(res[0])
        return res
    else:
        return res
    
print(searchRange([5,7,7,8,8,10], target = 8)) # [3,4]
print(searchRange([5,7,7,8,8,10], target = 6)) # [-1,-1]
print(searchRange([], target = 6)) # [-1,-1]

