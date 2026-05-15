class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        # guaranteed for row1, row2, col1, col2 to be correct
        sum_region = 0

        for r in range(row1, row2+1): 
            for c in range(col1, col2+1): 
                sum_region+=self.matrix[r][c]

        return sum_region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)