class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * (n + 1)
        for a, b in trust:
            trusted_by[a] -= 1  # a trusts someone, so they can't be the elder
            trusted_by[b] += 1  # b is trusted by someone

        # Find the person who is trusted by everyone else and trusts nobody
        for i in range(1, n + 1):
            if trusted_by[i] == n - 1:
                return i
        return -1