class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if '/' in i and '../'!= i and './' != i:  #kn time complexity worst "n2" best "n"
                stack.append(i)
            elif '../'==i:
                if stack:
                    stack.pop()
        return len(stack) 
            
        
        
        