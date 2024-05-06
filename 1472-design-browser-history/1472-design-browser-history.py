class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        while len(self.history) > self.current_index + 1:
            self.history.pop()
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(len(self.history) - 1, self.current_index + steps )
        return self.history[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
