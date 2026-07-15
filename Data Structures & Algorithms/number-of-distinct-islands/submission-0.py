class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n  = len(grid), len(grid[0])
        bfs = deque() # queue of visited locs 
        visited = set() # a set of visited locs 
        distinct_islands = set()
        for i in range(m): 
            for j in range(n): 
                # if the grid pos (i,j) == 1
                # Check also if it has not been visited yet
                if (i,j) not in visited and grid[i][j] == 1:
                    shape = []
                    bfs.append((i,j))
                    visited.add((i,j))
                    while bfs: 
                        # Pop from the left end of the queue 
                        x, y = bfs.popleft() 
                        shape.append((x - i, y - j))

                        # All directions
                        dirs = [ 
                            (x, y+1), # Up 
                            (x, y-1), # Down
                            (x-1, y), # Left
                            (x+1, y)  # Right
                        ]

                        for x_n, y_n in dirs: 
                            # Check boundary conds 
                            # Check that the value is also 1 from the given direction
                            # Finally check if it is already visited
                            if 0 <= x_n < m and 0 <= y_n < n and grid[x_n][y_n] == 1 and (x_n, y_n) not in visited:
                                visited.add((x_n, y_n))
                                bfs.append((x_n, y_n))
                    # Add to the set of distinct island shapes
                    distinct_islands.add(tuple(shape))    
        return len(distinct_islands)