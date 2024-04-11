class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total_sum = 0
        for i, num in enumerate(nums):
            count_bits = 0
            index = i
            while index:
                count_bits += index & 1
                index >>= 1
            if count_bits == k:
                total_sum += num
        return total_sum
