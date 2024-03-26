class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        final=[]  
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]
        for j in queries:
            if j[0] == 0:
                final.append(arr[j[1]])
            else:
                temp=arr[j[0]-1] ^ arr[j[1]]
                final.append(temp)
        return final
        
