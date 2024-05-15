class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = 0
        value = 0
        for i in s:
            if i == "(":
                stack.append(0)
            elif i == ")":
                multiplier = stack.pop()
                if multiplier == 0:
                    value = 1
                else:
                    value = multiplier * 2
                if not stack:
                    result += value
                else:
                    stack[-1] += value      
        return result
