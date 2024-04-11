class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result=0
        for i in range(len(hours)):
            if hours[i]>=target:
                result+=1
        return result
