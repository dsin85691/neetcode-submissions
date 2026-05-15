class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = {} 

        for i in range(len(nums)): 
            if nums[i] not in count_nums.keys(): 
                count_nums[nums[i]] = nums[i] 
            else: 
                return True 
        return False