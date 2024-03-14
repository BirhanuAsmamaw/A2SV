class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float(-inf)
        current_sum,left = 0,0
        
        for right in range(len(nums)):
            current_sum += nums[right]

            if right >= (k-1):
                result = max(current_sum/k,result)
                current_sum -= nums[left]
                left += 1

        return result
                
        
        
