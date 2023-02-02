class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(n,m):
            if n < m:
                s[n], s[m] = s[m], s[n]
                reverse(n + 1, m - 1)
        reverse(0, len(s) - 1)
           