class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i,j in enumerate(words):
            if x in j:
                result.append(i)
        return result
        