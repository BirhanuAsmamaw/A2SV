class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int:
        if not self.empty():
            first = self.queue[0]
            for i in range(self.size-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            self.size -= 1
            return first
            
    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()