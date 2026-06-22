class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [1, 2]

        for i in range(3,n+1):
            tmp = dp[1] 
            dp[1] = dp[1] + dp[0] 
            dp[0] = tmp 
        return dp[1]