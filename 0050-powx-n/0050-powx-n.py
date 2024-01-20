class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            if x== 0:
                return 0
            if n== 0:
                return 1
            
            result = recurse(x, n//2)
            result = result * result
            return x * result if n % 2 else result
        result = recurse(x, abs(n))
        return  result if n >= 0 else 1 / result
        
