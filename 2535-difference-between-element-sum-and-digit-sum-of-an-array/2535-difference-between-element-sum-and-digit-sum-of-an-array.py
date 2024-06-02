class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        for num in nums:
            element_sum += num

        digit_sum = 0
        for num in nums:
            num_str = str(num)
            for digit_char in num_str:
                digit_sum += int(digit_char)
        
        difference = abs(element_sum - digit_sum)
        
        return difference
