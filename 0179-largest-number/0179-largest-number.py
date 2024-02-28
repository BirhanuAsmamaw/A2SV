class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                len1 = len(nums[j])
                len2 = len(nums[j+1])
                min_idx = j + 1 if len2 < len1 else j 
                max_idx = j if min_idx == j + 1 else j + 1  
                mini = min(len1, len2)
                if nums[max_idx][0:mini] == nums[min_idx]:
                    if (nums[max_idx][mini:] + nums[min_idx]) < (nums[max_idx] )  :
                        if min_idx == j + 1:
                            nums[j],nums[j+1] = nums[j+1],nums[j]
                        continue
                if nums[j] < nums[j+1] :
                    nums[j],nums[j+1] = nums[j+1],nums[j]        
        if nums[0] == "0":
            return "0"        
        final= ''

        return final.join(nums)          

        
