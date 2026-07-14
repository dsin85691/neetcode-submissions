class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {} 

        # O(log n) Time complexity 10 ---> 5 --> 2 --> 1
        def dfs(x, n, cache):
            if n in cache: 
                return cache[n] # Memoization

            # base cases
            if n == 0: 
                return 1 
            elif n == 1: 
                return x

            if n % 2 == 1: 
                cache[n // 2] = dfs(x, n // 2, cache)
                cache[n // 2 + 1] = dfs(x, n // 2 + 1, cache) 
                return cache[n // 2] * cache[n // 2 + 1]
            else: 
                cache[n // 2] = dfs(x, n // 2, cache)
                return cache[n // 2] * cache[n // 2]
        if n >= 0:
            return dfs(x, n, cache)
        else: 
            return 1 / dfs(x, -1 * n, cache)