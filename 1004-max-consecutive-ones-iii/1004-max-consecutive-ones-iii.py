class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        counts = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            counts[num] += 1
            
            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1
                
            curr_window_size = right - left + 1
            result = max(result, curr_window_size)
            
        return result