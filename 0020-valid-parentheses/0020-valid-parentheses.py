class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkClosing = {")" : "(" , "]" : "[" , "}" : "{", }
        for i in s:
            if i in checkClosing:
                if stack and stack[-1] == checkClosing[i] : 
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
                
        return True if not stack else  False
        
        