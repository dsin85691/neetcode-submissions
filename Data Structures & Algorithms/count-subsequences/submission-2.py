class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t) 
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else: 
                    dp[i][j] = dp[i-1][j]

        return dp[N][M]