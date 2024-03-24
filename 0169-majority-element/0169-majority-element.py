class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dicti = defaultdict(int)
        n = len(nums)
        for j in nums:
            dicti[j] += 1
            if dicti[j] > (n /2):
                return j
            
                      
