class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}
        
        for right, num in enumerate(nums):
            counts[num] += 1
            while k < counts[0] :
                counts[nums[left]] -= 1
                left += 1
            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)
        return answer
