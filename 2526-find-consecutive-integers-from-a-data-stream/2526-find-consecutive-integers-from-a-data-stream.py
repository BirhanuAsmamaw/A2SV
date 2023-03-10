class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.stream.append(num)
        else:
            self.stream = deque()
             
        if len(self.stream) == self.k:
            self.stream.popleft()
            return True
        return False
        
        # for i in range(-1,-self.k - 1,-1):
        #     if self.stream[i] != self.value:
        #         return False
            
        return True    
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)