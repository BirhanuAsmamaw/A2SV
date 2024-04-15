class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        sn = len(s)
        pn= len(p)
        dict_p =Counter(p)
        
        for i in range(sn - pn + 1):
            dict_s =Counter(s[i : pn + i])
            if dict_s == dict_p:
                result.append(i)   
        return result
        
        
        
        
        
