class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sumMatrix = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                above = self.sumMatrix[r-1][c] if r > 0 else 0
                left = self.sumMatrix[r][c - 1] if c > 0 else 0
                corner = self.sumMatrix[r-1][c-1] if (r > 0 and c > 0) else 0

                self.sumMatrix[r][c] = above + left - corner + matrix[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2] if row1 > 0 else 0
        left = self.sumMatrix[row2][col1 - 1] if col1 > 0 else 0 
        corner = self.sumMatrix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
        
        return bottomRight - above - left + corner