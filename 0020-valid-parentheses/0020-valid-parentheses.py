class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        checkClosed = {")" : "(" , "]" : "[" , "}" : "{", }
        for i in s:
            if i in checkClosed:
                if stack and stack[-1] == checkClosed[i] : 
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
                
        return True if not stack else  False
        
        
