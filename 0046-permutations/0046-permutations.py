class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sett = set()
        while (len(sett) != factorial(len(nums))):
            shuffle(nums)
            sett.add(tuple(nums))
        return sett
