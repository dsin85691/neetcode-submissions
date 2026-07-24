class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n  = len(matrix), len(matrix[0])
        cache = {}
        
        def dfs(i, j, prev_val):
            # OOB or not increasing
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev_val:
                return 0
            
            if (i,j) in cache: 
                return cache[(i,j)]

            # Let the current pos be the new prev_val
            val = matrix[i][j]
            
            # Explore 4 directions
            up_lip = dfs(i - 1, j, val)
            down_lip = dfs(i + 1, j, val)
            right_lip = dfs(i, j + 1, val)
            left_lip = dfs(i, j - 1, val)
            
            cache[(i, j)] = 1 + max(up_lip, down_lip, right_lip, left_lip)
            return cache[(i, j)]

        long_LIP = 0
        for i in range(m): 
            for j in range(n): 
                lip = dfs(i, j, -1)
                long_LIP = max(lip, long_LIP)
        return long_LIP
