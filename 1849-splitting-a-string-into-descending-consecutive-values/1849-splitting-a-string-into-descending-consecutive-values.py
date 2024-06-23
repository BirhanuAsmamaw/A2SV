class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(idx,left):
            if idx == len(s):
                return True
            for j in range(idx,len(s)):
                rt_val = int(s[idx:j+1])
                if left == rt_val + 1 and dfs(j+1, rt_val):
                    return True
            return False
        for i in range(len(s)-1):
            lt_val = int(s[:i+1])
            if dfs(i+1,lt_val):
                return True
        return False
