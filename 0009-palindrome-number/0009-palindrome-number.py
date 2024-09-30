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
        

# and an other possible answer for this question

        if x < 0:
            return False
        if x == 0:
            return True

    # Extract the reversed digits
        reversed_x = 0
        original_x = x
        while x > 0:
            last_digit = x % 10
            reversed_x = reversed_x * 10 + last_digit
            x //= 10

    # Check if the original and reversed numbers are the same  so that we will know if it is palindrome or not
        return original_x == reversed_x
