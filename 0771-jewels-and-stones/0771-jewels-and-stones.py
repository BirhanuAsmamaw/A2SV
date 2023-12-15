class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Tot_jewel = 0
        for i in stones:
            if i in jewels:
                Tot_jewel += 1
        return Tot_jewel