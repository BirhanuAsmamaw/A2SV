class Solution:
    def repeatedCharacter(self, s: str) -> str:
        twice = set()
        for i in range(len(s)): 
            if s[i] in twice:  
                return s[i] 
            else:
                twice.add(s[i])