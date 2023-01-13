class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)   # see how to change number to list directly 
        num = list(num)
        for i in range(len(num)):
            for j in range(len(num)):     
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
               
        
        num1 = num[0] + num[2]
        num2 = num[1] + num[3]
        
        return int(num1) + int(num2)