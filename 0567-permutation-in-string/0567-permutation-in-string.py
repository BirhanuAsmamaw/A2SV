class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sn = len(s1)
        pn = len(s2)
        dict_p = Counter(s1)

        
        for i in range(pn-sn+1):
            dict_s = Counter(s2[i : sn + i])
            if dict_s == dict_p:
                return True   
        return False
        
        
        
