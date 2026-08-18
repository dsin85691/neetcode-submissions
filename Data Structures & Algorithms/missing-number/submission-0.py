class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums) 
        res = n
        for i in range(len(nums)): 
            res += (i - nums[i])
        return res