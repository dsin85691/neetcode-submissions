class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        land_used = set() 
        max_area = 0  
        for r in range(rows): 
            for c in range(cols): 
                # Check if value is 1 
                if grid[r][c] == 1 and (r,c) not in land_used: 
                    count = self.dfs(grid, r, c, land_used)
                    print(count)
                    max_area = max(count, max_area)

        return max_area


    def dfs(self, grid, r, c, visits): 
        rows, cols = len(grid), len(grid[0])
        count = 0 

        if min(r,c) < 0 or r == rows or c == cols or (r,c) in visits or grid[r][c] == 0: 
            return count
        
        visits.add((r,c)) 
        count+=1 

        count+=self.dfs(grid, r, c+1, visits) 
        count+=self.dfs(grid, r, c-1, visits) 
        count+=self.dfs(grid, r-1, c, visits) 
        count+=self.dfs(grid, r+1, c, visits) 

        return count