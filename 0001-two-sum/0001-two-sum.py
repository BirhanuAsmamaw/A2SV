class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums:
                try:
                    j = nums.index(another)
                    if i != j:
                        return [i, j]
                except ValueError as e:
                    continue
        return []