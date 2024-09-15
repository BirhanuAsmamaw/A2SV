class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        new_s = s.split()
        result = ""
        for i in range(k):
            result += new_s[i] + ' '
        return result.strip()
