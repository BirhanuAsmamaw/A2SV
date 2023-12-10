class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        forWard = 0
        backWard = len(string) - 1
        mid = len(string) // 2
        
        while forWard < mid:
            if string[forWard] != string[backWard]:
                return False
            forWard += 1
            backWard -= 1
        return True