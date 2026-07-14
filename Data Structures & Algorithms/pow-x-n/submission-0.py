class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # O(log n) Time complexity 10 ---> 5 --> 2 --> 1
        def dfs(x, n): 
            # base cases
            if n == 0: 
                return 1 
            elif n == 1: 
                return x

            if n % 2 == 1: 
                return dfs(x, n // 2) * dfs(x, n // 2 + 1) 
            else: 
                return dfs(x, n // 2) * dfs(x, n // 2)
        if n >= 0:
            return dfs(x, n)
        else: 
            return 1 / dfs(x, -1 * n)