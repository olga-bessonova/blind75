# two sum
# Solution: the idea is to create a hash map. First, go through the array of number and check the difference
# between the target and an element. Add an element to a hash map.
# for example, array [2,1,5,3], target 4. 4-2 = 2, 2 is not in a hashmap, add 2 to a hash map with 
# an element position in the array 0. And so on. Once we get to the last element, the difference is 1 which is in
# the hashmap.
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {} # create a hash map (value : index)

    for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[n] = i 
    return