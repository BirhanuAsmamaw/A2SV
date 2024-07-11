import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]         # this is a list that is gonna be changed to heap by heapify keyword
        for x,y in points:
            dist= (x**2)+(y**2)
            minHeap.append([dist,x,y])  
        heapq.heapify(minHeap)
        
        final=[]
        while k>0:
            dist,x,y = heapq.heappop(minHeap)
            final.append(([x,y]))
            k -=1
        return final  
            
        
