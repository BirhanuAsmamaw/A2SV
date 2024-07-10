class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  
        def backTracking(start , combination):
            if len(combination) == k:
                result.append(combination.copy())
                return
            for i in range(start,n + 1):
                combination.append(i)
                backTracking(i + 1, combination)
                combination.pop()
        backTracking(1, [])
        return result
            
        
