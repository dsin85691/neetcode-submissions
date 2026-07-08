class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins), amount

        dp = [float("inf")] * (M + 1)
        dp[0] = 0

        for c in coins: 
            row = [0] * (M + 1) 
            for a in range(1, M+1): 
                skip = dp[a] # use the previous min for the given amount
                include = float("inf")
                if a >= c: 
                    include = 1 + row[a - c]
                row[a] = min(skip, include) # Take the minimum of both possiblities
            dp = row # Update the old row with the new row 
        return dp[M] if dp[M] != float('inf') else -1