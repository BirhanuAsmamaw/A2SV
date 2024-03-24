class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique_letters = set()
        for char in sentence:
            if char.islower():
                unique_letters.add(char)

        return len(unique_letters) == 26
