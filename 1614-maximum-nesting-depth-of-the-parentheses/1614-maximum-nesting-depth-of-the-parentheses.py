class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack  = []
        result = 0
        for br in s:
            if br == "(":
                stack.append(br)
                result = max(result, len(stack))
            elif br == ")":
                stack.pop()    
        return result
    
    
