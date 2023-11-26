class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [None] * 2 * n
        for i in range(n):
            result[2 * i], result[2 * i + 1] = nums[i], nums[n + i]
        return result