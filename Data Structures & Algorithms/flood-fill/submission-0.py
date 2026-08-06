class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N, M = len(image), len(image[0])
        visited = set() 
        bfs = deque() 
        # D, U, R, L (hor/ver)
        neis = [(1,0), (-1,0), (0,1), (0,-1)]
        bfs.append((sr, sc)) # Initial pos 
        visited.add((sr,sc))

        while bfs: 
            node_r, node_c = bfs.popleft() 
            orig_color = image[node_r][node_c]
            image[node_r][node_c] = color

            for nei in neis: 
                n_l, n_r = nei
                r, c = node_r + n_l, node_c + n_r
                # OOB check, visited check, check if image has same color
                if min(r,c) < 0 or r >= N or c >= M or (r,c) in visited or orig_color != image[r][c]: 
                    continue

                bfs.append((r,c)) 
                visited.add((r,c)) 

        return image
