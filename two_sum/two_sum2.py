# two sum
# Solution: the idea is to create a hash map. First, go through the array of number and check the difference
# between the target and an element. Add an element to a hash map.
# for example, array [2,1,5,3], target 4. 4-2 = 2, 2 is not in a hashmap, add 2 to a hash map with 
# an element position in the array 0. And so on. Once we get to the last element, the difference is 1 which is in
# the hashmap.

def twoSum(nums, target): 
  hMap = {} #hash map

  for i, n in enumerate(nums):
    diff = target - n
    while diff in hMap:
      return [hMap[diff], i]
    hMap[n] = i
  return None
  
print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]
print(twoSum([3,3], 6)) # [0,1]
print(twoSum([1,2,2,3], 3)) # [0,1]