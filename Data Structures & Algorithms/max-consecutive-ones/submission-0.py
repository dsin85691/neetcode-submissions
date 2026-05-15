class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_bucket, bucket = 0, [0] * 1 

        for i in range(len(nums)): 
            if nums[i] == 1: 
                curr_bucket += 1 
            else: 
                curr_bucket = 0
            bucket[0] = max(curr_bucket, bucket[0])
              
        return bucket[0]