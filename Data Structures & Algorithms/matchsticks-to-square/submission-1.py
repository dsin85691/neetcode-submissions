class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        length = total_length // 4
        if max(matchsticks) > length:
            return False

        n = len(matchsticks)
        dp = [float("-inf")] * (1 << n)
        matchsticks.sort(reverse=True)

        def dfs(mask):
            if mask == 0:
                return 0
            if dp[mask] != float("-inf"):
                return dp[mask]

            for i in range(n):
                if mask & (1 << i):
                    res = dfs(mask ^ (1 << i))
                    if res >= 0 and res + matchsticks[i] <= length:
                        dp[mask] = (res + matchsticks[i]) % length
                        return dp[mask]
                    if mask == (1 << n) - 1:
                        dp[mask] = -1
                        return -1

            dp[mask] = -1
            return -1

        return not dfs((1 << n) - 1)