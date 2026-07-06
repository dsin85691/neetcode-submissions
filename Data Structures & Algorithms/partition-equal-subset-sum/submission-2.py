class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If the total is odd, it cannot be split evenly.
        if total % 2:
            return False

        target = total // 2
        dp = [0] * (target + 1)

        for num in nums:
            new_dp = dp[:]

            for capacity in range(num, target + 1):
                new_dp[capacity] = max(
                    dp[capacity],
                    num + dp[capacity - num]
                )

            dp = new_dp

        return dp[target] == target