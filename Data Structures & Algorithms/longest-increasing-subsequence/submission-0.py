class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)