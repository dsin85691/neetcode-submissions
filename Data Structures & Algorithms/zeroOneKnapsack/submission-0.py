class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity 

        dp = [0] * (M + 1) 
        dp[0] = 0 

        for c in range(M + 1): 
            if weight[0] <= c: 
                dp[c] = profit[0]        

        for i in range(1, N): 
            row = [0] * (M + 1) 
            for c in range(1, M+1): 
                skip = dp[c] 
                include = 0 
                if c - weight[i] >= 0: 
                    include = profit[i] + dp[c-weight[i]]
                row[c] = max(include, skip) 
            dp = row # Update the new row 
        return dp[M]