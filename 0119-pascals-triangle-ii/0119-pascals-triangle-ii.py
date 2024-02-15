class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            ladder = []
            for j in range(i+1):
                if j==0 or j==i:
                    ladder.append(1)
                else:
                    ladder.append(result[i-1][j-1] + result[i-1][j]) 
            result.append(ladder)
            
        return result[-1]
