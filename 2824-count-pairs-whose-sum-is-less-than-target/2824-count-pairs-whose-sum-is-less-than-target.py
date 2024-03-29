class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i,n):
                if i < j and nums[i] + nums[j] < target:
                    answer += 1
        return answer
