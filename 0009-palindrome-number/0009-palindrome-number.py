class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        forWard = 0
        backWard = len(string) - 1
        
        while forWard < backWard:
            if string[forWard] != string[backWard]:
                return False
            forWard  += 1
            backWard -= 1
        return True