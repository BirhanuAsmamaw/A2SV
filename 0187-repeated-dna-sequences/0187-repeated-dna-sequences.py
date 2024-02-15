class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen_hash = set()
        result = set()
        
        for ed in range(len(s) - 9):
            current = s[ed : ed + 10]
            if current in seen_hash:
                result.add(current)
            seen_hash.add(current)
            
        return list(result)
        
