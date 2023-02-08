class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        tMax = 1
        current = 0
        l = []
        for i in range(n):
            if s[i] not in l:
                current = current + 1 
                l.append(s[i])
            else:
                if current > tMax:
                    tMax = current
                l = l[l.index(s[i])+1:]
                l.append(s[i])
                current = len(l)
        if current > tMax:
            return current
        return tMax
        