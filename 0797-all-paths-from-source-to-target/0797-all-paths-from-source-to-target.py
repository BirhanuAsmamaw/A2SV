class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        queue =[[0]]
        target= len(graph) -1 
        result = []        
        while queue:
            temp = queue.pop(0)
            if temp[-1] == target:
                result.append(temp)            
            for neighbor in graph[temp[-1]]:
                queue.append( temp +[neighbor])       
        return result
