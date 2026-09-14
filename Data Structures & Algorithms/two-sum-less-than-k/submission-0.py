class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums) 
        max_sum = -1

        i, j = 0, len(nums) - 1 

        while i < j: 

            cur_sum = nums[i] + nums[j]

            if cur_sum < k: 
                max_sum = max(max_sum, cur_sum)
                i += 1
            elif cur_sum >= k: 
                j -= 1 
            
        return max_sum