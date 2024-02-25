class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0 : 1}
        result = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if map.get(sum - k):
                result += map[sum - k]
            map[sum] = map.get(sum , 0) + 1
        return result
        
