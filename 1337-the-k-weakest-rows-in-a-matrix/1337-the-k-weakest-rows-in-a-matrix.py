class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(sum(row), idx) for idx, row in enumerate(mat)]
        row_strength.sort()
        weakest_rows = [idx for _, idx in row_strength[:k]]
        return weakest_rows
mat1 = [[1,1,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k1 = 3
sol = Solution()
print(sol.kWeakestRows(mat1, k1))  # Output: [2, 0, 3]

mat2 = [[1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]]
k2 = 2
print(sol.kWeakestRows(mat2, k2))
