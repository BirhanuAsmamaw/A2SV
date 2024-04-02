class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = []
        for edge in edges :
            if edge[0] in result :
                return edge[0]
            if edge[1] in result :
                return edge[1]
            result.append(edge[1])
            result.append(edge[0])