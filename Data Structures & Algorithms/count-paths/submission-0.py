class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n 
        for i in range(m - 1, -1, -1): 
            curr_row = [0] * n
            curr_row[-1] = 1 # Initialize as 1 
            for j in range(n - 2, -1, -1): 
                curr_row[j] = curr_row[j+1] + prev_row[j] 
            prev_row = curr_row 
        
        return prev_row[0] 
