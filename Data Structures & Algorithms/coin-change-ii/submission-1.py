class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N, M = len(coins), amount
        dp = [0] * (M + 1) 

        # Base condition
        for j in range(amount + 1): 
            if j % coins[0] == 0: 
                dp[j] = 1
        print(dp)
        for r in range(1, len(coins)): 
            row = [0] * (M + 1)
            row[0] = 1
            for c in range(1, amount + 1): 
                skip = dp[c] 
                include = 0
                if c - coins[r] >= 0: 
                    include += row[c - coins[r]]
                combs = skip + include
                row[c] = combs 
            dp = row # Update with the new row 
        return dp[M]
