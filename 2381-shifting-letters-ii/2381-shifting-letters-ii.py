class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        array = [0] * (len(s) + 1)
        
        for start,end,direction in shifts:
            if direction == 1:
                array[start] += 1
                
                array[end + 1] -= 1
            else:
                array[start] -= 1
                array[end + 1] += 1
        array.pop()
        
        for i in range(1,len(s)):
            array[i] += array[i-1]
        ord_s = [ ] 
        for i in s:
            ord_s.append(ord(i)) 
        for j in range (len(s)):
            ord_s[j] += array[j]
        return ''.join([chr((i - 97)  % 26 + 97) for i in ord_s])
            
                
            
        
        
        
        
        
        
        
