class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {str(i): set() for i in range(10)} 
    
        for i in range(0, len(rings), 2):
            color, rod = rings[i], rings[i + 1]
            rods[rod].add(color)
        count = 0
        for rod in rods.values():
            if len(rod) == 3:  
                count += 1
        
        return count
