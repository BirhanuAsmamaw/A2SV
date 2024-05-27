class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1 
        MIN_INT = -2**31
        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            power, inc = 1, divisor
            while inc <= dividend:
                inc <<= 1
                power <<= 1
            dividend -= inc >> 1
            quotient += power >> 1
        if not negative:
            return min(MAX_INT, quotient)
        else:
            return max(MIN_INT, -quotient)
