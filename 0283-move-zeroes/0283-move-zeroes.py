class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count], nums[i] = nums[i], nums[count]
                count +=1

        return nums
