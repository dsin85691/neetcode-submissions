class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity

        dp = [0] * (M + 1) 

        for i in range(N): 
            curRow = [0] * (M + 1) 
            for c in range(1, M + 1): 
                skip = dp[c] 
                include = 0 
                if c - weight[i] >= 0: 
                    include = profit[i] + curRow[c - weight[i]]
                curRow[c] = max(include, skip) 
            dp = curRow 
        return dp[M]