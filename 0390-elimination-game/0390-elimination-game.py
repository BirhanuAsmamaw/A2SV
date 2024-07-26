class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remaining = n
        step = 1
        head = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
