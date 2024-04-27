class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        prime=[True]*n
        prime[0]=prime[1]=False
        
        count =0
        for i in range(2, n):
            if prime[i]:
                count +=1
                for j in range(2*i, n , i):
                    prime[j]=False      
        return count 
