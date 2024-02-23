class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()        
        for i in range(len(s)):
            s[i]=s[i][::-1]
        s=' '.join(map(str,s))
        return s
        
