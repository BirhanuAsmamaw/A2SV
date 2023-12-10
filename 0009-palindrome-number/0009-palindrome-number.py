class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = []
        while x != 0:
            arr.append(x % 10)
            x = x // 10
            
        forWard = 0
        backWard = len(arr) - 1
        
        while forWard < backWard:
            if arr[forWard] != arr[backWard]:
                return False
            forWard  += 1
            backWard -= 1
        return True