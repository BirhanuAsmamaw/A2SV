class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        s = list(s)
        n = len(s)
        for i in range(n // 2):
            j = n - 1 - i
            if s[i] != s[j]:
                s[i] = min(s[i], s[j]) 
                s[j] = s[i]  
        return ''.join(s)
