class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        ip_replace = address.replace(".","[.]")
        return ip_replace
