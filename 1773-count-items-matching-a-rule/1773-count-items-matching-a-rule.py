class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        result = 0
        if ruleKey=='color':
            index = 1
        elif ruleKey=='type':
            index = 0
        else:
            index = 2
        for item in items:
                if ruleValue == item[index]:
                    result += 1
        return result