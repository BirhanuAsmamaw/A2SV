class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        Sum = 0
        multiple = 1
        while n > 0:
            digit = n % 10 
            Sum += digit
            multiple *= digit
            n = n//10   
        return multiple - Sum
