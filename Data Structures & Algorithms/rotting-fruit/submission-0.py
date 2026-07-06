from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        answer = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist = self.bfs(grid, r, c, rows, cols)

                    if dist == -1:
                        return -1

                    answer = max(answer, dist)

        return answer

    def bfs(self, grid, sr, sc, rows, cols):
        q = deque([(sr, sc, 0)])
        visited = {(sr, sc)}

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, d = q.popleft()

            # Found a rotten orange
            if grid[r][c] == 2:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    grid[nr][nc] != 0
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))

        return -1