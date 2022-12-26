class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr=s.split()
        num=[]
        for i in range(len(arr)):
            if(arr[i].isnumeric()):
                num.append(int(arr[i]))
        
        for i in range(1,len(num)):
            if (num[i]-num[i-1] <= 0):
                return False
        return True
                           
                           
                          
                           
                           
            