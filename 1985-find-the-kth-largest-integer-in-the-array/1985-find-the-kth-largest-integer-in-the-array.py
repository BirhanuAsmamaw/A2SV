class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(i) for i in nums]  # the negative is because of python has not maxheap.so, we change the max to min by -ve sign
        heapq.heapify(maxHeap)
        
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1 
        return str(-maxHeap[0])