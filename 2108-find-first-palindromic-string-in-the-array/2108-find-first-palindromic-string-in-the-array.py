class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            palindromic = ''
            for j in range(len(i)):
                palindromic = i[j] + palindromic 
                if palindromic == i:
                    return i

        return ''
