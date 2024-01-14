def maximumDifference(nums):
    # print(all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)))
    max_el = nums[-1]
    max_diff = -1
    for i in reversed(range(len(nums))):
        if nums[i] >= max_el:
            max_el = nums[i]
            for j in range(0, i):
                # print("nums[i] = ", i, "nums[j] = ", j, "nums[i] - nums[j] = ", nums[i] - nums[j])
                if nums[i] - nums[j] > max_diff and nums[i] > nums[j]:
                    max_diff = nums[i] - nums[j]
    return max_diff


print(maximumDifference([999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15])) # -1
# arr = [0,1,2,3,4,5]
# def print_i(arr):
#     for i in reversed(range(len(arr))):
#         print(i)
# print(print_i([0,1,2,3,4,5]))