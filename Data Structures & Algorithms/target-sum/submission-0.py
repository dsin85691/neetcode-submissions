class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        abs_val = sum([abs(num) for num in nums]) 
        if abs(target) > abs_val: return 0
        N, M = len(nums), 2 * abs_val

        dp = [0] * (M + 1)
        # Initialize the values for dp using offset abs_val
        dp[abs_val - nums[0]] += 1
        dp[abs_val + nums[0]] += 1

        for i in range(1, N):
            row = [0] * (M + 1)  
            for c in range(M + 1): 
                if dp[c] > 0:
                    # subtract item 
                    if c - nums[i] >= 0: 
                        row[c - nums[i]] += dp[c]
                    # add item 
                    if c + nums[i] <= M:
                        row[c + nums[i]] += dp[c]
            dp = row
        return dp[abs_val + target]