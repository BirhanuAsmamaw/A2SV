class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        first_sum = [-math.inf]*n
        second_sum = [-math.inf]*n
        
        for i in range(n):
            if i>=firstLen-1:
                first_sum[i] = sum(nums[i-firstLen+1:i+1])
            if i >= secondLen -1:
                second_sum[i] = sum(nums[i-secondLen+1: i+1]) 
        max_sum = 0
        
        for i in range(firstLen-1, n):
            for j in range(secondLen-1,n):
                if j < i - firstLen+1 or j - secondLen+1 > i:
                    max_sum = max(first_sum[i]+second_sum[j], max_sum)
        return max_sum
