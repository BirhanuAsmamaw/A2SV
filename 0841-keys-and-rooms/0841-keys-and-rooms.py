class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = set()
        stack = [0]
        
        while stack:
            room = stack.pop()
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == n
