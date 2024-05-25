class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 

        # Use Depth-First Search (DFS) to explore the graph        
        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor, target, visited):
                    return True
            return False

        # Execute DFS to check path existence
        return dfs(source, destination, set()) 
