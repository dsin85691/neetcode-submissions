class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set() 
        len_rows, len_cols = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (r, c) == (destination[0], destination[1]):
                return True
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            
            for dr, dc in dirs:
                nr, nc = r, c
                # Roll until hitting a wall
                while 0 <= nr + dr < len_rows and 0 <= nc + dc < len_cols and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                
                if dfs(nr, nc):
                    return True
            return False

        return dfs(start[0], start[1])