class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        length = len(s)
        i = 0
        while s and (i < length):
            if i % 2 == 0:
                result += s[:k][::-1]
            else:
                result += s[:k]
            s = s[k:]
            i += 1

        return result
        
