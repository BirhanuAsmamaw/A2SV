class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for row in range(1, len(self.dp)):
            for col in range(1, len(self.dp[0])):
                self.dp[row][col]  = matrix[row - 1][col - 1] + \
                                self.dp[row - 1][col] + \
                                self.dp[row][col - 1] - \
                                self.dp[row - 1][col - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - \
                 self.dp[row1][col2 + 1] + self.dp[row1][col1]
        return result
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
