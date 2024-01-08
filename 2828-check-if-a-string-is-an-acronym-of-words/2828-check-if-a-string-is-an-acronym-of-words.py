class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        stri =''
        for i in words:
            stri += i[0]
        if stri == s :
            return True
        else:
            return False  