class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heappush(heap, (i * -1))
        while len(heap) > 1:
            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1
            if x == y:
                continue
            else:
                heapq.heappush(heap, ((y - x )* -1))

        if heap:
            return heap[0] * -1
        else:
            return 0 
        
