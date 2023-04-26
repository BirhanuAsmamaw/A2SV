class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Init 
        fleet = 0
        car_fleet_time = float("-inf")
        
        # Cars which are ahead are checked first
        for pos, reach_time in sorted([(position[i], (target-position[i])/speed[i]) for i in range(len(position))], reverse=True):
            
            if reach_time > car_fleet_time:
                car_fleet_time = reach_time
                fleet += 1
                
        return fleet