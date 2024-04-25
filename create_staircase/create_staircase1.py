def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      # print('step: ', step)
      # print('nums[0:step]: ', nums[0:step])
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
      # print('subsets: ', subsets)
    else:
      return False

  return subsets
print(create_staircase([1, 2, 3, 4, 5, 6])) # [[1], [2, 3], [4, 5, 6]]
print(create_staircase([1, 2, 3, 4, 5, 6, 7])) # False