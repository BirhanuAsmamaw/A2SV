class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = 0
        n = len(s)
        ans = 0
        vowels = {'a','e','i','o','u'}
        length = 0
        v_length = 0

        while end < n:
            length += 1
            if s[end] in vowels:
                v_length += 1
            
            while length > k:
                length -= 1
                if s[start] in vowels:
                    v_length -= 1
                start += 1
            ans = max(ans, v_length)    
            end += 1
        
        return ans
        