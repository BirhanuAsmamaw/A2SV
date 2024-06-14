class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        result = []

        for q in queries:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right + 1) // 2
                if prefix_sums[mid] <= q:
                    left = mid
                else:
                    right = mid - 1
            result.append(left)

        return result