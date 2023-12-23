# runtime O(log(n)) memory O(1)
def searchInsert(nums, target):
  # pointers
  l, r = 0, len(nums) - 1

  while l <= r:
      mid = (l + r) // 2

      if target == nums[mid]:
          return mid
      elif target < nums[mid]:
          r = mid -1 
      else:
          l = mid + 1
  return l

print (searchInsert([1,2,3,5,6], 5))
print (searchInsert([1,2,3,5,6], 4))
    
