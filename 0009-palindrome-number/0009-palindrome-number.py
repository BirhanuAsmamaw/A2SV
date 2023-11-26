class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_str = ""
        for i in str(x):
            rev_str = i + rev_str

        if rev_str == str(x):
            return True
        else:
            return False
        