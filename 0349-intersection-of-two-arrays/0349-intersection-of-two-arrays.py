class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_elements = set()
        for num in nums1:
            if num in nums2:
                unique_elements.add(num)

        return list(unique_elements)