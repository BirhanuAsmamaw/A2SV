class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        for i in range(n):
            count = set()
            for j in range(i, n):
                count.add(nums[j])
                result += len(count) ** 2
        
        return result