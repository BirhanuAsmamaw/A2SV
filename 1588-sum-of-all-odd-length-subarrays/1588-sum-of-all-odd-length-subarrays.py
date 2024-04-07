class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        answer=0
        n = len(arr)
        for i in range (n):
            for j in  range (i+1,n+1):
                if (j-i) % 2:
                    answer += sum(arr[i:j])  
        return answer
