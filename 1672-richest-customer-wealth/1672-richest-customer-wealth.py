class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            max_wealth = max(sum(i), max_wealth)

        return max_wealth
