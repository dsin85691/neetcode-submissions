class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        land_used = set() 
        count = 0 
        for r in range(rows): 
            for c in range(cols): 
                # Check if value is 1 
                if grid[r][c] == '1' and (r,c) not in land_used: 
                    self.dfs(grid, r, c, rows, cols, land_used)
                    count+=1

        return count


    def dfs(self, grid, r, c, rows, cols, visits): 
        
        if min(r,c) < 0 or r == rows or c == cols or (r,c) in visits or grid[r][c] == '0': 
            return
        
        visits.add((r,c)) 

        self.dfs(grid, r, c+1, rows, cols, visits) 
        self.dfs(grid, r, c-1, rows, cols, visits) 
        self.dfs(grid, r-1, c, rows, cols, visits) 
        self.dfs(grid, r+1, c, rows, cols, visits) 

        return visits