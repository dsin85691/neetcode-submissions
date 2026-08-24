class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set() 
        M, N = len(matrix), len(matrix[0])
        for r in range(M):  
            for c in range(N): 
                if matrix[r][c] == 0: 
                    rows.add(r) 
                    cols.add(c) 
        
        for c in cols: 
            for i in range(M): 
                if matrix[i][c] != 0: 
                    matrix[i][c] = 0 
        for r in rows: 
            for c in range(N): 
                if matrix[r][c] != 0: 
                    matrix[r][c] = 0