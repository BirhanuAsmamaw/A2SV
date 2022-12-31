class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        i = 0
        arr = []
        while i < len(nums):
            if nums[i] == target:
                arr.append(i)
            i += 1
        return arr
