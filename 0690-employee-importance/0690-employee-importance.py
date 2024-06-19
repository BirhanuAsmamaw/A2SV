"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        def dfs(id):
            nonlocal importance
            for i in employees:
                if i.id != id:
                    continue
                importance += i.importance
                subordinates = len(i.subordinates)
                for j in range(subordinates):
                    dfs(i.subordinates[j])
        dfs(id)
        return importance
    
