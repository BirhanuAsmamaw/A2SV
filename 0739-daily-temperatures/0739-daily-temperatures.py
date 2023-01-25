class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        stack = []
        
        for i,val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stack_Val, stack_Index = stack.pop()
                result[stack_Index ] = (i - stack_Index)
            stack.append([val,i])
        
        return result
        