class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]  # Initialize the result matrix
        
        for i in range(n - 2):
            for j in range(n - 2):
                # Extract the 3x3 submatrix
                submatrix = [grid[i+k][j:j+3] for k in range(3)]
                # Find the maximum value in the submatrix
                max_value = grid[i][j]
                for row in submatrix:
                    for val in row:
                        max_value = max(max_value, val)
                maxLocal[i][j] = max_value
        
        return maxLocal