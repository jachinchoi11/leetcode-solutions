class MinStack:
    def __init__(self):
        self.minStack = []
        self.regStack = []

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)

        self.regStack.append(val)

    def pop(self) -> None:
        poppedValue = self.regStack.pop()
        if poppedValue == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.regStack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()