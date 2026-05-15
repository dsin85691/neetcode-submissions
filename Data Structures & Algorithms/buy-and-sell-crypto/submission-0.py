class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit, max_profit = 0, 0

        for R in range(1, len(prices)): 

            if cur_profit < 0: 
                cur_profit = 0 
            cur_profit += (prices[R] - prices[R-1])
            max_profit = max(max_profit, cur_profit)

        return max_profit 
        