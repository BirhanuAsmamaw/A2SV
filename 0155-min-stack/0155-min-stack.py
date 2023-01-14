class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack and val > self.minstack[-1]:
                self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()  

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()