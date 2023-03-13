class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        value = tickets[k]
        for ind,tic in enumerate(tickets):
            if ind <= k:
                if tic < value:
                    res += tic
                else:
                    res += value
            else:
                if tic < value - 1:
                    res += tic
                else:
                    res += value - 1
        return res
                    
                
        