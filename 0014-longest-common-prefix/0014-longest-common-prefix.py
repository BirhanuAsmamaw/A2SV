class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
