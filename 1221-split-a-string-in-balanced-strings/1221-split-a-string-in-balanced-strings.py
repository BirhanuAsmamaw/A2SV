class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        d = {'R':0, 'L':0}
        result = 0
        for i in s:
            if i == 'R':
                d['R'] += 1
            else:
                d['L'] += 1
            if d['R'] == d['L'] and d['R'] != 0:
                result += 1
                
        return result
