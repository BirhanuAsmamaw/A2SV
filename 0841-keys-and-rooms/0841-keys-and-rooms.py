from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()  # Set to keep track of visited rooms
        stack = [0]      # Stack for DFS traversal starting from room 0
        
        while stack:
            room = stack.pop()  # Take a room from the stack
            visited.add(room)  # Mark the room as visited
            
            # Add keys from the current room to the stack if the rooms are not visited yet
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        
        # If all rooms are visited, return True; otherwise, return False
        return len(visited) == n

