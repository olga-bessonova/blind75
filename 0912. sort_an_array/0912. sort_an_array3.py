class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # arr = [0,1,2]
        # hash = {5:10}
        # arr.extend([5]*10)
        # print(arr)
        hash = {}
        for i,n in enumerate(nums):
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        
        # Find min and max among keys
        min_el = nums[0]
        max_el = nums[0]
        for i,n in enumerate(nums):
            if n < min_el:
                min_el = n
            if n > max_el:
                max_el = n

        res = []

        for i in range(min_el, max_el+1):
            if i in hash:
                res.extend([i]*hash[i])

        return res 

        