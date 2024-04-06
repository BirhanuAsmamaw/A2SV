class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        preFix = 1
        for i in range(n):
            result[i] = preFix
            preFix *= nums[i]
        postFix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= postFix
            postFix *= nums[i]
        return result
        
