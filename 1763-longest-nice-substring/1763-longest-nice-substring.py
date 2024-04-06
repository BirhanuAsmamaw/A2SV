class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        Sub_String = ''
        Nice_SubString = ''
       
        for en in range(len(s)):
            for start in range(en + 1):
                Sub_String = s[start: en + 1]
                if (len(set(Sub_String.lower()))) == (len(set(Sub_String))) // 2:
                    Nice_SubString = max(Nice_SubString,Sub_String,key = len)
        return Nice_SubString
            
           
        
