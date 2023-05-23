class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(nums,start,end):
            if start == end:
                return nums[start]
            else:
                return max(nums[start] - predict(nums,start +1,end), nums[end] - predict(nums,start,end-1))
        
        result = predict(nums, 0 ,len(nums) - 1)
        
         
        if result >= 0:
            return True
        return False