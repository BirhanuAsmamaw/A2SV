class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i,strng,l):
            if i >= len(s):
                return ""		
            if s[i]=="]":
                l[0] = i 
                return ""		
            if s[i]=="[":
                return int(strng) * helper(i+1,"",l) + helper(l[0]+1, "" ,l)		
            if s[i].isnumeric():
                return helper(i + 1,strng + s[i],l)		
            else:
                return s[i] + helper(i+1,strng,l)
				
        l = [None]
        return helper(0,"",l)
