class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        for i in range(0,len(pref)):
            if(i==0):
                arr.append(pref[i])
            else:
                arr.append(pref[i] ^ pref[i-1])
        return arr