class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range (len(nums) + 1)]
         
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, i in count.items():
            frequency[i].append(n)
        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
