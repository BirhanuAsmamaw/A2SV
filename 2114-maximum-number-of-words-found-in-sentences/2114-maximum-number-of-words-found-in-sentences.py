class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for i in sentences:
            splitted = len(i.split())
            if(splitted > count):
                count =splitted
        return count