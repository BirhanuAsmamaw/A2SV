class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        
        count = Counter(changed)
        changed.sort()
        ans = []
        
        for i in changed:
            if i == 0 and count[i] >= 2:
                count[i] -= 2
                ans.append(i)
            elif i > 0 and count[i] and count[i*2]:
                count[i] -= 1
                count[i*2] -= 1
                ans.append(i)
                
        return ans if len(ans) == n//2 else []
                
                