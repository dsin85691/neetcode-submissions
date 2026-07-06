class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums) # O(n)
        # This cannot be divided evenly 
        if total_sum % 2 == 1: 
            return False 

        # target value
        target = total_sum // 2 
        # total nums vs total sum / 2     
        N, M = len(nums), target 
        print(target)
        dp_cache = [0] * (M + 1) 

        for i in range(1, N + 1):
            row = [0]  * (M + 1)
            for c in range(1, M + 1): 
                skip = dp_cache[c]  # skip the num 
                include = 0
                if target - nums[i - 1] - dp_cache[c - nums[i - 1]] >= 0: 
                    # Current nums[i] + previously cached sum 
                    include = nums[i - 1] + dp_cache[c - nums[i - 1]] 
                row[c] = max(include, skip) # Include the maximum 
            dp_cache = row # Update the cache with the new row 
        print(dp_cache)
        return dp_cache[M] == target