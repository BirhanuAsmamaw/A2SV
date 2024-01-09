class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictionary=dict()
        for i in s:
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
                
        for i in dictionary:
            if dictionary[i]==1:
                return s.index(i)
        return -1
        