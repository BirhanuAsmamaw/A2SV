class Solution:
    def smallerNumbersThanCurrent(self,nums):
        
        count=0
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            arr.append(count)
            count=0
        return arr
