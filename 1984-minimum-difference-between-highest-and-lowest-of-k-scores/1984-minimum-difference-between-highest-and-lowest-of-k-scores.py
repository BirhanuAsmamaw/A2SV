class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        n = len(nums)
        answer = inf
        
        for end in range(k-1,n ):
            answer = min(answer, nums[end]- nums[start])
            start += 1
            
        return answer
            
            
