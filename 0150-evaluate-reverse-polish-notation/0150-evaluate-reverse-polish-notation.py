class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i in "+-*/":
                first_pop = stack.pop()
                second_pop = stack.pop()
                if i == "+":
                    stack.append(first_pop + second_pop)
                elif i == "-":
                    stack.append(second_pop - first_pop)
                elif i == "*":
                    stack.append(first_pop * second_pop)
                elif i == "/":
                    stack.append(int(second_pop / first_pop))
            else:
                stack.append(int(i))
        return stack[0]
        
        
        
