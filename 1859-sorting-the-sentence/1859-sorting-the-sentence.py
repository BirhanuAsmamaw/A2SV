class Solution:
    def sortSentence(self, s: str) -> str:
        
        arr = s.split()
        num=[None]* len(arr)
        for i in range(len(arr)):
            last= int(arr[i][-1])
            num[last-1] = arr[i][:-1]
            final= ' '
        return final.join(num)
        
            
            
            
