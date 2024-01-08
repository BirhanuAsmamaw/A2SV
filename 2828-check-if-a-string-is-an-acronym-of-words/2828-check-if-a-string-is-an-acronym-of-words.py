class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym =''
        for i in words:
            acronym += i[0]
        if acronym == s :
            return True
        else:
            return False  