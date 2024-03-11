class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in s:
            while(count<len(t) and t[count]!= i):
                count += 1
            if count == len(t):
                return False
            count += 1

        return True
        
