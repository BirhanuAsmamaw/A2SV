class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        start = 0
        end = len(s) - 1
        for i in range(len(s)):
            if  len(s) > 1 :
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
                    break
               
                
            else:
                return True               
                break
               
        return True
            
                
